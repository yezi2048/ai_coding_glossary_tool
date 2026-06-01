from __future__ import annotations

import ctypes
from ctypes import wintypes
import html
import json
import queue
import re
import sys
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from tkinter import Menu, TclError, Tk
from tkinter import ttk
import tkinter as tk


APP_NAME = "码词急救包"
DEFAULT_CONFIG = {
    "glossary_path": r"data\glossary\ai_coding_beginner_glossary.md",
    "hotkey": "Ctrl+Shift+E",
    "max_selected_chars": 240,
    "restore_text_clipboard": True,
    "show_window_on_start": True,
}

MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
WM_HOTKEY = 0x0312
WM_QUIT = 0x0012
VK_CONTROL = 0x11
VK_C = 0x43
KEYEVENTF_KEYUP = 0x0002

user32 = ctypes.windll.user32


@dataclass
class Entry:
    term: str
    aliases: str
    category: str
    simple: str
    where: str
    caution: str

    @property
    def keys(self) -> list[str]:
        values = [self.term]
        for item in re.split(r"\s*/\s*|、|，|,|；|;", self.aliases):
            item = item.strip()
            if item:
                values.append(item)
        return dedupe(values)


def dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        marker = normalize(value)
        if marker and marker not in seen:
            seen.add(marker)
            result.append(value)
    return result


def normalize(value: str) -> str:
    value = html.unescape(value or "")
    value = value.strip().strip("`'\"“”‘’[]()（）<>《》")
    value = re.sub(r"\s+", " ", value)
    return value.casefold()


def clean_cell(value: str) -> str:
    value = value.replace(r"\|", "|")
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = html.unescape(value)
    value = value.replace("　", " ")
    value = re.sub(r"[ \t]+", " ", value)
    return value.strip()


def split_markdown_row(line: str) -> list[str] | None:
    line = line.rstrip("\n")
    if not line.lstrip().startswith("|"):
        return None

    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in text:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            escaped = True
            current.append(char)
            continue
        if char == "|":
            cells.append(clean_cell("".join(current)))
            current = []
            continue
        current.append(char)
    cells.append(clean_cell("".join(current)))
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


class Glossary:
    def __init__(self, entries: list[Entry]) -> None:
        self.entries = entries

    @classmethod
    def from_markdown(cls, path: Path) -> "Glossary":
        if not path.exists():
            raise FileNotFoundError(f"词库文件不存在：{path}")

        entries: list[Entry] = []
        header: list[str] | None = None
        in_glossary = False

        for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
            cells = split_markdown_row(raw_line)
            if cells and "词条" in cells and "小白解释" in cells and "操作 / 风险提醒" in cells:
                header = cells
                in_glossary = True
                continue

            if not in_glossary:
                continue

            if cells is None:
                if entries:
                    break
                continue

            if is_separator_row(cells):
                continue

            if not header:
                continue

            padded = cells + [""] * max(0, len(header) - len(cells))
            row = {header[i]: padded[i] for i in range(min(len(header), len(padded)))}
            term = row.get("词条", "").strip()
            simple = row.get("小白解释", "").strip()
            if not term or not simple:
                continue

            entries.append(
                Entry(
                    term=term,
                    aliases=row.get("别名 / 英文", "").strip(),
                    category=row.get("分类", "").strip(),
                    simple=simple,
                    where=row.get("你通常在哪里看到", "").strip(),
                    caution=row.get("操作 / 风险提醒", "").strip(),
                )
            )

        return cls(entries)

    def search(self, query: str, limit: int = 5) -> list[tuple[int, Entry, str]]:
        cleaned = normalize(query)
        if not cleaned:
            return []

        scored: list[tuple[int, Entry, str]] = []
        for entry in self.entries:
            best_score = 0
            best_key = ""
            blob = normalize(" ".join([entry.term, entry.aliases, entry.category, entry.simple, entry.where, entry.caution]))

            for key in entry.keys:
                key_norm = normalize(key)
                if not key_norm:
                    continue

                score = 0
                if cleaned == key_norm:
                    score = 120
                elif key_norm in cleaned:
                    score = 80 + min(30, len(key_norm))
                elif cleaned in key_norm:
                    score = 70 + min(25, len(cleaned))
                elif all(part in blob for part in cleaned.split()):
                    score = 45

                if score > best_score:
                    best_score = score
                    best_key = key

            if best_score:
                scored.append((best_score, entry, best_key))

        scored.sort(key=lambda item: (item[0], len(item[2])), reverse=True)
        return scored[:limit]


class HotkeyListener(threading.Thread):
    def __init__(self, events: queue.Queue[str], hotkey: str = "Ctrl+Shift+E") -> None:
        super().__init__(daemon=True)
        self.events = events
        self.hotkey = hotkey
        self.thread_id = 0
        self._stop_event = threading.Event()

    def run(self) -> None:
        self.thread_id = ctypes.windll.kernel32.GetCurrentThreadId()
        modifiers, vk = parse_hotkey(self.hotkey)
        if not user32.RegisterHotKey(None, 1, modifiers, vk):
            self.events.put("hotkey_failed")
            return

        msg = wintypes.MSG()
        try:
            while not self._stop_event.is_set():
                result = user32.GetMessageW(ctypes.byref(msg), None, 0, 0)
                if result in (0, -1):
                    break
                if msg.message == WM_HOTKEY and msg.wParam == 1:
                    self.events.put("hotkey")
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageW(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)

    def stop(self) -> None:
        self._stop_event.set()
        if self.thread_id:
            user32.PostThreadMessageW(self.thread_id, WM_QUIT, 0, 0)


def parse_hotkey(hotkey: str) -> tuple[int, int]:
    parts = [part.strip().casefold() for part in hotkey.split("+")]
    modifiers = 0
    key = ""
    for part in parts:
        if part in {"ctrl", "control"}:
            modifiers |= MOD_CONTROL
        elif part == "shift":
            modifiers |= MOD_SHIFT
        elif part == "alt":
            modifiers |= MOD_ALT
        elif part:
            key = part

    if len(key) == 1:
        return modifiers, ord(key.upper())

    named = {"space": 0x20, "enter": 0x0D, "esc": 0x1B, "escape": 0x1B}
    if key in named:
        return modifiers, named[key]

    return MOD_CONTROL | MOD_SHIFT, ord("E")


def send_ctrl_c() -> None:
    user32.keybd_event(VK_CONTROL, 0, 0, 0)
    user32.keybd_event(VK_C, 0, 0, 0)
    user32.keybd_event(VK_C, 0, KEYEVENTF_KEYUP, 0)
    user32.keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0)


def load_config(app_dir: Path) -> dict:
    config_path = app_dir / "config.json"
    config = DEFAULT_CONFIG.copy()
    if config_path.exists():
        try:
            config.update(json.loads(config_path.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            pass
    return config


def resolve_glossary_path(app_dir: Path, value: str) -> Path:
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    return app_dir / path


class GlossaryApp:
    def __init__(self, root: Tk, app_dir: Path, startup: bool = False) -> None:
        self.root = root
        self.app_dir = app_dir
        self.config = load_config(app_dir)
        self.glossary_path = resolve_glossary_path(app_dir, self.config["glossary_path"])
        self.glossary = Glossary([])
        self.events: queue.Queue[str] = queue.Queue()
        self.listener: HotkeyListener | None = None
        self.last_foreground_hwnd = 0
        self.root_hwnd = 0
        self.last_result = ""

        self.search_var = tk.StringVar()
        self.status_var = tk.StringVar(value="正在加载词库...")

        self.build_ui()
        self.reload_glossary(show_message=False)
        self.start_hotkey()
        self.poll_events()
        self.track_foreground_window()

        show_on_start = bool(self.config.get("show_window_on_start", True)) and not startup
        if show_on_start:
            self.show_window()
        else:
            self.root.withdraw()

    def build_ui(self) -> None:
        self.root.title(APP_NAME)
        self.root.geometry("760x560")
        self.root.minsize(620, 420)
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

        main = ttk.Frame(self.root, padding=12)
        main.pack(fill="both", expand=True)

        title = ttk.Label(main, text=APP_NAME, font=("Microsoft YaHei UI", 15, "bold"))
        title.pack(anchor="w")

        tip = ttk.Label(
            main,
            text="选中任意 App 里的术语后按 Ctrl+Shift+E；也可以在这里搜索或解释剪贴板。",
            foreground="#555555",
        )
        tip.pack(anchor="w", pady=(2, 10))

        search_row = ttk.Frame(main)
        search_row.pack(fill="x")
        entry = ttk.Entry(search_row, textvariable=self.search_var)
        entry.pack(side="left", fill="x", expand=True)
        entry.bind("<Return>", lambda _event: self.explain_text(self.search_var.get(), source="手动搜索"))
        entry.bind("<Button-3>", self.show_context_menu)

        ttk.Button(search_row, text="解释", command=lambda: self.explain_text(self.search_var.get(), source="手动搜索")).pack(
            side="left", padx=(8, 0)
        )
        ttk.Button(search_row, text="解释剪贴板", command=self.explain_clipboard).pack(side="left", padx=(8, 0))
        ttk.Button(search_row, text="重载词库", command=lambda: self.reload_glossary(show_message=True)).pack(
            side="left", padx=(8, 0)
        )

        self.output = tk.Text(main, wrap="word", font=("Microsoft YaHei UI", 10), height=18, padx=10, pady=10)
        self.output.pack(fill="both", expand=True, pady=(12, 8))
        self.output.bind("<Button-3>", self.show_context_menu)
        self.output.configure(state="disabled")

        bottom = ttk.Frame(main)
        bottom.pack(fill="x")
        ttk.Label(bottom, textvariable=self.status_var, foreground="#666666").pack(side="left")
        ttk.Button(bottom, text="隐藏", command=self.hide_window).pack(side="right")
        ttk.Button(bottom, text="退出", command=self.quit).pack(side="right", padx=(0, 8))

        self.context_menu = Menu(self.root, tearoff=False)
        self.context_menu.add_command(label="解释刚才选中的文字", command=self.explain_previous_selection)
        self.context_menu.add_command(label="解释剪贴板", command=self.explain_clipboard)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="复制当前解释", command=self.copy_current_result)
        self.context_menu.add_command(label="重载词库", command=lambda: self.reload_glossary(show_message=True))
        self.context_menu.add_separator()
        self.context_menu.add_command(label="退出", command=self.quit)

    def start_hotkey(self) -> None:
        self.listener = HotkeyListener(self.events, self.config.get("hotkey", "Ctrl+Shift+E"))
        self.listener.start()

    def poll_events(self) -> None:
        try:
            while True:
                event = self.events.get_nowait()
                if event == "hotkey":
                    self.explain_current_selection()
                elif event == "hotkey_failed":
                    self.status_var.set("全局快捷键注册失败：Ctrl+Shift+E 可能被其他软件占用。")
        except queue.Empty:
            pass
        self.root.after(120, self.poll_events)

    def track_foreground_window(self) -> None:
        if self.root_hwnd == 0:
            try:
                self.root_hwnd = int(self.root.winfo_id())
            except TclError:
                self.root_hwnd = 0

        hwnd = user32.GetForegroundWindow()
        if hwnd and hwnd != self.root_hwnd:
            self.last_foreground_hwnd = hwnd

        self.root.after(300, self.track_foreground_window)

    def reload_glossary(self, show_message: bool) -> None:
        try:
            self.glossary = Glossary.from_markdown(self.glossary_path)
            self.status_var.set(f"已加载 {len(self.glossary.entries)} 个词条 | 快捷键：{self.config.get('hotkey', 'Ctrl+Shift+E')}")
            if show_message:
                self.write_output(f"已重载词库：{self.glossary_path}\n\n当前词条数：{len(self.glossary.entries)}")
        except Exception as exc:
            self.status_var.set("词库加载失败")
            self.write_output(f"词库加载失败：{exc}")

    def explain_current_selection(self) -> None:
        text = self.copy_selected_text(refocus_previous=False)
        self.explain_text(text, source="选中文字")

    def explain_previous_selection(self) -> None:
        text = self.copy_selected_text(refocus_previous=True)
        self.explain_text(text, source="刚才选中文字")

    def explain_clipboard(self) -> None:
        self.explain_text(self.get_clipboard_text() or "", source="剪贴板")

    def explain_text(self, text: str, source: str) -> None:
        text = (text or "").strip()
        max_len = int(self.config.get("max_selected_chars", 240))
        if len(text) > max_len:
            text = text[:max_len]

        self.show_window()
        self.search_var.set(text)

        if not text:
            self.write_output(
                "没有读到文字。\n\n"
                "用法：先在任意 App 或浏览器里选中一个术语，然后按 Ctrl+Shift+E。\n"
                "如果当前软件不允许自动复制，可以先 Ctrl+C，再点“解释剪贴板”。"
            )
            return

        matches = self.glossary.search(text)
        if not matches:
            self.write_output(
                f"暂时没在本地词库里找到：{text}\n\n"
                "可以先把这个词补进 Markdown 词库，再点“重载词库”。\n\n"
                "建议新增字段：词条、别名 / 英文、分类、小白解释、你通常在哪里看到、操作 / 风险提醒。"
            )
            return

        blocks = [f"查询来源：{source}\n查询内容：{text}\n"]
        for index, (_score, entry, matched_key) in enumerate(matches, start=1):
            blocks.append(self.format_entry(entry, matched_key, index))
        self.write_output("\n\n".join(blocks))

    def format_entry(self, entry: Entry, matched_key: str, index: int) -> str:
        alias_line = f"\n别名/英文：{entry.aliases}" if entry.aliases else ""
        where_line = entry.where or "词库里还没写常见场景。"
        caution_line = entry.caution or "词库里还没写风险提醒。"
        category_line = f"分类：{entry.category}" if entry.category else "分类：未分类"

        return (
            f"{index}. {entry.term}\n"
            f"{category_line}{alias_line}\n"
            f"匹配到：{matched_key}\n\n"
            f"小白版解释：\n{entry.simple}\n\n"
            f"你通常会在哪里看到：\n{where_line}\n\n"
            f"操作/风险提醒：\n{caution_line}\n\n"
            "问 AI 工具时可以这样补一句：\n"
            f"“我在某个软件里看到 `{entry.term}`，请用小白能懂的话解释，并告诉我可不可以点或执行。”"
        )

    def copy_selected_text(self, refocus_previous: bool) -> str:
        previous_clipboard = self.get_clipboard_text()
        if refocus_previous and self.last_foreground_hwnd:
            user32.SetForegroundWindow(self.last_foreground_hwnd)
            time.sleep(0.12)

        send_ctrl_c()
        time.sleep(0.18)

        text = self.get_clipboard_text() or ""
        if self.config.get("restore_text_clipboard", True) and previous_clipboard is not None:
            self.set_clipboard_text(previous_clipboard)

        return text

    def get_clipboard_text(self) -> str | None:
        for _ in range(8):
            try:
                return self.root.clipboard_get()
            except TclError:
                time.sleep(0.04)
        return None

    def set_clipboard_text(self, text: str) -> None:
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.root.update_idletasks()
        except TclError:
            pass

    def write_output(self, text: str) -> None:
        self.last_result = text
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")

    def copy_current_result(self) -> None:
        if self.last_result:
            self.set_clipboard_text(self.last_result)
            self.status_var.set("已复制当前解释到剪贴板。")

    def show_context_menu(self, event: tk.Event) -> None:
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def show_window(self) -> None:
        self.root.deiconify()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(700, lambda: self.root.attributes("-topmost", False))

    def hide_window(self) -> None:
        self.root.withdraw()

    def quit(self) -> None:
        if self.listener:
            self.listener.stop()
        self.root.destroy()


def run_self_test(app_dir: Path) -> int:
    config = load_config(app_dir)
    glossary = Glossary.from_markdown(resolve_glossary_path(app_dir, config["glossary_path"]))
    samples = ["push origin", "DNS", "npm run build", "API Key", "git push origin main"]
    print(f"loaded_entries={len(glossary.entries)}")
    for sample in samples:
        matches = glossary.search(sample, limit=1)
        if matches:
            print(f"{sample} -> {matches[0][1].term}")
        else:
            print(f"{sample} -> NOT_FOUND")
            return 1
    return 0


def main() -> int:
    app_dir = Path(__file__).resolve().parent
    if "--self-test" in sys.argv:
        return run_self_test(app_dir)

    startup = "--startup" in sys.argv
    root = Tk()
    app = GlossaryApp(root, app_dir, startup=startup)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        app.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

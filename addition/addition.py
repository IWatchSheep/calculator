from decimal import Decimal, InvalidOperation, localcontext
import tkinter as tk

class AdditionCalculator:
    BASE_WIDTH: int = 18
    MAX_CANVAS_HEIGHT: int = 240

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Addition Calculator")
        self.root.resizable(True, True)

        self.addends: list[str] = ["", ""]
        self.current_index: int = 0
        self.calculated: bool = False

        self.addend_frames: list[tk.Frame] = []
        self.addend_labels: list[tk.Label] = []
        self.addend_entries: list[tk.Entry] = []
        self.addend_vars: list[tk.StringVar] = []

        self._create_widgets()
        self._bind_keys()
        self._update_active_highlight()

        self.root.update_idletasks()
        self.root.minsize(280, 260)

    @staticmethod
    def _get_label_text(index: int) -> str:
        ordinals = [
            "First", "Second", "Third", "Fourth", "Fifth",
            "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"
        ]
        name = f"{ordinals[index]} Addend" if index < len(ordinals) else f"Addend {index + 1}"
        return name if index == 0 else f"{name} (+)"

    def _create_widgets(self) -> None:
        # Scrollable container nested above the box keypad
        self.scroll_container = tk.Frame(self.root)
        self.scroll_container.pack(side="top", fill="both", expand=True, padx=12, pady=(10, 4))

        self.canvas = tk.Canvas(self.scroll_container, highlightthickness=0, bd=0)
        self.scrollbar = tk.Scrollbar(self.scroll_container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.displays_frame = tk.Frame(self.canvas)
        self.canvas_window_id = self.canvas.create_window((0, 0), window=self.displays_frame, anchor="nw")

        self.displays_frame.bind("<Configure>", self._on_displays_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        self._bind_mousewheel(self.scroll_container)
        self._bind_mousewheel(self.canvas)
        self._bind_mousewheel(self.displays_frame)

        self.scroll_container.bind("<Enter>", lambda _e: self.root.bind_all("<MouseWheel>", self._on_mousewheel))
        self.scroll_container.bind("<Leave>", lambda _e: self.root.unbind_all("<MouseWheel>"))

        # Initial two addend windows
        for i in range(2):
            self._create_addend_widget(i)

        # Result window (always at the bottom of the displays area)
        self.result_frame = tk.Frame(self.displays_frame)
        self.result_frame.pack(side="top", fill="x", expand=True, pady=(6, 2))
        self._bind_mousewheel(self.result_frame)

        self.result_label = tk.Label(
            self.result_frame,
            text="Result (=)",
            font=("Segoe UI", 9, "bold"),
            fg="#2e7d32",
            anchor="w",
        )
        self.result_label.pack(fill="x")
        self._bind_mousewheel(self.result_label)

        self.result_var = tk.StringVar(value="")
        self.result_entry = tk.Entry(
            self.result_frame,
            textvariable=self.result_var,
            font=("Consolas", 16, "bold"),
            justify="right",
            state="readonly",
            readonlybackground="#f4f9f4",
            fg="#1b5e20",
            bd=3,
            relief="sunken",
            width=self.BASE_WIDTH,
        )
        self.result_entry.pack(fill="x", expand=True)
        self._bind_mousewheel(self.result_entry)

        # Keypad container (maintains compact box shape regardless of window stretching)
        self.keypad_frame = tk.Frame(self.root)
        self.keypad_frame.pack(side="top", pady=(4, 12))
        self._create_keypad()

    def _bind_mousewheel(self, widget: tk.Widget) -> None:
        widget.bind("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event) -> None:
        if getattr(event, "delta", 0):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_displays_configure(self, _event) -> None:
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        req_w = self.displays_frame.winfo_reqwidth()
        req_h = self.displays_frame.winfo_reqheight()
        target_h = min(req_h, self.MAX_CANVAS_HEIGHT)
        self.canvas.configure(width=req_w, height=target_h)

    def _on_canvas_configure(self, event) -> None:
        self.canvas.itemconfig(self.canvas_window_id, width=event.width)

    def _create_addend_widget(self, index: int) -> None:
        f = tk.Frame(self.displays_frame)
        f.pack(side="top", fill="x", expand=True, pady=2)
        self._bind_mousewheel(f)

        lbl = tk.Label(
            f,
            text=self._get_label_text(index),
            font=("Segoe UI", 9),
            fg="#555555",
            anchor="w",
        )
        lbl.pack(fill="x")
        self._bind_mousewheel(lbl)

        var = tk.StringVar(value=self.addends[index])
        entry = tk.Entry(
            f,
            textvariable=var,
            font=("Consolas", 16),
            justify="right",
            state="readonly",
            readonlybackground="#ffffff",
            bd=3,
            relief="sunken",
            width=self.BASE_WIDTH,
        )
        entry.pack(fill="x", expand=True)
        entry.bind("<Button-1>", lambda _e, idx=index: self._set_active_index(idx))
        self._bind_mousewheel(entry)

        self.addend_frames.append(f)
        self.addend_labels.append(lbl)
        self.addend_vars.append(var)
        self.addend_entries.append(entry)

    def _create_keypad(self) -> None:
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("+", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("C", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("=", 2, 3),
            ("0", 3, 0), (".", 3, 2),
        ]

        for text, r, c in buttons:
            cmd = lambda t=text: self.on_button_click(t)
            bg = "#e0e0e0"
            fg = "#000000"
            if text == "+":
                bg = "#ffb74d"
            elif text == "=":
                bg = "#4caf50"
                fg = "#ffffff"
            elif text == "C":
                bg = "#e57373"
                fg = "#ffffff"

            btn = tk.Button(
                self.keypad_frame,
                text=text,
                font=("Consolas", 16, "bold"),
                width=4,
                height=2,
                bg=bg,
                fg=fg,
                activebackground="#cccccc",
                command=cmd,
            )
            if text == "0":
                btn.grid(row=r, column=c, columnspan=2, padx=4, pady=4, sticky="nsew")
            elif text == "=":
                btn.grid(row=r, column=c, rowspan=2, padx=4, pady=4, sticky="nsew")
            else:
                btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

    def _bind_keys(self) -> None:
        for digit in "0123456789":
            self.root.bind(digit, lambda _e, d=digit: self.on_button_click(d))
            self.root.bind(f"<KP_{digit}>", lambda _e, d=digit: self.on_button_click(d))
        self.root.bind("+", lambda _e: self.on_button_click("+"))
        self.root.bind("<KP_Add>", lambda _e: self.on_button_click("+"))
        self.root.bind("<Return>", lambda _e: self.on_button_click("="))
        self.root.bind("<KP_Enter>", lambda _e: self.on_button_click("="))
        self.root.bind("=", lambda _e: self.on_button_click("="))
        self.root.bind("<Escape>", lambda _e: self.on_button_click("C"))
        self.root.bind("<BackSpace>", lambda _e: self.on_backspace())
        self.root.bind(".", lambda _e: self.on_button_click("."))
        self.root.bind("<KP_Decimal>", lambda _e: self.on_button_click("."))

    def _set_active_index(self, index: int) -> None:
        self.current_index = index
        self._update_active_highlight()
        self._ensure_active_visible()

    def _ensure_active_visible(self) -> None:
        if 0 <= self.current_index < len(self.addend_frames):
            self.root.update_idletasks()
            f = self.addend_frames[self.current_index]
            total_h = self.displays_frame.winfo_reqheight()
            if total_h > 0:
                y = f.winfo_y()
                self.canvas.yview_moveto(y / total_h)

    def _update_active_highlight(self) -> None:
        for i, lbl in enumerate(self.addend_labels):
            base_txt = self._get_label_text(i)
            if i == self.current_index and not self.calculated:
                lbl.config(text=f"▶ {base_txt}", font=("Segoe UI", 9, "bold"), fg="#1976d2")
                self.addend_entries[i].config(readonlybackground="#eef5fc")
            else:
                lbl.config(text=base_txt, font=("Segoe UI", 9), fg="#555555")
                self.addend_entries[i].config(readonlybackground="#ffffff")

    def add_addend_window(self) -> None:
        """Pops up another addend window below the rest and above the result and keypad."""
        self.addends.append("")
        idx = len(self.addends) - 1
        self.result_frame.pack_forget()
        self._create_addend_widget(idx)
        self.result_frame.pack(side="top", fill="x", expand=True, pady=(6, 2))
        self._update_entry_widths()
        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def _remove_last_addend_window(self) -> None:
        if len(self.addends) > 2:
            self.addends.pop()
            f = self.addend_frames.pop()
            f.destroy()
            self.addend_labels.pop()
            self.addend_entries.pop()
            self.addend_vars.pop()
            self._update_entry_widths()

    def _update_entry_widths(self) -> None:
        """Stretches display windows if large numbers are entered."""
        lengths = [len(v.get()) for v in self.addend_vars] + [len(self.result_var.get())]
        max_len = max(lengths + [self.BASE_WIDTH])
        target_width = max_len + 2
        for entry in self.addend_entries:
            entry.config(width=target_width)
        self.result_entry.config(width=target_width)

        self.root.update_idletasks()
        needed_w = self.displays_frame.winfo_reqwidth() + self.scrollbar.winfo_reqwidth() + 32
        if needed_w > self.root.winfo_width():
            self.root.geometry(f"{needed_w}x{self.root.winfo_height()}")

    def on_button_click(self, char: str) -> None:
        if char == "C":
            self.clear_all()
        elif char == "=":
            self.calculate()
        elif char == "+":
            self.handle_plus()
        elif char == ".":
            self.handle_decimal()
        else:
            self.handle_digit(char)

    def handle_digit(self, digit: str) -> None:
        if self.calculated:
            self.clear_all()
        cur = self.addends[self.current_index]
        self.addends[self.current_index] = cur + digit
        self.addend_vars[self.current_index].set(self.addends[self.current_index])
        self._update_entry_widths()

    def handle_decimal(self) -> None:
        if self.calculated:
            self.clear_all()
        cur = self.addends[self.current_index]
        if "." not in cur:
            self.addends[self.current_index] = cur + "." if cur else "0."
            self.addend_vars[self.current_index].set(self.addends[self.current_index])
            self._update_entry_widths()

    def handle_plus(self) -> None:
        if self.calculated:
            res = self.result_var.get()
            self.clear_all()
            self.addends[0] = res
            self.addend_vars[0].set(res)
            self.current_index = 1
            self.calculated = False
            self._update_active_highlight()
            self._update_entry_widths()
            return

        if self.current_index == 0:
            if not self.addends[0]:
                self.addends[0] = "0"
                self.addend_vars[0].set("0")
            self.current_index = 1
            self._update_active_highlight()
            return

        # If already on the last addend and '+' is pressed again,
        # automatically pop up another window below the rest
        if self.current_index == len(self.addends) - 1:
            if not self.addends[self.current_index]:
                return
            self.add_addend_window()
            self.current_index = len(self.addends) - 1
            self._update_active_highlight()
        else:
            self.current_index += 1
            self._update_active_highlight()

    def on_backspace(self) -> None:
        if self.calculated:
            self.clear_all()
            return

        cur = self.addends[self.current_index]
        if cur:
            self.addends[self.current_index] = cur[:-1]
            self.addend_vars[self.current_index].set(self.addends[self.current_index])
            self._update_entry_widths()
        else:
            # If current window is empty and was dynamically added, remove it
            if self.current_index > 1 and self.current_index == len(self.addends) - 1:
                self._remove_last_addend_window()
                self.current_index -= 1
                self._update_active_highlight()
            elif self.current_index > 0:
                self.current_index -= 1
                self._update_active_highlight()

    def calculate(self) -> None:
        if self.calculated:
            return

        cleaned: list[str] = []
        has_decimal = False
        for a in self.addends:
            s = a.strip()
            if s:
                if s.endswith("."):
                    s += "0"
                if "." in s:
                    has_decimal = True
                cleaned.append(s)

        if not cleaned:
            return

        try:
            if has_decimal:
                values = [Decimal(s) for s in cleaned]
            else:
                values = [int(s) for s in cleaned]
        except (InvalidOperation, ValueError):
            self.result_var.set("Error")
            return

        if has_decimal:
            # Decimal addition uses a working precision. Calculate enough digits
            # for both the largest whole-number place and the smallest fraction.
            highest_place = max(value.adjusted() for value in values)
            lowest_place = min(value.as_tuple().exponent for value in values)
            needed_precision = max(1, highest_place - lowest_place + 2)

            with localcontext() as ctx:
                ctx.prec = needed_precision
                total = sum(values, Decimal(0))

            # 'f' avoids scientific notation for very small decimal answers.
            formatted_result = format(total, "f")
            if "." in formatted_result:
                formatted_result = formatted_result.rstrip("0").rstrip(".")
            if Decimal(formatted_result) == 0:
                formatted_result = "0"
        else:
            total = sum(values)
            formatted_result = str(total)
        self.result_var.set(formatted_result)
        self.calculated = True
        self._update_entry_widths()
        self._update_active_highlight()
        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

        expr = " + ".join(str(v) for v in values)
        print(f"{expr} = {formatted_result}")

    def clear_all(self) -> None:
        while len(self.addend_frames) > 2:
            f = self.addend_frames.pop()
            f.destroy()
            self.addend_labels.pop()
            self.addend_entries.pop()
            self.addend_vars.pop()

        self.addends = ["", ""]
        self.addend_vars[0].set("")
        self.addend_vars[1].set("")
        self.result_var.set("")
        self.current_index = 0
        self.calculated = False
        self._update_entry_widths()
        self.root.geometry("")
        self.canvas.yview_moveto(0.0)
        self._update_active_highlight()


def main() -> None:
    root = tk.Tk()
    AdditionCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()

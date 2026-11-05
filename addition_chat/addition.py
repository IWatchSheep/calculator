from decimal import Decimal, InvalidOperation, localcontext
import re
import tkinter as tk
from tkinter import ttk
from typing import Dict, List, Optional, Set, Tuple


class WordSummerChatbot:
    """
    Offline rule-based NLP helper that sums up and synthesizes
    word descriptions corresponding to addends across multiple word columns.
    """

    CATEGORIES: Dict[str, Tuple[str, Set[str]]] = {
        "fruit": (
            "fruits",
            {
                "apple", "apples", "banana", "bananas", "orange", "oranges",
                "pear", "pears", "grape", "grapes", "strawberry", "strawberries",
                "blueberry", "blueberries", "peach", "peaches", "lemon", "lemons",
                "lime", "limes", "mango", "mangoes", "watermelon", "watermelons",
                "cherry", "cherries", "plum", "plums", "kiwi", "kiwis", "fruit", "fruits"
            }
        ),
        "vegetable": (
            "vegetables",
            {
                "carrot", "carrots", "potato", "potatoes", "tomato", "tomatoes",
                "onion", "onions", "pepper", "peppers", "broccoli", "cucumber",
                "cucumbers", "lettuce", "spinach", "garlic", "vegetable", "vegetables"
            }
        ),
        "animal": (
            "animals",
            {
                "dog", "dogs", "puppy", "puppies", "cat", "cats", "kitten", "kittens",
                "bird", "birds", "fish", "fishes", "horse", "horses", "cow", "cows",
                "pig", "pigs", "sheep", "rabbit", "rabbits", "animal", "animals", "pet", "pets"
            }
        ),
        "vehicle": (
            "vehicles",
            {
                "car", "cars", "truck", "trucks", "bus", "buses", "bike", "bikes",
                "bicycle", "bicycles", "motorcycle", "motorcycles", "train", "trains",
                "plane", "planes", "boat", "boats", "vehicle", "vehicles"
            }
        ),
        "clothing": (
            "items of clothing",
            {
                "shirt", "shirts", "pant", "pants", "shoe", "shoes", "sock", "socks",
                "hat", "hats", "jacket", "jackets", "coat", "coats", "dress", "dresses",
                "glove", "gloves", "clothing", "clothes"
            }
        ),
        "stationery": (
            "school/office items",
            {
                "pen", "pens", "pencil", "pencils", "book", "books", "notebook", "notebooks",
                "eraser", "erasers", "ruler", "rulers", "paper", "papers", "folder", "folders"
            }
        ),
        "currency": (
            "dollars",
            {
                "dollar", "dollars", "cent", "cents", "buck", "bucks", "dime", "dimes",
                "nickel", "nickels", "quarter", "quarters"
            }
        ),
        "time": (
            "time units",
            {
                "second", "seconds", "minute", "minutes", "hour", "hours",
                "day", "days", "week", "weeks", "month", "months", "year", "years"
            }
        ),
        "people": (
            "people",
            {
                "person", "people", "student", "students", "child", "children",
                "kid", "kids", "boy", "boys", "girl", "girls", "man", "men",
                "woman", "women", "member", "members", "worker", "workers"
            }
        ),
    }

    @classmethod
    def _lemmatize_word(cls, word: str) -> str:
        """Simple rule-based singularizer/lemmatizer for standard English nouns."""
        w = word.strip().lower()
        if w.endswith("ies") and len(w) > 4:
            return w[:-3] + "y"
        if w.endswith("es") and len(w) > 3 and (w.endswith("shes") or w.endswith("ches") or w.endswith("xes") or w.endswith("ses")):
            return w[:-2]
        if w.endswith("s") and not w.endswith("ss") and len(w) > 2:
            return w[:-1]
        return w

    @classmethod
    def _pluralize_word(cls, word: str, count_is_one: bool) -> str:
        w = word.strip()
        if not w:
            return ""
        if count_is_one:
            return cls._lemmatize_word(w)
        lem = cls._lemmatize_word(w)
        if lem == "child":
            return "children"
        if lem == "person":
            return "people"
        if lem == "man":
            return "men"
        if lem == "woman":
            return "women"
        if lem.endswith("y") and len(lem) > 1 and lem[-2] not in "aeiou":
            return lem[:-1] + "ies"
        if lem.endswith(("s", "sh", "ch", "x", "z")):
            return lem + "es"
        return lem + "s"

    @classmethod
    def _find_category(cls, token: str) -> Optional[Tuple[str, str]]:
        t = token.lower()
        lem = cls._lemmatize_word(t)
        for cat_name, (cat_label, members) in cls.CATEGORIES.items():
            if t in members or lem in members:
                return cat_name, cat_label
        return None

    @classmethod
    def summarize(cls, items: List[Tuple], total_formatted: str) -> str:
        """
        Summarizes a list of (number_string, word_string, [context_string, ...]) tuples
        into a cohesive word result.
        """
        cleaned_rows: List[Tuple[str, str, str, str]] = []
        for item in items:
            num = item[0] if len(item) > 0 else "0"
            num_clean = str(num).strip() or "0"
            word_parts: List[str] = []
            for part in item[1:]:
                p = str(part).strip()
                if p and not (p.startswith("(") and p.endswith("...)")):
                    word_parts.append(p)
            if word_parts:
                item_word = word_parts[0]
                context_str = " ".join(word_parts[1:]) if len(word_parts) > 1 else ""
                full_desc = f"{item_word} {context_str}".strip()
                cleaned_rows.append((num_clean, item_word, context_str, full_desc))

        if not cleaned_rows:
            return ""

        is_single_unit = (total_formatted == "1" or total_formatted == "1.0")

        # Extract primary word tokens (last word of item_word usually serves as noun head)
        tokens = []
        for _, item_w, _, _ in cleaned_rows:
            words = re.findall(r"[A-Za-z]+", item_w)
            tokens.append(words[-1] if words else item_w)

        lemmas = [cls._lemmatize_word(tok) for tok in tokens]
        all_same_item = (len(set(lemmas)) == 1)

        contexts = [ctx for _, _, ctx, _ in cleaned_rows]
        all_same_context = (len(set(contexts)) == 1)

        # Case 1: All descriptions refer to the same noun (e.g. "pens" and "pen")
        if all_same_item:
            base = lemmas[0]
            display_word = cls._pluralize_word(base, is_single_unit)
            if all_same_context:
                if contexts[0]:
                    return f"{display_word} {contexts[0]}"
                return display_word
            else:
                # Same noun, but different contexts (e.g. 2 in the drawer, 3 on the desk)
                breakdown = ", ".join(
                    f"{n} {ctx}" if ctx else f"{n} {display_word}"
                    for n, _, ctx, _ in cleaned_rows
                )
                return f"{display_word} ({breakdown})"

        # Case 2: Check if all items belong to a common recognized category (e.g. "fruits")
        categories = [cls._find_category(tok) for tok in tokens]
        if all(c is not None for c in categories):
            cat_keys = {c[0] for c in categories if c is not None}
            if len(cat_keys) == 1:
                cat_label = categories[0][1]
                breakdown = ", ".join(f"{n} {desc}" for n, _, _, desc in cleaned_rows)
                return f"{cat_label} ({breakdown})"

        # Case 3: Two distinct items
        if len(cleaned_rows) == 2:
            return f"{cleaned_rows[0][3]} and {cleaned_rows[1][3]}"

        # Case 4: Multiple distinct items (natural listing)
        breakdown = ", ".join(f"{n} {desc}" for n, _, _, desc in cleaned_rows)
        return f"total items ({breakdown})"


class AdditionCalculator:
    BASE_WIDTH: int = 16

    # Pre-made hard-coded starter words categorized and ready for use in Column 2 (Item)
    DEFAULT_WORDS: List[str] = [
        "(Type custom word...)",
        "apples", "bananas", "berries", "books", "cars", "cats", "cents",
        "chairs", "children", "cups", "days", "dogs", "dollars", "hours",
        "laptops", "minutes", "notebooks", "oranges", "pencils", "pens",
        "people", "phones", "pizzas", "sandwiches", "shirts", "shoes",
        "students", "tables", "tomatoes"
    ]

    # Pre-made hard-coded starter context/description phrases for Column 3 (Description/Context)
    DEFAULT_CONTEXTS: List[str] = [
        "(Type custom description...)",
        "at home", "at school", "at work", "in the basket",
        "in the box", "in the cabinet", "in the classroom", "in the drawer",
        "in the fridge", "in the garage", "in the garden", "in the kitchen",
        "in the library", "in the office", "in the park", "in the room",
        "on sale", "on the counter", "on the desk", "on the floor",
        "on the shelf", "on the table", "under the bed", "with friends"
    ]

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Addition Calculator with Word Chatbot")
        self.root.resizable(True, True)

        self.word_options: List[str] = list(self.DEFAULT_WORDS)
        self.context_options: List[str] = list(self.DEFAULT_CONTEXTS)

        self.addends: List[str] = ["", ""]
        self.addend_words: List[str] = ["", ""]
        self.addend_contexts: List[str] = ["", ""]
        self.extra_addend_words: List[List[str]] = []

        self.current_index: int = 0
        self.active_field: str = "number"  # "number" or "word"
        self.active_word_col: int = 0      # 0 for Item, 1 for Context, 2+ for extra columns
        self.calculated: bool = False

        self.addend_frames: List[tk.Frame] = []
        self.addend_labels: List[tk.Label] = []
        self.addend_entries: List[tk.Entry] = []
        self.addend_vars: List[tk.StringVar] = []

        self.addend_row_inner_frames: List[tk.Frame] = []

        self.addend_word_entries: List[ttk.Combobox] = []
        self.addend_word_vars: List[tk.StringVar] = []

        self.addend_context_entries: List[ttk.Combobox] = []
        self.addend_context_vars: List[tk.StringVar] = []

        self.extra_word_entries: List[List[ttk.Combobox]] = []
        self.extra_word_vars: List[List[tk.StringVar]] = []
        self.extra_header_labels: List[tk.Label] = []

        self._create_widgets()
        self._bind_keys()
        self._update_active_highlight()

        self.root.update_idletasks()
        self.root.minsize(750, self.root.winfo_reqheight())

    @staticmethod
    def _get_label_text(index: int) -> str:
        ordinals = [
            "First", "Second", "Third", "Fourth", "Fifth",
            "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"
        ]
        name = f"{ordinals[index]} Addend" if index < len(ordinals) else f"Addend {index + 1}"
        return name if index == 0 else f"{name} (+)"

    def _create_widgets(self) -> None:
        # Bottom-anchored control container holding numeric keypad and typewriter keyboard
        self.bottom_container = tk.Frame(self.root)
        self.bottom_container.pack(side="bottom", fill="x", padx=12, pady=(4, 12))

        # We keep self.keypad_frame so existing layout expectations remain intact
        self.keypad_frame = tk.Frame(self.bottom_container)
        self.keypad_frame.pack(side="left", padx=(0, 10), anchor="n")
        self._create_keypad()

        # Typewriter keyboard to the right of the numeric keypad
        self.typewriter_frame = tk.Frame(self.bottom_container)
        self.typewriter_frame.pack(side="left", fill="both", expand=True, anchor="n")
        self._create_typewriter()

        # Scrollable container nested above the bottom controls
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

        # Column headers
        self.header_frame = tk.Frame(self.displays_frame)
        self.header_frame.pack(side="top", fill="x", pady=(0, 4))
        self.header_num_lbl = tk.Label(
            self.header_frame,
            text="Number (Quantity)",
            font=("Segoe UI", 9, "bold"),
            fg="#444444",
            width=self.BASE_WIDTH + 2,
            anchor="w"
        )
        self.header_num_lbl.pack(side="left")

        self.header_word_lbl = tk.Label(
            self.header_frame,
            text="Item (Word)",
            font=("Segoe UI", 9, "bold"),
            fg="#444444",
            anchor="w"
        )
        self.header_word_lbl.pack(side="left", fill="x", expand=True, padx=(8, 0))

        self.header_context_lbl = tk.Label(
            self.header_frame,
            text="Description / Context",
            font=("Segoe UI", 9, "bold"),
            fg="#444444",
            anchor="w"
        )
        self.header_context_lbl.pack(side="left", fill="x", expand=True, padx=(8, 0))

        self.add_col_btn = tk.Button(
            self.header_frame,
            text="+ Column",
            font=("Segoe UI", 8, "bold"),
            bg="#e1f5fe",
            fg="#0277bd",
            relief="groove",
            command=self.add_column,
        )
        self.add_col_btn.pack(side="left", padx=(8, 0))

        # Initial two addend rows
        for i in range(2):
            self._create_addend_widget(i)

        # Result row (anchored at the bottom of displays_frame)
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

        result_row = tk.Frame(self.result_frame)
        result_row.pack(fill="x", expand=True)
        self._bind_mousewheel(result_row)

        self.result_var = tk.StringVar(value="")
        self.result_entry = tk.Entry(
            result_row,
            textvariable=self.result_var,
            font=("Consolas", 15, "bold"),
            justify="right",
            state="readonly",
            readonlybackground="#f4f9f4",
            fg="#1b5e20",
            bd=3,
            relief="sunken",
            width=self.BASE_WIDTH,
        )
        self.result_entry.pack(side="left", fill="x")
        self._bind_mousewheel(self.result_entry)

        self.result_word_var = tk.StringVar(value="")
        self.result_word_entry = tk.Entry(
            result_row,
            textvariable=self.result_word_var,
            font=("Segoe UI", 12, "bold"),
            justify="left",
            state="readonly",
            readonlybackground="#f4f9f4",
            fg="#1b5e20",
            bd=3,
            relief="sunken",
        )
        self.result_word_entry.pack(side="left", fill="x", expand=True, padx=(8, 0))
        self._bind_mousewheel(self.result_word_entry)

        # Fit displays initial height cleanly
        self.root.update_idletasks()
        self.canvas.configure(height=self.displays_frame.winfo_reqheight())

    def _bind_mousewheel(self, widget: tk.Widget) -> None:
        widget.bind("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event) -> None:
        if getattr(event, "delta", 0):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_displays_configure(self, _event) -> None:
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

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

        row_f = tk.Frame(f)
        row_f.pack(fill="x", expand=True)
        self._bind_mousewheel(row_f)

        # Column 1 — Quantity: Numerical value entered by user
        num_var = tk.StringVar(value=self.addends[index])
        num_entry = tk.Entry(
            row_f,
            textvariable=num_var,
            font=("Consolas", 15),
            justify="right",
            state="readonly",
            readonlybackground="#ffffff",
            bd=3,
            relief="sunken",
            width=self.BASE_WIDTH,
        )
        num_entry.pack(side="left", fill="x")
        num_entry.bind("<Button-1>", lambda _e, idx=index: self._set_active_index(idx, "number"))
        self._bind_mousewheel(num_entry)

        # Column 2 — Item: Drop-down list with custom-word capability
        word_var = tk.StringVar(value=self.addend_words[index])
        word_combo = ttk.Combobox(
            row_f,
            textvariable=word_var,
            values=self.word_options,
            font=("Segoe UI", 11),
        )
        word_combo.pack(side="left", fill="x", expand=True, padx=(8, 0))
        word_combo.bind("<Button-1>", lambda _e, idx=index: self._set_active_index(idx, "word", col=0))
        word_combo.bind("<FocusIn>", lambda _e, idx=index: self._set_active_index(idx, "word", col=0))
        word_combo.bind("<<ComboboxSelected>>", lambda _e, idx=index: self._on_combo_select(idx))
        word_combo.bind("<KeyRelease>", lambda _e, idx=index: self._sync_word_from_entry(idx))
        word_combo.bind("<FocusOut>", lambda _e, idx=index: self._on_word_focus_out(idx))
        self._bind_mousewheel(word_combo)

        save_btn = tk.Button(
            row_f,
            text="+ Add to List",
            font=("Segoe UI", 8, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32",
            relief="groove",
            command=lambda idx=index: self.save_custom_word(idx),
        )
        save_btn.pack(side="left", padx=(4, 0))
        self._bind_mousewheel(save_btn)

        # Column 3 — Description / Context: Drop-down list and free-text entry
        context_var = tk.StringVar(value=self.addend_contexts[index])
        context_combo = ttk.Combobox(
            row_f,
            textvariable=context_var,
            values=self.context_options,
            font=("Segoe UI", 11),
        )
        context_combo.pack(side="left", fill="x", expand=True, padx=(8, 0))
        context_combo.bind("<Button-1>", lambda _e, idx=index: self._set_active_index(idx, "word", col=1))
        context_combo.bind("<FocusIn>", lambda _e, idx=index: self._set_active_index(idx, "word", col=1))
        context_combo.bind("<<ComboboxSelected>>", lambda _e, idx=index: self._on_context_combo_select(idx))
        context_combo.bind("<KeyRelease>", lambda _e, idx=index: self._sync_context_from_entry(idx))
        context_combo.bind("<FocusOut>", lambda _e, idx=index: self._on_context_focus_out(idx))
        self._bind_mousewheel(context_combo)

        save_context_btn = tk.Button(
            row_f,
            text="+ Add to List",
            font=("Segoe UI", 8, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32",
            relief="groove",
            command=lambda idx=index: self.save_custom_context(idx),
        )
        save_context_btn.pack(side="left", padx=(4, 0))
        self._bind_mousewheel(save_context_btn)

        # Dynamic extra columns (Column 4, 5, etc.) if previously added
        for col_idx in range(len(self.extra_addend_words)):
            self._create_extra_column_widget_for_row(row_f, index, col_idx)

        self.addend_frames.append(f)
        self.addend_labels.append(lbl)
        self.addend_vars.append(num_var)
        self.addend_entries.append(num_entry)
        self.addend_word_vars.append(word_var)
        self.addend_word_entries.append(word_combo)
        self.addend_context_vars.append(context_var)
        self.addend_context_entries.append(context_combo)
        self.addend_row_inner_frames.append(row_f)

    def _create_extra_column_widget_for_row(self, row_f: tk.Frame, row_idx: int, col_idx: int) -> None:
        col_var = tk.StringVar(value=self.extra_addend_words[col_idx][row_idx])
        col_combo = ttk.Combobox(
            row_f,
            textvariable=col_var,
            values=self.context_options,
            font=("Segoe UI", 11),
        )
        col_combo.pack(side="left", fill="x", expand=True, padx=(8, 0))
        col_combo.bind("<Button-1>", lambda _e, r=row_idx, c=col_idx: self._set_active_index(r, "word", col=c + 2))
        col_combo.bind("<FocusIn>", lambda _e, r=row_idx, c=col_idx: self._set_active_index(r, "word", col=c + 2))
        col_combo.bind("<<ComboboxSelected>>", lambda _e, r=row_idx, c=col_idx: self._on_extra_combo_select(r, c))
        col_combo.bind("<KeyRelease>", lambda _e, r=row_idx, c=col_idx: self._sync_extra_from_entry(r, c))
        col_combo.bind("<FocusOut>", lambda _e, r=row_idx, c=col_idx: self._on_extra_focus_out(r, c))
        self._bind_mousewheel(col_combo)

        save_extra_btn = tk.Button(
            row_f,
            text="+ Add to List",
            font=("Segoe UI", 8, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32",
            relief="groove",
            command=lambda r=row_idx, c=col_idx: self.save_custom_extra(r, c),
        )
        save_extra_btn.pack(side="left", padx=(4, 0))
        self._bind_mousewheel(save_extra_btn)

        if row_idx >= len(self.extra_word_vars[col_idx]):
            self.extra_word_vars[col_idx].append(col_var)
            self.extra_word_entries[col_idx].append(col_combo)

    def add_column(self, col_title: Optional[str] = None) -> None:
        """Adds a new column to all rows dynamically."""
        col_idx = len(self.extra_addend_words)
        title = col_title or f"Column {col_idx + 4} (Extra)"

        self.extra_addend_words.append(["" for _ in range(len(self.addends))])
        self.extra_word_vars.append([])
        self.extra_word_entries.append([])

        # Repack + Column button after appending header
        self.add_col_btn.pack_forget()
        header_lbl = tk.Label(
            self.header_frame,
            text=title,
            font=("Segoe UI", 9, "bold"),
            fg="#444444",
            anchor="w",
        )
        header_lbl.pack(side="left", fill="x", expand=True, padx=(8, 0))
        self.extra_header_labels.append(header_lbl)
        self.add_col_btn.pack(side="left", padx=(8, 0))

        # Add widget to each row
        for row_idx, row_f in enumerate(self.addend_row_inner_frames):
            self._create_extra_column_widget_for_row(row_f, row_idx, col_idx)

        self.root.update_idletasks()

    def _on_combo_select(self, index: int) -> None:
        val = self.addend_word_vars[index].get()
        if val == "(Type custom word...)":
            self.addend_word_vars[index].set("")
            self.addend_words[index] = ""
            self.addend_word_entries[index].focus_set()
        else:
            self.addend_words[index] = val
        self._set_active_index(index, "word", col=0)

    def _on_context_combo_select(self, index: int) -> None:
        val = self.addend_context_vars[index].get()
        if val == "(Type custom description...)":
            self.addend_context_vars[index].set("")
            self.addend_contexts[index] = ""
            self.addend_context_entries[index].focus_set()
        else:
            self.addend_contexts[index] = val
        self._set_active_index(index, "word", col=1)

    def _on_extra_combo_select(self, row_idx: int, col_idx: int) -> None:
        val = self.extra_word_vars[col_idx][row_idx].get()
        if val == "(Type custom description...)":
            self.extra_word_vars[col_idx][row_idx].set("")
            self.extra_addend_words[col_idx][row_idx] = ""
            self.extra_word_entries[col_idx][row_idx].focus_set()
        else:
            self.extra_addend_words[col_idx][row_idx] = val
        self._set_active_index(row_idx, "word", col=col_idx + 2)

    def _sync_word_from_entry(self, index: int) -> None:
        if 0 <= index < len(self.addend_word_vars):
            self.addend_words[index] = self.addend_word_vars[index].get()

    def _sync_context_from_entry(self, index: int) -> None:
        if 0 <= index < len(self.addend_context_vars):
            self.addend_contexts[index] = self.addend_context_vars[index].get()

    def _sync_extra_from_entry(self, row_idx: int, col_idx: int) -> None:
        if 0 <= col_idx < len(self.extra_word_vars) and 0 <= row_idx < len(self.extra_word_vars[col_idx]):
            self.extra_addend_words[col_idx][row_idx] = self.extra_word_vars[col_idx][row_idx].get()

    def _on_word_focus_out(self, index: int) -> None:
        self._sync_word_from_entry(index)
        val = self.addend_words[index].strip()
        if val and val != "(Type custom word...)":
            self.add_word_to_options(val)

    def _on_context_focus_out(self, index: int) -> None:
        self._sync_context_from_entry(index)
        val = self.addend_contexts[index].strip()
        if val and val != "(Type custom description...)":
            self.add_context_to_options(val)

    def _on_extra_focus_out(self, row_idx: int, col_idx: int) -> None:
        self._sync_extra_from_entry(row_idx, col_idx)
        val = self.extra_addend_words[col_idx][row_idx].strip()
        if val and not (val.startswith("(") and val.endswith("...)")):
            self.add_context_to_options(val)

    def save_custom_word(self, index: Optional[int] = None) -> None:
        """Adds the word in the active row to the saved options list for future selection."""
        idx = self.current_index if index is None else index
        if 0 <= idx < len(self.addend_word_vars):
            self._sync_word_from_entry(idx)
            val = self.addend_words[idx].strip()
            if val and val != "(Type custom word...)":
                self.add_word_to_options(val)

    def save_custom_context(self, index: Optional[int] = None) -> None:
        """Adds the context description in the active row to the saved options list for future selection."""
        idx = self.current_index if index is None else index
        if 0 <= idx < len(self.addend_context_vars):
            self._sync_context_from_entry(idx)
            val = self.addend_contexts[idx].strip()
            if val and val != "(Type custom description...)":
                self.add_context_to_options(val)

    def save_custom_extra(self, row_idx: int, col_idx: int) -> None:
        self._sync_extra_from_entry(row_idx, col_idx)
        val = self.extra_addend_words[col_idx][row_idx].strip()
        if val and not (val.startswith("(") and val.endswith("...)")):
            self.add_context_to_options(val)

    def save_active_word_or_context(self) -> None:
        if self.active_word_col == 1:
            self.save_custom_context()
        elif self.active_word_col > 1:
            extra_idx = self.active_word_col - 2
            self.save_custom_extra(self.current_index, extra_idx)
        else:
            self.save_custom_word()

    def add_word_to_options(self, word: str) -> bool:
        """Adds a new word to the dropdown options if not already present."""
        w = word.strip()
        if not w or w == "(Type custom word...)":
            return False

        existing_lower = [opt.lower() for opt in self.word_options if opt != "(Type custom word...)"]
        if w.lower() not in existing_lower:
            base_options = [opt for opt in self.word_options if opt != "(Type custom word...)"]
            base_options.append(w)
            base_options.sort(key=str.lower)
            self.word_options = ["(Type custom word...)"] + base_options
            self._refresh_all_comboboxes()
            return True
        return False

    def add_context_to_options(self, context_str: str) -> bool:
        """Adds a new context phrase to the dropdown options if not already present."""
        c = context_str.strip()
        if not c or c == "(Type custom description...)":
            return False

        existing_lower = [opt.lower() for opt in self.context_options if opt != "(Type custom description...)"]
        if c.lower() not in existing_lower:
            base_options = [opt for opt in self.context_options if opt != "(Type custom description...)"]
            base_options.append(c)
            base_options.sort(key=str.lower)
            self.context_options = ["(Type custom description...)"] + base_options
            self._refresh_all_context_comboboxes()
            return True
        return False

    def _refresh_all_comboboxes(self) -> None:
        for combo in self.addend_word_entries:
            combo["values"] = self.word_options

    def _refresh_all_context_comboboxes(self) -> None:
        for combo in self.addend_context_entries:
            combo["values"] = self.context_options
        for col in self.extra_word_entries:
            for combo in col:
                combo["values"] = self.context_options

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
                font=("Consolas", 15, "bold"),
                width=4,
                height=2,
                bg=bg,
                fg=fg,
                activebackground="#cccccc",
                command=cmd,
            )
            if text == "0":
                btn.grid(row=r, column=c, columnspan=2, padx=3, pady=3, sticky="nsew")
            elif text == "=":
                btn.grid(row=r, column=c, rowspan=2, padx=3, pady=3, sticky="nsew")
            else:
                btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

    def _create_typewriter(self) -> None:
        """Creates the QWERTY typewriter layout to the right of the numeric keypad."""
        lbl = tk.Label(
            self.typewriter_frame,
            text="Typewriter (Words)",
            font=("Segoe UI", 9, "bold"),
            fg="#555555",
            anchor="w"
        )
        lbl.pack(fill="x", pady=(0, 2))

        keyboard_inner = tk.Frame(self.typewriter_frame)
        keyboard_inner.pack(fill="both", expand=True)

        rows = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"],
        ]

        for r_idx, row in enumerate(rows):
            r_frame = tk.Frame(keyboard_inner)
            r_frame.pack(side="top", pady=2)
            for char in row:
                btn = tk.Button(
                    r_frame,
                    text=char,
                    font=("Segoe UI", 10, "bold"),
                    width=3,
                    height=1,
                    bg="#f0f4f8",
                    activebackground="#d0e1f9",
                    command=lambda c=char: self.on_typewriter_char(c.lower()),
                )
                btn.pack(side="left", padx=2)

        # Bottom function row: Space, Backspace, Clear Word, Add to List
        func_frame = tk.Frame(keyboard_inner)
        func_frame.pack(side="top", pady=2)

        space_btn = tk.Button(
            func_frame,
            text="Space",
            font=("Segoe UI", 10, "bold"),
            width=10,
            height=1,
            bg="#e3edf7",
            command=lambda: self.on_typewriter_char(" "),
        )
        space_btn.pack(side="left", padx=2)

        bksp_btn = tk.Button(
            func_frame,
            text="⌫ Bksp",
            font=("Segoe UI", 10, "bold"),
            width=8,
            height=1,
            bg="#fce4ec",
            command=self.on_typewriter_backspace,
        )
        bksp_btn.pack(side="left", padx=2)

        clear_word_btn = tk.Button(
            func_frame,
            text="Clear",
            font=("Segoe UI", 10, "bold"),
            width=7,
            height=1,
            bg="#ffebee",
            command=self.on_typewriter_clear_word,
        )
        clear_word_btn.pack(side="left", padx=2)

        save_word_btn = tk.Button(
            func_frame,
            text="+ Save Word",
            font=("Segoe UI", 10, "bold"),
            width=11,
            height=1,
            bg="#e8f5e9",
            fg="#2e7d32",
            command=self.save_active_word_or_context,
        )
        save_word_btn.pack(side="left", padx=2)

    def on_typewriter_char(self, char: str) -> None:
        if self.calculated:
            self.clear_all()
        self.active_field = "word"
        if self.active_word_col == 0:
            cur = self.addend_words[self.current_index]
            self.addend_words[self.current_index] = cur + char
            self.addend_word_vars[self.current_index].set(self.addend_words[self.current_index])
        elif self.active_word_col == 1:
            cur = self.addend_contexts[self.current_index]
            self.addend_contexts[self.current_index] = cur + char
            self.addend_context_vars[self.current_index].set(self.addend_contexts[self.current_index])
        else:
            extra_idx = self.active_word_col - 2
            if extra_idx < len(self.extra_addend_words):
                cur = self.extra_addend_words[extra_idx][self.current_index]
                self.extra_addend_words[extra_idx][self.current_index] = cur + char
                self.extra_word_vars[extra_idx][self.current_index].set(self.extra_addend_words[extra_idx][self.current_index])
        self._update_active_highlight()

    def on_typewriter_backspace(self) -> None:
        if self.active_word_col == 0:
            cur = self.addend_words[self.current_index]
            if cur:
                self.addend_words[self.current_index] = cur[:-1]
                self.addend_word_vars[self.current_index].set(self.addend_words[self.current_index])
        elif self.active_word_col == 1:
            cur = self.addend_contexts[self.current_index]
            if cur:
                self.addend_contexts[self.current_index] = cur[:-1]
                self.addend_context_vars[self.current_index].set(self.addend_contexts[self.current_index])
        else:
            extra_idx = self.active_word_col - 2
            if extra_idx < len(self.extra_addend_words):
                cur = self.extra_addend_words[extra_idx][self.current_index]
                if cur:
                    self.extra_addend_words[extra_idx][self.current_index] = cur[:-1]
                    self.extra_word_vars[extra_idx][self.current_index].set(self.extra_addend_words[extra_idx][self.current_index])

    def on_typewriter_clear_word(self) -> None:
        if self.active_word_col == 0:
            self.addend_words[self.current_index] = ""
            self.addend_word_vars[self.current_index].set("")
        elif self.active_word_col == 1:
            self.addend_contexts[self.current_index] = ""
            self.addend_context_vars[self.current_index].set("")
        else:
            extra_idx = self.active_word_col - 2
            if extra_idx < len(self.extra_addend_words):
                self.extra_addend_words[extra_idx][self.current_index] = ""
                self.extra_word_vars[extra_idx][self.current_index].set("")

    def _bind_keys(self) -> None:
        # Numeric keys routed to calculator when focused on root
        for digit in "0123456789":
            self.root.bind(digit, lambda _e, d=digit: self._handle_key_input(d))
            self.root.bind(f"<KP_{digit}>", lambda _e, d=digit: self._handle_key_input(d))
        self.root.bind("+", lambda _e: self.handle_plus())
        self.root.bind("<KP_Add>", lambda _e: self.handle_plus())
        self.root.bind("<Return>", lambda _e: self.calculate())
        self.root.bind("<KP_Enter>", lambda _e: self.calculate())
        self.root.bind("=", lambda _e: self.calculate())
        self.root.bind("<Escape>", lambda _e: self.clear_all())
        self.root.bind(".", lambda _e: self._handle_key_input("."))
        self.root.bind("<KP_Decimal>", lambda _e: self._handle_key_input("."))

    def _handle_key_input(self, char: str) -> None:
        # If user is currently typing inside a word combobox/entry, don't hijack their typing
        focused = self.root.focus_get()
        all_combos = (
            self.addend_word_entries +
            self.addend_context_entries +
            [c for sub in self.extra_word_entries for c in sub]
        )
        if isinstance(focused, (tk.Entry, ttk.Combobox)) and focused in all_combos:
            return
        self.on_button_click(char)

    def _set_active_index(self, index: int, field: str = "number", col: int = 0) -> None:
        self.current_index = index
        self.active_field = field
        self.active_word_col = col
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
                if self.active_field == "number":
                    self.addend_entries[i].config(readonlybackground="#eef5fc")
                else:
                    self.addend_entries[i].config(readonlybackground="#ffffff")
            else:
                lbl.config(text=base_txt, font=("Segoe UI", 9), fg="#555555")
                self.addend_entries[i].config(readonlybackground="#ffffff")

    def add_addend_window(self) -> None:
        """Pops up another addend row below the rest, scrolling top addends up and keeping keypad in place."""
        self.addends.append("")
        self.addend_words.append("")
        self.addend_contexts.append("")
        for col_idx in range(len(self.extra_addend_words)):
            self.extra_addend_words[col_idx].append("")
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
            self.addend_words.pop()
            self.addend_contexts.pop()
            for col_idx in range(len(self.extra_addend_words)):
                self.extra_addend_words[col_idx].pop()
                if self.extra_word_vars[col_idx]:
                    self.extra_word_vars[col_idx].pop()
                if self.extra_word_entries[col_idx]:
                    w = self.extra_word_entries[col_idx].pop()
                    w.destroy()
            f = self.addend_frames.pop()
            f.destroy()
            self.addend_labels.pop()
            self.addend_entries.pop()
            self.addend_vars.pop()
            self.addend_word_entries.pop()
            self.addend_word_vars.pop()
            self.addend_context_entries.pop()
            self.addend_context_vars.pop()
            self.addend_row_inner_frames.pop()
            self._update_entry_widths()

    def _update_entry_widths(self) -> None:
        """Stretches display windows if large numbers are entered."""
        lengths = [len(v.get()) for v in self.addend_vars] + [len(self.result_var.get())]
        max_len = max(lengths + [self.BASE_WIDTH])
        target_width = max_len + 2
        for entry in self.addend_entries:
            entry.config(width=target_width)
        self.result_entry.config(width=target_width)
        self.header_num_lbl.config(width=target_width + 2)

    def on_button_click(self, char: str) -> None:
        self.active_field = "number"
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
            res_num = self.result_var.get()
            res_word = self.result_word_var.get()
            self.clear_all()
            self.addends[0] = res_num
            self.addend_vars[0].set(res_num)
            self.addend_words[0] = res_word
            self.addend_word_vars[0].set(res_word)
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

        # If already on the last addend and '+' is pressed again, automatically add another row
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

        if self.active_field == "word":
            self.on_typewriter_backspace()
            return

        cur = self.addends[self.current_index]
        if cur:
            self.addends[self.current_index] = cur[:-1]
            self.addend_vars[self.current_index].set(self.addends[self.current_index])
            self._update_entry_widths()
        else:
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

        # Synchronize any text inputs from the word comboboxes and save new words
        for idx in range(len(self.addend_words)):
            self.addend_words[idx] = self.addend_word_vars[idx].get()
            w = self.addend_words[idx].strip()
            if w and w != "(Type custom word...)":
                self.add_word_to_options(w)

        for idx in range(len(self.addend_contexts)):
            self.addend_contexts[idx] = self.addend_context_vars[idx].get()
            c = self.addend_contexts[idx].strip()
            if c and c != "(Type custom description...)":
                self.add_context_to_options(c)

        for col_idx in range(len(self.extra_addend_words)):
            for row_idx in range(len(self.extra_addend_words[col_idx])):
                val = self.extra_word_vars[col_idx][row_idx].get()
                self.extra_addend_words[col_idx][row_idx] = val
                v_clean = val.strip()
                if v_clean and not (v_clean.startswith("(") and v_clean.endswith("...)")):
                    self.add_context_to_options(v_clean)

        cleaned: List[str] = []
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
            self.result_word_var.set("")
            return

        if has_decimal:
            highest_place = max(value.adjusted() for value in values)
            lowest_place = min(int(value.as_tuple().exponent) for value in values)
            needed_precision = max(1, highest_place - lowest_place + len(values) + 1)

            with localcontext() as context:
                context.prec = needed_precision
                total = sum(values, Decimal(0))

            formatted_result = format(total, "f")
            if "." in formatted_result:
                formatted_result = formatted_result.rstrip("0").rstrip(".")
        else:
            formatted_result = str(sum(values))

        self.result_var.set(formatted_result)

        # Chatbot calculation for the word result column across all word columns
        items = []
        for i in range(len(self.addends)):
            num = self.addends[i]
            w = self.addend_words[i]
            c = self.addend_contexts[i]
            extras = [self.extra_addend_words[col][i] for col in range(len(self.extra_addend_words))]
            items.append((num, w, c, *extras))

        word_result = WordSummerChatbot.summarize(items, formatted_result)
        self.result_word_var.set(word_result)

        self.calculated = True
        self._update_entry_widths()
        self._update_active_highlight()
        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

        expr = " + ".join(str(v) for v in values)
        print(f"{expr} = {formatted_result} ({word_result})")

    def clear_all(self) -> None:
        while len(self.addend_frames) > 2:
            f = self.addend_frames.pop()
            f.destroy()
            self.addend_labels.pop()
            self.addend_entries.pop()
            self.addend_vars.pop()
            self.addend_word_entries.pop()
            self.addend_word_vars.pop()
            self.addend_context_entries.pop()
            self.addend_context_vars.pop()
            self.addend_row_inner_frames.pop()
            for col_idx in range(len(self.extra_addend_words)):
                if len(self.extra_addend_words[col_idx]) > 2:
                    self.extra_addend_words[col_idx].pop()
                if len(self.extra_word_vars[col_idx]) > 2:
                    self.extra_word_vars[col_idx].pop()
                if len(self.extra_word_entries[col_idx]) > 2:
                    self.extra_word_entries[col_idx].pop().destroy()

        self.addends = ["", ""]
        self.addend_words = ["", ""]
        self.addend_contexts = ["", ""]
        self.addend_vars[0].set("")
        self.addend_vars[1].set("")
        self.addend_word_vars[0].set("")
        self.addend_word_vars[1].set("")
        self.addend_context_vars[0].set("")
        self.addend_context_vars[1].set("")
        for col_idx in range(len(self.extra_addend_words)):
            self.extra_addend_words[col_idx] = ["", ""]
            if len(self.extra_word_vars[col_idx]) >= 2:
                self.extra_word_vars[col_idx][0].set("")
                self.extra_word_vars[col_idx][1].set("")

        self.result_var.set("")
        self.result_word_var.set("")
        self.current_index = 0
        self.active_field = "number"
        self.active_word_col = 0
        self.calculated = False
        self._update_entry_widths()
        self.canvas.yview_moveto(0.0)
        self._update_active_highlight()


def main() -> None:
    root = tk.Tk()
    AdditionCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()

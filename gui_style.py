"""Colours, arrow layout and the do-nothing button helper shared by main.py and operator_row_math."""
import tkinter as tk

CREAM = "#fffbe6"
BLUE = "#1e6fd9"
GREEN = "#3cb043"
RED = "#e02020"
PURPLE = "#8a1fb0"
ORANGE = "#f07030"
PALE_BLUE = "#d6e6fa"
PALE_ORANGE = "#fbe4cf"
ARROW_BG = "#eaeaea"

ARROWS = [["↖", "↑", "↗"], ["←", None, "→"], ["↙", "↓", "↘"]]


def btn(parent, text, bg, fg="white", **kw):
    """Colored flat button that does nothing yet."""
    opts = dict(text=text, bg=bg, fg=fg, relief="raised", bd=1,
                font=("Segoe UI", 8, "bold"), activebackground=bg, command=lambda: None)
    opts.update(kw)
    return tk.Button(parent, **opts)

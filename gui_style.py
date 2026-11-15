"""Colours, arrow layout and the do-nothing button helper shared by main.py and operator_row_math."""
import tkinter as tk

from gui_coordinates import (  # noqa: F401
    ARROW_CENTER_POSITION,
    ARROW_GRID_POSITIONS,
    CARD_ARROW_GRID_POSITION,
    CARD_COMPONENT_POSITIONS,
    CARD_CONTEXT_POSITION,
    CARD_LABEL_POSITION,
    CARD_LEAD_BUTTON_POSITION,
    CARD_TRAILING_BUTTON_POSITION,
    GridPosition,
    LayoutRegion,
    arrow_at_position,
    card_component_position,
)

CREAM = "#fffbe6"
BLUE = "#1e6fd9"
GREEN = "#3cb043"
RED = "#e02020"
PURPLE = "#8a1fb0"
ORANGE = "#f07030"
PALE_BLUE = "#d6e6fa"
PALE_ORANGE = "#fbe4cf"
ARROW_BG = "#eaeaea"

ARROWS = [
    [arrow_at_position(r, c) for c in range(1, 4)]
    for r in range(1, 4)
]


def btn(parent, text, bg, fg="white", **kw):
    """Colored flat button that does nothing yet."""
    opts = dict(text=text, bg=bg, fg=fg, relief="raised", bd=1,
                font=("Segoe UI", 8, "bold"), activebackground=bg, command=lambda: None)
    opts.update(kw)
    return tk.Button(parent, **opts)

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
    MAIN_ROW_COLUMNS,
    ROW_1_ACTIONS_POS,
    ROW_1_JOIN_NOTE_POS,
    ROW_1_LABEL_POS,
    ROW_1_MATH_POS,
    ROW_1_RESULT_POS,
    ROW_2_ACTIONS_POS,
    ROW_2_HELPER_POS,
    ROW_2_LABEL_POS,
    ROW_2_MATH_POS,
    ROW_2_RESULT_POS,
    ROW_1_ROW_LABEL_POS,
    ROW_1_HELPER_SLOT_POS,
    ROW_1_MATH_EXPRESSION_POS,
    ROW_1_MATH_ACTIONS_POS,
    ROW_1_RESULT_CARD_POS,
    ROW_2_ROW_LABEL_POS,
    ROW_2_HELPER_SLOT_POS,
    ROW_2_MATH_EXPRESSION_POS,
    ROW_2_MATH_ACTIONS_POS,
    ROW_2_RESULT_CARD_POS,
    ROW_COL_ACTIONS,
    ROW_COL_HELPER,
    ROW_COL_LABEL,
    ROW_COL_MATH,
    ROW_COL_RESULT,
    arrow_at_position,
    card_component_position,
    main_row_position,
    main_row_positions,
    EXCEL_TOTAL_COLUMNS,
    EXCEL_INITIAL_TOTAL_ROWS,
    EXCEL_ROWS_PER_CALCULATOR_ROW,
    EXCEL_CALCULATOR_ROW_STRIDE,
    excel_start_row,
    excel_heading_row,
    excel_workspace_position,
    excel_workspace_positions,
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

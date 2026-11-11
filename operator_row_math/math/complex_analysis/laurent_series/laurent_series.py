"""Row for the operator: Laurent series

Picture:      Σ □ ₙ ( □ − □ ) ⁿ
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py math/complex_analysis/laurent_series
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Laurent series'
KEY = 'math/complex_analysis/laurent_series'
PATTERN = 'Σ □ ₙ ( □ − □ ) ⁿ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. Needs the function and the centre. The series is not one number.'    # formula only: what the row says (no box is added and compute() is unchanged)
LEVELS = [0, 0, 1, 0, 0, 0, 0, 0, -1]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'Σ'), ('dec', ''), ('op', 'n'), ('op', '('), ('dec', ''), ('op', '−'), ('dec', ''), ('op', ')'), ('op', 'n')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

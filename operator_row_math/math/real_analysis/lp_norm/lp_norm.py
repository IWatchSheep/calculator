"""Row for the operator: Lp norm

Picture:      ‖ □ ‖ ₚ = ( ∫ | □ | ᵖ □ □ ) ^ ( 1 / □ ) with □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/real_analysis/lp_norm
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Lp norm'
KEY = 'math/real_analysis/lp_norm'
PATTERN = '‖ □ ‖ ₚ = ( ∫ | □ | ᵖ □ □ ) ^ ( 1 / □ ) with □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'a', 'b']    # what each box (left to right) is
KINDS = ['function', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 0, 1, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '‖'), ('box', ''), ('op', '‖'), ('op', 'p'), ('op', '='), ('op', '('), ('op', '∫'), ('op', '|'), ('box', ''), ('op', '|'), ('op', 'p'), ('dec', ''), ('dec', ''), ('op', ')'), ('op', '^'), ('op', '('), ('op', '1'), ('op', '/'), ('dec', ''), ('op', ')'), ('op', 'with'), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))

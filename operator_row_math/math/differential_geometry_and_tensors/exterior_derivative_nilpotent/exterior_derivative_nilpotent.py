"""Row for the operator: Exterior derivative: d squared is zero

Picture:      d ² = 0
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py math/differential_geometry_and_tensors/exterior_derivative_nilpotent
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Exterior derivative: d squared is zero'
KEY = 'math/differential_geometry_and_tensors/exterior_derivative_nilpotent'
PATTERN = 'd ² = 0'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. d² = 0 is the whole statement.'    # formula only: what the row says (no box is added and compute() is unchanged)
LEVELS = [0, -1, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('exterior derivative', 'apply d twice'), 1: ('two', 'the second application'), 3: ('zero', 'd of d is always the zero form')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
STACK_EXPONENTS = True    # an exponent card shares the column of the symbol it powers (one grid row up) instead of having a column of its own
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'd'), ('op', '2'), ('op', '='), ('op', '0')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"), stack_exponents=True)

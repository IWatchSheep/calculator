"""Row for the operator: Z-transform

Picture:      □ ( □ ) = Σ ₙ □ [ □ ] · □ ⁻ⁿ
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/transforms_and_differential_equations/z_transform
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Z-transform'
KEY = 'math/transforms_and_differential_equations/z_transform'
PATTERN = '□ ( □ ) = Σ ₙ □ [ □ ] · □ ⁻ⁿ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['x', 'z']    # what each box (left to right) is
KINDS = ['list', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('the transform', 'X of z'), 2: ('the variable', 'z, a complex number'), 6: ('time index', 'n'), 7: ('the sequence', 'x of n'), 9: ('the index', 'n'), 12: ('the variable', 'z'), 13: ('the power', 'minus n, one over z to the n')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '('), ('box', ''), ('op', ')'), ('op', '='), ('op', 'Σ'), ('op', 'n'), ('box', ''), ('op', '['), ('dec', ''), ('op', ']'), ('op', '·'), ('box', ''), ('op', '−n')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

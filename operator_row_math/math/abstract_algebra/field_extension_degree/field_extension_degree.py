"""Row for the operator: Field extension: degree

Picture:      [ K : F ] = dim F K
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py math/abstract_algebra/field_extension_degree
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Field extension: degree'
KEY = 'math/abstract_algebra/field_extension_degree'
PATTERN = '[ K : F ] = dim F K'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. The degree is the dimension of K over F. No missing number.'    # formula only: what the row says (no box is added and compute() is unchanged)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 1, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {1: ('bigger field', 'the field that contains F'), 3: ('smaller field', 'the field inside K'), 6: ('dimension', 'how many vectors are in a basis'), 7: ('smaller field', 'the dimension is counted over F'), 8: ('bigger field', 'the vector space whose dimension is taken')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '['), ('op', 'K'), ('op', ':'), ('op', 'F'), ('op', ']'), ('op', '='), ('op', 'dim'), ('op', 'F'), ('op', 'K')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

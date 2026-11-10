"""Row for the operator: Direct sum: dimension

Picture:      dim ( A ⊕ B ) = dim A + dim B
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py math/abstract_algebra/direct_sum_dimension
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Direct sum: dimension'
KEY = 'math/abstract_algebra/direct_sum_dimension'
PATTERN = 'dim ( A ⊕ B ) = dim A + dim B'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('dimension', 'the number of vectors in a basis'), 2: ('first space', 'a vector space'), 4: ('second space', 'a vector space'), 7: ('dimension', 'the number of vectors in a basis'), 8: ('first space', 'a vector space'), 10: ('dimension', 'the number of vectors in a basis'), 11: ('second space', 'a vector space')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'dim'), ('op', '('), ('op', 'A'), ('op', '⊕'), ('op', 'B'), ('op', ')'), ('op', '='), ('op', 'dim'), ('op', 'A'), ('op', '+'), ('op', 'dim'), ('op', 'B')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

"""Row for the operator: Exponential distribution

Picture:      f ( □ ) = □ · e ^ ( − □ □ ) for □ ≥ 0
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/statistics_and_probability/exponential_distribution
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Exponential distribution'
KEY = 'math/statistics_and_probability/exponential_distribution'
PATTERN = 'f ( □ ) = □ · e ^ ( − □ □ ) for □ ≥ 0'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['x', 'lam']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 1, 0, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {2: ('value', 'zero or greater'), 5: ('rate', 'how many events per unit of time'), 11: ('rate', 'how many events per unit of time'), 12: ('value', 'zero or greater'), 15: ('value', 'zero or greater')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', '='), ('box', ''), ('op', '·'), ('op', 'e'), ('op', '^'), ('op', '('), ('op', '−'), ('box', ''), ('box', ''), ('op', ')'), ('op', 'for'), ('box', ''), ('op', '≥'), ('op', '0')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

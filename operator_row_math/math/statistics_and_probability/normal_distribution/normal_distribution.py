"""Row for the operator: Normal distribution

Picture:      f ( □ ) = e ^ ( − ( □ − □ ) ² / 2 □ ² ) / ( □ √ ( 2 π ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/statistics_and_probability/normal_distribution
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Normal distribution'
KEY = 'math/statistics_and_probability/normal_distribution'
PATTERN = 'f ( □ ) = e ^ ( − ( □ − □ ) ² / 2 □ ² ) / ( □ √ ( 2 π ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['x']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {2: ('value', 'where you read the curve'), 10: ('value', 'where you read the curve')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n'], [1, 'n']], [[2, 'n'], [1, 'n']], [[2, 'n'], [1, 'n']], [[2, 'n'], [1, 'n']], [[2, 'n'], [1, 'n']], [[2, 'n'], [1, 'n']], [[2, 'n'], [1, 'bar']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n']], [[2, 'bar']], [[2, 'hide']], [[2, 'd']], [[2, 'd']], [[2, 'd']], [[2, 'd']], [[2, 'd']], [[2, 'd']], [[2, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', '='), ('op', 'e'), ('op', '^'), ('op', '('), ('op', '−'), ('op', '('), ('box', ''), ('op', '−'), ('dec', ''), ('op', ')'), ('op', '2'), ('op', '/'), ('op', '2'), ('dec', ''), ('op', '2'), ('op', ')'), ('op', '/'), ('op', '('), ('dec', ''), ('op', '√'), ('op', '('), ('op', '2'), ('op', 'π'), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

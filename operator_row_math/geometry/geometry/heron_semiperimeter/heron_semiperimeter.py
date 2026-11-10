"""Row for the operator: Heron's formula: semi-perimeter

Picture:      □ = ( □ + □ + □ ) / 2
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py geometry/geometry/heron_semiperimeter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Heron's formula: semi-perimeter"
KEY = 'geometry/geometry/heron_semiperimeter'
PATTERN = '□ = ( □ + □ + □ ) / 2'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['a', 'b', 'c']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('semi-perimeter', 'half of a plus b plus c, metres'), 3: ('side a', 'metres'), 5: ('side b', 'metres'), 7: ('side c', 'metres')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'hide']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'hide']], [[1, 'bar']], [[1, 'd']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('box', ''), ('op', '+'), ('box', ''), ('op', '+'), ('box', ''), ('op', ')'), ('op', '/'), ('op', '2')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

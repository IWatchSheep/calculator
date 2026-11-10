"""Row for the operator: Weight

Picture:      □ = ( 1 + cos ( □ ) ) / 2
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/spin_up_at_angle
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Spin up at an angle'
KEY = 'physics/physics/spin_up_at_angle'
PATTERN = '□ = ( 1 + cos ( □ ) ) / 2'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['theta']
KINDS = ['number']
WORDS = {0: ('probability', '0 to 1, spin up along the measurement axis'), 7: ('angle', 'radians from z to the measurement axis')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'hide']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'hide']], [[1, 'bar']], [[1, 'd']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('op', '1'), ('op', '+'), ('op', 'cos'), ('op', '('), ('box', ''), ('op', ')'), ('op', ')'), ('op', '/'), ('op', '2')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

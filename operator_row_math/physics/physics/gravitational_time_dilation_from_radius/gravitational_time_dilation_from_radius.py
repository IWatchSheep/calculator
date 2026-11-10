"""Row for the operator: Gravitational time dilation: from the horizon

Picture:      □ = □ × √ ( 1 − □ / □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/gravitational_time_dilation_from_radius
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Gravitational time dilation: from the horizon'
KEY = 'physics/physics/gravitational_time_dilation_from_radius'
PATTERN = '□ = □ × √ ( 1 − □ / □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['dt', 'rs', 'r']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('clock time', 'seconds on the clock near the mass'), 2: ('far-away time', 'seconds measured far from the mass'), 8: ('horizon radius', 'the answer of the row above, metres'), 10: ('distance', 'metres from the centre, outside the horizon')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [], [], [], [], [[1, 'n']], [[1, 'bar']], [[1, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '×'), ('op', '√'), ('op', '('), ('op', '1'), ('op', '−'), ('box', ''), ('op', '/'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

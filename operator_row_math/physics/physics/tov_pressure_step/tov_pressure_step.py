"""Row for the operator: Weight

Picture:      □ = − □ × ( G □ □ ( 1 + □ / ( □ c ² ) ) ( 1 + 4 π □ ³ □ / ( □ c ² ) ) ) / ( □ ² ( 1 − 2 G □ / ( □ c ² ) ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/tov_pressure_step
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'TOV pressure step'
KEY = 'physics/physics/tov_pressure_step'
PATTERN = '□ = − □ × ( G □ □ ( 1 + □ / ( □ c ² ) ) ( 1 + 4 π □ ³ □ / ( □ c ² ) ) ) / ( □ ² ( 1 − 2 G □ / ( □ c ² ) ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['r', 'dr', 'M', 'rho', 'P']
KINDS = ['number', 'number', 'number', 'number', 'number']
SLOTS = [1, 2, 3, 4, 3, 0, 4, 2, 0, 2, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('pressure change', 'pascals, outward across the shell'), 3: ('shell thickness', 'metres, outward'), 6: ('gravitational constant', '6.674e-11 N m2/kg2'), 7: ('interior mass', 'kilograms already inside r'), 8: ('density', 'kilograms per cubic metre'), 12: ('pressure', 'pascals at r'), 16: ('speed of light', '299792458 m/s'), 25: ('radius', 'metres from the centre')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n'], [1, 'n']], [[3, 'n'], [1, 'bar']], [[3, 'n'], [1, 'hide']], [[3, 'n'], [1, 'd']], [[3, 'n'], [1, 'd']], [[3, 'n'], [1, 'd']], [[3, 'n'], [1, 'hide']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n'], [2, 'n']], [[3, 'n'], [2, 'n']], [[3, 'n'], [2, 'n']], [[3, 'n'], [2, 'n']], [[3, 'n'], [2, 'n']], [[3, 'n'], [2, 'bar']], [[3, 'n'], [2, 'hide']], [[3, 'n'], [2, 'd']], [[3, 'n'], [2, 'd']], [[3, 'n'], [2, 'd']], [[3, 'n'], [2, 'hide']], [[3, 'n']], [[3, 'n']], [[3, 'bar']], [[3, 'hide']], [[3, 'd']], [[3, 'd']], [[3, 'd']], [[3, 'd']], [[3, 'd']], [[3, 'd'], [4, 'n']], [[3, 'd'], [4, 'n']], [[3, 'd'], [4, 'n']], [[3, 'd'], [4, 'bar']], [[3, 'd'], [4, 'hide']], [[3, 'd'], [4, 'd']], [[3, 'd'], [4, 'd']], [[3, 'd'], [4, 'd']], [[3, 'd'], [4, 'hide']], [[3, 'd']], [[3, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '−'), ('box', ''), ('op', '×'), ('op', '('), ('op', 'G'), ('box', ''), ('box', ''), ('op', '('), ('op', '1'), ('op', '+'), ('box', ''), ('op', '/'), ('op', '('), ('box', ''), ('op', 'c'), ('op', '2'), ('op', ')'), ('op', ')'), ('op', '('), ('op', '1'), ('op', '+'), ('op', '4'), ('op', 'π'), ('box', ''), ('op', '3'), ('box', ''), ('op', '/'), ('op', '('), ('box', ''), ('op', 'c'), ('op', '2'), ('op', ')'), ('op', ')'), ('op', ')'), ('op', '/'), ('op', '('), ('box', ''), ('op', '2'), ('op', '('), ('op', '1'), ('op', '−'), ('op', '2'), ('op', 'G'), ('box', ''), ('op', '/'), ('op', '('), ('box', ''), ('op', 'c'), ('op', '2'), ('op', ')'), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

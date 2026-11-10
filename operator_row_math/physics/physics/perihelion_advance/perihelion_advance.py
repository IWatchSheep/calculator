"""Row for the operator: Weight

Picture:      □ = 3 π □ / ( □ ( 1 − □ ² ) ) × 36525 / □ × 648000 / π
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/perihelion_advance
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Perihelion advance'
KEY = 'physics/physics/perihelion_advance'
PATTERN = '□ = 3 π □ / ( □ ( 1 − □ ² ) ) × 36525 / □ × 648000 / π'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['a', 'eccentricity', 'period_days', 'Rs']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [3, 0, 1, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('advance', 'arcseconds per century, the general-relativity part only'), 4: ('Schwarzschild radius', 'metres, 2GM/c2 of the central mass'), 7: ('semi-major axis', 'metres'), 11: ('eccentricity', '0 is a circle, must be below 1'), 18: ('orbital period', 'days')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[2, 'n'], [1, 'hide']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'd']], [[2, 'n'], [1, 'hide']], [[2, 'n']], [[2, 'n']], [[2, 'bar']], [[2, 'd'], [3, 'n']], [[2, 'd'], [3, 'n']], [[2, 'd'], [3, 'n']], [[3, 'bar']], [[3, 'd']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '3'), ('op', 'π'), ('box', ''), ('op', '/'), ('op', '('), ('box', ''), ('op', '('), ('op', '1'), ('op', '−'), ('box', ''), ('op', '2'), ('op', ')'), ('op', ')'), ('op', '×'), ('op', '36525'), ('op', '/'), ('box', ''), ('op', '×'), ('op', '648000'), ('op', '/'), ('op', 'π')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

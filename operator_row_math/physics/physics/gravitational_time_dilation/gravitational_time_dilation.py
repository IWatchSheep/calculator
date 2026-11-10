"""Row for the operator: Gravitational time dilation

Picture:      □ = □ × √ ( 1 − 2 × G × □ / ( □ × c ² ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/gravitational_time_dilation
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Gravitational time dilation'
KEY = 'physics/physics/gravitational_time_dilation'
PATTERN = '□ = □ × √ ( 1 − 2 × G × □ / ( □ × c ² ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['dt', 'M', 'r']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('clock time', 'seconds on the clock near the mass'), 2: ('far-away time', 'seconds measured far from the mass'), 10: ('gravitational constant', '6.674e-11 N m2/kg2'), 12: ('mass', 'kilograms'), 15: ('distance', 'metres from the centre, outside the horizon'), 17: ('speed of light', '299792458 m/s')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [], [], [], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'hide']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '×'), ('op', '√'), ('op', '('), ('op', '1'), ('op', '−'), ('op', '2'), ('op', '×'), ('op', 'G'), ('op', '×'), ('box', ''), ('op', '/'), ('op', '('), ('box', ''), ('op', '×'), ('op', 'c'), ('op', '2'), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

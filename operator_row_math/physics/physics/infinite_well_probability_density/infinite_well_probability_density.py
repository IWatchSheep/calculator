"""Row for the operator: Weight

Picture:      □ = 2 / □ × sin ² ( □ π □ / □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/infinite_well_probability_density
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Infinite-well probability density'
KEY = 'physics/physics/infinite_well_probability_density'
PATTERN = '□ = 2 / □ × sin ² ( □ π □ / □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n','L','x']
KINDS = ['number', 'number', 'number']
SLOTS = [1, 0, 2, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('probability density', 'per metre'), 4: ('box width', 'metres'), 9: ('level', '1, 2, 3, …'), 11: ('position', 'metres from the left wall')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [], [], [], [], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'bar']], [[2, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '2'), ('op', '/'), ('box', ''), ('op', '×'), ('op', 'sin'), ('op', '2'), ('op', '('), ('box', ''), ('op', 'π'), ('box', ''), ('op', '/'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

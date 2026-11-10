"""Row for the operator: Weight

Picture:      □ = 6371000 · 2 atan2 ( √ a , √ ( 1 − a ) ) with a = sin ² ( ( □ − □ ) / 2 ) + cos □ cos □ sin ² ( ( □ − □ ) / 2 )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/haversine_distance
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Haversine distance'
KEY = 'physics/physics/haversine_distance'
PATTERN = '□ = 6371000 · 2 atan2 ( √ a , √ ( 1 − a ) ) with a = sin ² ( ( □ − □ ) / 2 ) + cos □ cos □ sin ² ( ( □ − □ ) / 2 )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['lat1', 'lon1', 'lat2', 'lon2']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [2, 0, 0, 2, 3, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('distance', 'metres along the surface'), 24: ('second latitude', 'radians, north is positive'), 26: ('first latitude', 'radians, north is positive'), 40: ('second longitude', 'radians, east is positive'), 42: ('first longitude', 'radians, east is positive')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [[1, 'hide']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'hide']], [[1, 'bar']], [[1, 'd']], [], [], [], [], [], [], [], [], [], [[2, 'hide']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'hide']], [[2, 'bar']], [[2, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '6371000'), ('op', '·'), ('op', '2'), ('op', 'atan2'), ('op', '('), ('op', '√'), ('op', 'a'), ('op', ','), ('op', '√'), ('op', '('), ('op', '1'), ('op', '−'), ('op', 'a'), ('op', ')'), ('op', ')'), ('op', 'with'), ('op', 'a'), ('op', '='), ('op', 'sin'), ('op', '2'), ('op', '('), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', '/'), ('op', '2'), ('op', ')'), ('op', '+'), ('op', 'cos'), ('box', ''), ('op', 'cos'), ('box', ''), ('op', 'sin'), ('op', '2'), ('op', '('), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', '/'), ('op', '2'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

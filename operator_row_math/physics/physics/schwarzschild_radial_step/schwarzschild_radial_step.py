"""Row for the operator: Weight

Picture:      □ = □ + □ □ + ½ ( − □ c ² / ( 2 □ ² ) ) □ ²
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/schwarzschild_radial_step
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Schwarzschild radial step'
KEY = 'physics/physics/schwarzschild_radial_step'
PATTERN = '□ = □ + □ □ + ½ ( − □ c ² / ( 2 □ ² ) ) □ ²'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['r', 'v', 'dt', 'Rs']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 2, 3, 0, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('next radius', 'metres from the centre after one step'), 2: ('radius', 'metres from the centre, outside the horizon'), 4: ('radial speed', 'metres per second of proper time, negative falls inward'), 5: ('proper time step', 'seconds'), 10: ('Schwarzschild radius', 'metres, 2GM/c2'), 11: ('speed of light', '299792458 m/s')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [], [], [], [], [], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'hide']], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '+'), ('box', ''), ('box', ''), ('op', '+'), ('op', '½'), ('op', '('), ('op', '−'), ('box', ''), ('op', 'c'), ('op', '2'), ('op', '/'), ('op', '('), ('op', '2'), ('box', ''), ('op', '2'), ('op', ')'), ('op', ')'), ('box', ''), ('op', '2')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

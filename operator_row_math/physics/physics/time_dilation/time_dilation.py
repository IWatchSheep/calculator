"""Row for the operator: Time dilation

Picture:      □ = □ / √ ( 1 − □ ² / c ² )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/time_dilation
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Time dilation'
KEY = 'physics/physics/time_dilation'
PATTERN = '□ = □ / √ ( 1 − □ ² / c ² )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['dt0', 'v']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('elapsed time', 'seconds for the stay-at-home clock; negligible below about 1 percent of the speed of light'), 2: ('proper time', 'seconds on the moving clock'), 8: ('speed', 'metres per second'), 11: ('speed of light', '299792458 m/s')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'd'], [2, 'n']], [[1, 'd'], [2, 'n']], [[1, 'd'], [2, 'bar']], [[1, 'd'], [2, 'd']], [[1, 'd'], [2, 'd']], [[1, 'd']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '/'), ('op', '√'), ('op', '('), ('op', '1'), ('op', '−'), ('box', ''), ('op', '2'), ('op', '/'), ('op', 'c'), ('op', '2'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

"""Row for the operator: Weight

Picture:      □ = | □ | / ( − ( □ · □ ) / | □ | )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/time_to_collision
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Time to collision'
KEY = 'physics/physics/time_to_collision'
PATTERN = '□ = | □ | / ( − ( □ · □ ) / | □ | )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['position', 'velocity']    # what each box (left to right) is
KINDS = ['list', 'list']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 0, 1, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('time', 'seconds until it reaches the obstacle'), 3: ('obstacle from the robot', 'x, y, z in metres'), 11: ('robot velocity', 'metres per second, x, y, z')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd'], [2, 'hide']], [[1, 'd'], [2, 'n']], [[1, 'd'], [2, 'n']], [[1, 'd'], [2, 'n']], [[1, 'd'], [2, 'hide']], [[1, 'd'], [2, 'bar']], [[1, 'd'], [2, 'd']], [[1, 'd'], [2, 'd']], [[1, 'd'], [2, 'd']], [[1, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '|'), ('box', ''), ('op', '|'), ('op', '/'), ('op', '('), ('op', '−'), ('op', '('), ('box', ''), ('op', '·'), ('box', ''), ('op', ')'), ('op', '/'), ('op', '|'), ('box', ''), ('op', '|'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

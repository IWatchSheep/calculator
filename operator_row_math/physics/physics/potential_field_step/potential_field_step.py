"""Row for the operator: Weight

Picture:      □ = □ ( □ − □ ) + □ ( 1 / d − 1 / □ ) ( 1 / d ² ) ( □ − □ ) / d
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/potential_field_step
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Potential-field step'
KEY = 'physics/physics/potential_field_step'
PATTERN = '□ = □ ( □ − □ ) + □ ( 1 / d − 1 / □ ) ( 1 / d ² ) ( □ − □ ) / d'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['position', 'goal', 'obstacle', 'influence', 'k_att', 'k_rep']    # what each box (left to right) is
KINDS = ['list', 'list', 'list', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [4, 1, 0, 5, 3, 0, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('push', 'Fx, Fy, Fz'), 2: ('pull gain', 'strength of the pull toward the goal'), 4: ('goal', 'x, y, z in metres'), 6: ('robot', 'x, y, z in metres'), 9: ('push gain', 'strength of the push away from the obstacle'), 17: ('influence', 'metres, the obstacle pushes only inside this distance'), 28: ('obstacle', 'x, y, z in metres')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [], [], [], [], [], [[4, 'n']], [[4, 'n']], [[4, 'n'], [1, 'n']], [[4, 'n'], [1, 'bar']], [[4, 'n'], [1, 'd']], [[4, 'n']], [[4, 'n'], [2, 'n']], [[4, 'n'], [2, 'bar']], [[4, 'n'], [2, 'd']], [[4, 'n']], [[4, 'n']], [[4, 'n'], [3, 'n']], [[4, 'n'], [3, 'bar']], [[4, 'n'], [3, 'd']], [[4, 'n'], [3, 'd']], [[4, 'n']], [[4, 'n']], [[4, 'n']], [[4, 'n']], [[4, 'n']], [[4, 'n']], [[4, 'bar']], [[4, 'd']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', '+'), ('box', ''), ('op', '('), ('op', '1'), ('op', '/'), ('op', 'd'), ('op', '−'), ('op', '1'), ('op', '/'), ('box', ''), ('op', ')'), ('op', '('), ('op', '1'), ('op', '/'), ('op', 'd'), ('op', '2'), ('op', ')'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', '/'), ('op', 'd')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

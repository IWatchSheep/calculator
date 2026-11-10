"""Row for the operator: Weight

Picture:      □ = | □ − □ | ≤ □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/point_inside_sphere
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Point inside a sphere'
KEY = 'physics/physics/point_inside_sphere'
PATTERN = '□ = | □ − □ | ≤ □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['centre', 'radius', 'point']    # what each box (left to right) is
KINDS = ['list', 'number', 'list']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [2, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('inside', '1 if inside or on the sphere, 0 if outside'), 3: ('point', 'x, y, z in metres'), 5: ('centre', 'x, y, z in metres'), 8: ('radius', 'metres')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '|'), ('box', ''), ('op', '−'), ('box', ''), ('op', '|'), ('op', '≤'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

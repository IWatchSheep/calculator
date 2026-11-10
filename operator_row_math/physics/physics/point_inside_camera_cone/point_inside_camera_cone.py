"""Row for the operator: Weight

Picture:      □ = □ ∈ cone ( □ , □ , □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/point_inside_camera_cone
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Point inside a camera cone'
KEY = 'physics/physics/point_inside_camera_cone'
PATTERN = '□ = □ ∈ cone ( □ , □ , □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['camera', 'direction', 'half_angle', 'point']    # what each box (left to right) is
KINDS = ['list', 'list', 'number', 'list']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [3, 0, 1, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('inside', '1 if the point is inside the camera cone, 0 if outside'), 2: ('point', 'x, y, z in metres'), 6: ('camera', 'x, y, z in metres'), 8: ('look direction', 'x, y, z, it is normalised for you'), 10: ('half angle', 'radians, from the look direction to the edge of the view')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '∈'), ('op', 'cone'), ('op', '('), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

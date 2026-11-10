"""Row for the operator: Weight

Picture:      □ = ( 6371000 cos □ □ , 6371000 □ , □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/local_east_north_up
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Local east, north, up'
KEY = 'physics/physics/local_east_north_up'
PATTERN = '□ = ( 6371000 cos □ □ , 6371000 □ , □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['lat', 'delta_lat', 'delta_lon', 'delta_height']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 2, 1, 3]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('offset', 'east, north, up, metres'), 5: ('latitude', 'radians, north is positive, where the patch touches the Earth'), 6: ('change in longitude', 'radians, east is positive'), 9: ('change in latitude', 'radians'), 11: ('change in height', 'metres, up is positive')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('op', '6371000'), ('op', 'cos'), ('box', ''), ('box', ''), ('op', ','), ('op', '6371000'), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

"""Row for the operator: Weight

Picture:      □ = atan2 ( cos □ sin □ − sin □ cos □ cos ( □ − □ ) , sin ( □ − □ ) cos □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/bearing_between
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Bearing between two points'
KEY = 'physics/physics/bearing_between'
PATTERN = '□ = atan2 ( cos □ sin □ − sin □ cos □ cos ( □ − □ ) , sin ( □ − □ ) cos □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['lat1', 'lon1', 'lat2', 'lon2']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 2, 0, 2, 3, 1, 3, 1, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('heading', 'radians, 0 is east, positive turns toward north'), 5: ('first latitude', 'radians, north is positive'), 7: ('second latitude', 'radians, north is positive'), 15: ('second longitude', 'radians, east is positive'), 17: ('first longitude', 'radians, east is positive')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', 'atan2'), ('op', '('), ('op', 'cos'), ('box', ''), ('op', 'sin'), ('box', ''), ('op', '−'), ('op', 'sin'), ('box', ''), ('op', 'cos'), ('box', ''), ('op', 'cos'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', ','), ('op', 'sin'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', 'cos'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

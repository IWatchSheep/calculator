"""Row for the operator: Weight

Picture:      □ = □ + □ □ ( cos □ , sin □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/dead_reckoning
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Dead reckoning'
KEY = 'physics/physics/dead_reckoning'
PATTERN = '□ = □ + □ □ ( cos □ , sin □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['position', 'speed', 'heading', 't']    # what each box (left to right) is
KINDS = ['list', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 3, 2, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('new position', 'east, north, metres'), 2: ('position', 'east, north, metres'), 4: ('speed', 'metres per second, negative backs up'), 5: ('time', 'seconds'), 8: ('heading', 'radians, 0 is east, positive turns toward north')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '+'), ('box', ''), ('box', ''), ('op', '('), ('op', 'cos'), ('box', ''), ('op', ','), ('op', 'sin'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

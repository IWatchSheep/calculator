"""Row for the operator: Weight

Picture:      □ = ( □ cos □ · □ , □ sin □ · □ − ½ g □ ² )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/projectile_position
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Projectile position'
KEY = 'physics/physics/projectile_position'
PATTERN = '□ = ( □ cos □ · □ , □ sin □ · □ − ½ g □ ² )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['v', 'angle', 't']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 2, 0, 1, 2, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('position', 'x then y, metres, y is up'), 3: ('launch speed', 'metres per second'), 5: ('angle', 'radians above the horizontal'), 7: ('time', 'seconds since launch'), 16: ('gravity', '9.81 m/s2')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('box', ''), ('op', 'cos'), ('box', ''), ('op', '·'), ('box', ''), ('op', ','), ('box', ''), ('op', 'sin'), ('box', ''), ('op', '·'), ('box', ''), ('op', '−'), ('op', '½'), ('op', 'g'), ('box', ''), ('op', '2'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

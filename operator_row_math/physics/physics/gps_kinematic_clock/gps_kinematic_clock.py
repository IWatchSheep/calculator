"""Row for the operator: Weight

Picture:      □ = ( 1 / □ − 1 ) · 86400 · 1000000
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/gps_kinematic_clock
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'GPS kinematic clock'
KEY = 'physics/physics/gps_kinematic_clock'
PATTERN = '□ = ( 1 / □ − 1 ) · 86400 · 1000000'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['gamma']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('clock rate', 'microseconds per day, negative'), 5: ('Lorentz factor', 'from the satellite speed, the answer of the row above when this is chained')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [], [], [], [], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('op', '1'), ('op', '/'), ('box', ''), ('op', '−'), ('op', '1'), ('op', ')'), ('op', '·'), ('op', '86400'), ('op', '·'), ('op', '1000000')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

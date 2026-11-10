"""Row for the operator: Weight

Picture:      □ = □ ( □ + □ □ ) + ( 1 − □ ) □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/complementary_filter
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Complementary filter'
KEY = 'physics/physics/complementary_filter'
PATTERN = '□ = □ ( □ + □ □ ) + ( 1 − □ ) □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['previous', 'gyro', 'dt', 'measured', 'alpha']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [4, 0, 1, 2, 4, 3]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('angle', 'radians, the new estimate'), 2: ('gyro weight', '0 takes the measurement, 1 trusts the gyro'), 4: ('previous angle', 'radians'), 6: ('turn rate', 'radians per second'), 7: ('time step', 'seconds'), 15: ('measured angle', 'radians, from gravity or a compass')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '('), ('box', ''), ('op', '+'), ('box', ''), ('box', ''), ('op', ')'), ('op', '+'), ('op', '('), ('op', '1'), ('op', '−'), ('box', ''), ('op', ')'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

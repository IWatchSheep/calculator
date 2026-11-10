"""Row for the operator: Relativistic momentum: from the Lorentz factor

Picture:      □ = □ × □ × □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/relativistic_momentum_from_gamma
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Relativistic momentum: from the Lorentz factor'
KEY = 'physics/physics/relativistic_momentum_from_gamma'
PATTERN = '□ = □ × □ × □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['gamma', 'm', 'v']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('momentum', 'kg m/s'), 2: ('Lorentz factor', 'the answer of the row above'), 4: ('rest mass', 'kilograms'), 6: ('speed', 'metres per second, the speed typed above')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '×'), ('box', ''), ('op', '×'), ('box', '')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

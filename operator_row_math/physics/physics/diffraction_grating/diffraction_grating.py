"""Row for the operator: Diffraction grating

Picture:      □ × sin ( □ ) = □ × □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/diffraction_grating
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Diffraction grating'
KEY = 'physics/physics/diffraction_grating'
PATTERN = '□ × sin ( □ ) = □ × □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['m', 'wavelength', 'd']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [2, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('box', ''), ('op', '×'), ('op', 'sin'), ('op', '('), ('out', ''), ('op', ')'), ('op', '='), ('box', ''), ('op', '×'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))

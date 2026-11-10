"""Row for the operator: Compton wavelength shift

Picture:      □ = h / ( m × c ) × ( 1 − cos ( □ ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/compton_shift
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Compton wavelength shift'
KEY = 'physics/physics/compton_shift'
PATTERN = '□ = h / ( m × c ) × ( 1 − cos ( □ ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['theta']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', 'h'), ('op', '/'), ('op', '('), ('op', 'm'), ('op', '×'), ('op', 'c'), ('op', ')'), ('op', '×'), ('op', '('), ('op', '1'), ('op', '−'), ('op', 'cos'), ('op', '('), ('box', ''), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

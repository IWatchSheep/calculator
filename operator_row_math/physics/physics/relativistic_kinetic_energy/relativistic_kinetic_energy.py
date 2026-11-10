"""Row for the operator: Relativistic kinetic energy

Picture:      □ = ( γ − 1 ) × □ × c ² with □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/relativistic_kinetic_energy
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Relativistic kinetic energy'
KEY = 'physics/physics/relativistic_kinetic_energy'
PATTERN = '□ = ( γ − 1 ) × □ × c ² with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['m', 'v']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('op', 'γ'), ('op', '−'), ('op', '1'), ('op', ')'), ('op', '×'), ('box', ''), ('op', '×'), ('op', 'c'), ('op', '2'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

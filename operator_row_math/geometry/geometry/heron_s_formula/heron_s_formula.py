"""Row for the operator: Heron's formula

Picture:      □ = √ ( s ( s − □ ) ( s − □ ) ( s − □ ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py geometry/geometry/heron_s_formula
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Heron's formula"
KEY = 'geometry/geometry/heron_s_formula'
PATTERN = '□ = √ ( s ( s − □ ) ( s − □ ) ( s − □ ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['a', 'b', 'c']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '√'), ('op', '('), ('op', 's'), ('op', '('), ('op', 's'), ('op', '−'), ('box', ''), ('op', ')'), ('op', '('), ('op', 's'), ('op', '−'), ('box', ''), ('op', ')'), ('op', '('), ('op', 's'), ('op', '−'), ('box', ''), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

"""Row for the operator: De Moivre's theorem

Picture:      (□(cos □ + i sin □))ⁿ = □ⁿ(cos □□ + i sin □□)
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/complex_analysis/de_moivre_s_theorem
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "De Moivre's theorem"
KEY = 'math/complex_analysis/de_moivre_s_theorem'
PATTERN = '(□(cos □ + i sin □))ⁿ = □ⁿ(cos □□ + i sin □□)'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['r', 'theta', 'n']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '('), ('box', ''), ('op', '(cos'), ('box', ''), ('op', '+ i sin'), ('box', ''), ('op', '))ⁿ')]      # cards left of "="
RIGHT = [('box', ''), ('op', 'ⁿ(cos'), ('box', ''), ('box', ''), ('op', '+ i sin'), ('box', ''), ('box', ''), ('op', ')')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

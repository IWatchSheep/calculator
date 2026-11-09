"""Row for the operator: Catalan number

Picture:      □ₙ = C(2□, □) / (□ + 1)
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/graph_theory_and_combinatorics/catalan_number
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Catalan number'
KEY = 'math/graph_theory_and_combinatorics/catalan_number'
PATTERN = '□ₙ = C(2□, □) / (□ + 1)'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('box', ''), ('op', 'ₙ')]      # cards left of "="
RIGHT = [('op', 'C(2'), ('box', ''), ('op', ','), ('box', ''), ('op', ') / ('), ('box', ''), ('op', '+ 1)')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

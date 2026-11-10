"""Row for the operator: Derivative

Picture:      □ = lim ( h → 0 ) ( ( □ ( □ + h ) − □ ( □ ) ) / h )
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/calculus/derivative
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Derivative'
KEY = 'math/calculus/derivative'
PATTERN = '□ = lim ( h → 0 ) ( ( □ ( □ + h ) − □ ( □ ) ) / h )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'x']    # what each box (left to right) is
KINDS = ['function', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', 'lim'), ('op', '('), ('op', 'h'), ('op', '→'), ('op', '0'), ('op', ')'), ('op', '('), ('op', '('), ('box', ''), ('op', '('), ('box', ''), ('op', '+'), ('op', 'h'), ('op', ')'), ('op', '−'), ('box', ''), ('op', '('), ('box', ''), ('op', ')'), ('op', ')'), ('op', '/'), ('op', 'h'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

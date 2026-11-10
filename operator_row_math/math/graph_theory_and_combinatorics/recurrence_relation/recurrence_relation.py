"""Row for the operator: Recurrence relation

Picture:      □ ₙ = f ( □ ₙ₋₁ , … ) with □ , □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/graph_theory_and_combinatorics/recurrence_relation
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Recurrence relation'
KEY = 'math/graph_theory_and_combinatorics/recurrence_relation'
PATTERN = '□ ₙ = f ( □ ₙ₋₁ , … ) with □ , □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['coeffs', 'start', 'n']    # what each box (left to right) is
KINDS = ['list', 'list', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('dec', ''), ('op', 'ₙ'), ('op', '='), ('op', 'f'), ('op', '('), ('dec', ''), ('op', 'ₙ₋₁'), ('op', ','), ('op', '…'), ('op', ')'), ('op', 'with'), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

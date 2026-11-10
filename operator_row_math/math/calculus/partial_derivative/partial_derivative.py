"""Row for the operator: Partial derivative

Picture:      ∂ □ / ∂ □ ᵢ ≈ ( f ( … □ ᵢ + □ … ) − f ( … □ ᵢ − □ … ) ) / 2 □ with □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/calculus/partial_derivative
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Partial derivative'
KEY = 'math/calculus/partial_derivative'
PATTERN = '∂ □ / ∂ □ ᵢ ≈ ( f ( … □ ᵢ + □ … ) − f ( … □ ᵢ − □ … ) ) / 2 □ with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'point', 'i']    # what each box (left to right) is
KINDS = ['multi', 'list', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '∂'), ('box', ''), ('op', '/'), ('op', '∂'), ('dec', ''), ('op', 'ᵢ'), ('op', '≈'), ('op', '('), ('op', 'f'), ('op', '('), ('op', '…'), ('box', ''), ('op', 'ᵢ'), ('op', '+'), ('dec', ''), ('op', '…'), ('op', ')'), ('op', '−'), ('op', 'f'), ('op', '('), ('op', '…'), ('dec', ''), ('op', 'ᵢ'), ('op', '−'), ('dec', ''), ('op', '…'), ('op', ')'), ('op', ')'), ('op', '/'), ('op', '2'), ('dec', ''), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

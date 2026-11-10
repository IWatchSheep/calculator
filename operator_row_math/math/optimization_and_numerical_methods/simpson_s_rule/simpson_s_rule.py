"""Row for the operator: Simpson's rule

Picture:      ∫ ₐ ᵇ □ ≈ □ / 3 · ( □ ₀ + 4 □ ₁ + 2 □ ₂ + ... + □ ₙ ) with □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/simpson_s_rule
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Simpson's rule"
KEY = 'math/optimization_and_numerical_methods/simpson_s_rule'
PATTERN = '∫ ₐ ᵇ □ ≈ □ / 3 · ( □ ₀ + 4 □ ₁ + 2 □ ₂ + ... + □ ₙ ) with □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'a', 'b']    # what each box (left to right) is
KINDS = ['function', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '∫'), ('op', 'ₐ'), ('op', 'ᵇ'), ('box', ''), ('op', '≈'), ('dec', ''), ('op', '/'), ('op', '3'), ('op', '·'), ('op', '('), ('dec', ''), ('op', '₀'), ('op', '+'), ('op', '4'), ('dec', ''), ('op', '₁'), ('op', '+'), ('op', '2'), ('dec', ''), ('op', '₂'), ('op', '+'), ('op', '...'), ('op', '+'), ('dec', ''), ('op', 'ₙ'), ('op', ')'), ('op', 'with'), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

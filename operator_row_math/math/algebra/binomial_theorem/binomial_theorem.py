"""Row for the operator: Binomial theorem

Picture:      ( □ + □ ) ⁿ = Σ ₖ C ( □ , □ ) · □ ⁿ⁻ᵏ · □ ᵏ
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/algebra/binomial_theorem
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Binomial theorem'
KEY = 'math/algebra/binomial_theorem'
PATTERN = '( □ + □ ) ⁿ = Σ ₖ C ( □ , □ ) · □ ⁿ⁻ᵏ · □ ᵏ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['a', 'b', 'n']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 2, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '('), ('box', ''), ('op', '+'), ('box', ''), ('op', ')'), ('op', 'ⁿ'), ('op', '='), ('op', 'Σ'), ('op', 'ₖ'), ('op', 'C'), ('op', '('), ('box', ''), ('op', ','), ('dec', ''), ('op', ')'), ('op', '·'), ('box', ''), ('op', 'ⁿ⁻ᵏ'), ('op', '·'), ('box', ''), ('op', 'ᵏ')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

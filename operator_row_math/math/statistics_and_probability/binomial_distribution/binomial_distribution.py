"""Row for the operator: Binomial distribution

Picture:      P ( □ = □ ) = C ( □ , □ ) · □ ᵏ · ( 1 − □ ) ⁿ⁻ᵏ
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/statistics_and_probability/binomial_distribution
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Binomial distribution'
KEY = 'math/statistics_and_probability/binomial_distribution'
PATTERN = 'P ( □ = □ ) = C ( □ , □ ) · □ ᵏ · ( 1 − □ ) ⁿ⁻ᵏ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n', 'k', 'p']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 0, 1, 2, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'P'), ('op', '('), ('dec', ''), ('op', '='), ('box', ''), ('op', ')'), ('op', '='), ('op', 'C'), ('op', '('), ('box', ''), ('op', ','), ('box', ''), ('op', ')'), ('op', '·'), ('box', ''), ('op', 'ᵏ'), ('op', '·'), ('op', '('), ('op', '1'), ('op', '−'), ('box', ''), ('op', ')'), ('op', 'ⁿ⁻ᵏ')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

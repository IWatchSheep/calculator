"""Row for the operator: Stirling number (second kind)

Picture:      S(□, □) = (1/□!) Σⱼ (−1)ʲ C(□, □) (□ − □)ⁿ
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/graph_theory_and_combinatorics/stirling_number_second_kind
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Stirling number (second kind)'
KEY = 'math/graph_theory_and_combinatorics/stirling_number_second_kind'
PATTERN = 'S(□, □) = (1/□!) Σⱼ (−1)ʲ C(□, □) (□ − □)ⁿ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n', 'k']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'S('), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('op', '(1/'), ('box', ''), ('op', '!) Σⱼ (−1)ʲ C('), ('box', ''), ('op', ','), ('box', ''), ('op', ') ('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')ⁿ')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

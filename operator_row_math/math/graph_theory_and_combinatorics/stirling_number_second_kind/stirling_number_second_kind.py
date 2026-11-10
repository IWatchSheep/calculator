"""Row for the operator: Stirling number (second kind)

Picture:      S ( □ , □ ) = ( 1 / □ ! ) Σ ⱼ ( − 1 ) ʲ C ( □ , □ ) ( □ − □ ) ⁿ
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/graph_theory_and_combinatorics/stirling_number_second_kind
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Stirling number (second kind)'
KEY = 'math/graph_theory_and_combinatorics/stirling_number_second_kind'
PATTERN = 'S ( □ , □ ) = ( 1 / □ ! ) Σ ⱼ ( − 1 ) ʲ C ( □ , □ ) ( □ − □ ) ⁿ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n', 'k']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 1, 1, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
FRAC = [[], [], [], [], [], [], [], [], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [[1, 'd']], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'S'), ('op', '('), ('box', ''), ('op', ','), ('box', ''), ('op', ')'), ('op', '='), ('op', '('), ('op', '1'), ('op', '/'), ('box', ''), ('op', '!'), ('op', ')'), ('op', 'Σ'), ('op', 'j'), ('op', '('), ('op', '−'), ('op', '1'), ('op', ')'), ('op', 'j'), ('op', 'C'), ('op', '('), ('box', ''), ('op', ','), ('dec', ''), ('op', ')'), ('op', '('), ('box', ''), ('op', '−'), ('dec', ''), ('op', ')'), ('op', 'n')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))

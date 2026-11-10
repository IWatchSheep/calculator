"""Row for the operator: Product rule

Picture:      ( f · g ) ′ = f ′ · g + f · g ′ with □ , □ , □ , □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/calculus/product_rule
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Product rule'
KEY = 'math/calculus/product_rule'
PATTERN = '( f · g ) ′ = f ′ · g + f · g ′ with □ , □ , □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['f', 'fprime', 'g', 'gprime']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '('), ('op', 'f'), ('op', '·'), ('op', 'g'), ('op', ')'), ('op', '′'), ('op', '='), ('op', 'f'), ('op', '′'), ('op', '·'), ('op', 'g'), ('op', '+'), ('op', 'f'), ('op', '·'), ('op', 'g'), ('op', '′'), ('op', 'with'), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))

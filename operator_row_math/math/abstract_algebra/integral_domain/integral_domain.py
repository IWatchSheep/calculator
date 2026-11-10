"""Row for the operator: Integral domain

Picture:      a × b = 0 ⇒ a = 0 or b = 0 with □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/abstract_algebra/integral_domain
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Integral domain'
KEY = 'math/abstract_algebra/integral_domain'
PATTERN = 'a × b = 0 ⇒ a = 0 or b = 0 with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'a'), ('op', '×'), ('op', 'b'), ('op', '='), ('op', '0'), ('op', '⇒'), ('op', 'a'), ('op', '='), ('op', '0'), ('op', 'or'), ('op', 'b'), ('op', '='), ('op', '0'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

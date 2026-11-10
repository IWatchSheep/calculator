"""Row for the operator: Injective

Picture:      f ( □ ) = f ( □ ) ⇒ □ = □ with □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/category_theory_and_foundations/injective
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Injective'
KEY = 'math/category_theory_and_foundations/injective'
PATTERN = 'f ( □ ) = f ( □ ) ⇒ □ = □ with □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'domain']    # what each box (left to right) is
KINDS = ['function', 'set']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'f'), ('op', '('), ('dec', ''), ('op', ')'), ('op', '='), ('op', 'f'), ('op', '('), ('dec', ''), ('op', ')'), ('op', '⇒'), ('dec', ''), ('op', '='), ('dec', ''), ('op', 'with'), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

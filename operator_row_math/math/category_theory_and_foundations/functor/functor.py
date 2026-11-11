"""Row for the operator: Functor

Picture:      □ : 𝒞 → 𝒟
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py math/category_theory_and_foundations/functor
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Functor'
KEY = 'math/category_theory_and_foundations/functor'
PATTERN = '□ : 𝒞 → 𝒟'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. The whole statement is the definition.'    # formula only: what the row says (no box is added and compute() is unchanged)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('dec', ''), ('op', ':'), ('op', '𝒞'), ('op', '→'), ('op', '𝒟')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

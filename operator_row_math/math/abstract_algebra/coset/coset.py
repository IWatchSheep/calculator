"""Row for the operator: Coset

Picture:      □ □ = { □ ∘ □ : □ ∈ □ } with □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/abstract_algebra/coset
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Coset'
KEY = 'math/abstract_algebra/coset'
PATTERN = '□ □ = { □ ∘ □ : □ ∈ □ } with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['g', 'H', 'op']    # what each box (left to right) is
KINDS = ['item', 'set', 'multi']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 0, 1, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('box', ''), ('box', ''), ('op', '='), ('op', '{'), ('box', ''), ('op', '∘'), ('dec', ''), ('op', ':'), ('dec', ''), ('op', '∈'), ('box', ''), ('op', '}'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

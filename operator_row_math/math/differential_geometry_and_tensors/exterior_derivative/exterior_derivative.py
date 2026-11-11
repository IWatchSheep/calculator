"""Row for the operator: Exterior derivative

Picture:      d ( □ d □ ) = d □ ∧ d □
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py math/differential_geometry_and_tensors/exterior_derivative
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Exterior derivative'
KEY = 'math/differential_geometry_and_tensors/exterior_derivative'
PATTERN = 'd ( □ d □ ) = d □ ∧ d □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. Needs the form. The two rows already show d(f dx) = df ∧ dx and d² = 0.'    # formula only: what the row says (no box is added and compute() is unchanged)
WORDS = {0: ('exterior derivative', 'sends a form to the form one degree higher'), 2: ('function', 'a smooth function'), 4: ('coordinate', 'the variable the form is written in'), 7: ('exterior derivative', 'sends a form to the form one degree higher'), 8: ('function', 'a smooth function'), 10: ('exterior derivative', 'sends a form to the form one degree higher'), 11: ('coordinate', 'the variable the form is written in')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'd'), ('op', '('), ('dec', ''), ('op', 'd'), ('dec', ''), ('op', ')'), ('op', '='), ('op', 'd'), ('dec', ''), ('op', '∧'), ('op', 'd'), ('dec', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

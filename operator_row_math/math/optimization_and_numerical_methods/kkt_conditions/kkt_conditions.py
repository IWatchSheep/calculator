"""Row for the operator: KKT conditions

Picture:      ∇ □ + □ · ∇ □ = 0
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/kkt_conditions
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'KKT conditions'
KEY = 'math/optimization_and_numerical_methods/kkt_conditions'
PATTERN = '∇ □ + □ · ∇ □ = 0'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. Needs the objective, the constraints, and the multipliers. The four rows are the conditions.'    # formula only: what the row says (no box is added and compute() is unchanged)
WORDS = {0: ('gradient', 'the direction of steepest rise'), 1: ('objective', 'f, the function being minimized'), 3: ('multiplier', 'lambda, one weight for each constraint'), 5: ('gradient', 'the direction of steepest rise'), 6: ('constraint', 'g, the inequality being held'), 8: ('zero', 'the slopes cancel')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '∇'), ('dec', ''), ('op', '+'), ('dec', ''), ('op', '·'), ('op', '∇'), ('dec', ''), ('op', '='), ('op', '0')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

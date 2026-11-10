"""Row for the operator: Shortest path (A*)

Picture:      A* ( □ , □ , □ , □ ) = □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/graph_theory_and_combinatorics/a_star
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Shortest path (A*)'
KEY = 'math/graph_theory_and_combinatorics/a_star'
PATTERN = 'A* ( □ , □ , □ , □ ) = □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['graph', 'positions', 'start', 'goal']    # what each box (left to right) is
KINDS = ['wgraph', 'graph', 'item', 'item']    # what to type in each box (see advanced_input.KINDS)
WORDS = {2: ('graph', 'node to a list of neighbor, weight pairs, weights are metres'), 4: ('positions', 'node to x, y in metres'), 6: ('start', 'the node the robot is on'), 8: ('goal', 'the node the robot wants')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'A*'), ('op', '('), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))

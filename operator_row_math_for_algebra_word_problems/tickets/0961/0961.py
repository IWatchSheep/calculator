"""Row for the algebra word problem: Tickets 0961

Picture:      Tickets 0961(□, □, □, □) = □
Calculation:  reference - the problem is stored; no solver answers it yet
Try it:       python operator_row_math_for_algebra_word_problems/preview.py tickets/0961
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Tickets 0961'
KEY = 'tickets/0961'
LIBRARY_KEY = 'tickets/0961'    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = 'Tickets 0961(□, □, □, □) = □'
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = 'reference'
INPUTS = ['number 1', 'number 2', 'number 3', 'number 4']    # what each box (left to right) is: the numbers of the problem in the order they appear in its text
DEFAULTS = ['8', '5', '252', '1398']    # the numbers as written in the stored problem
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'Tickets 0961('), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

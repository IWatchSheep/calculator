"""Row for the algebra word problem: Percent 0627

Picture:      Percent 0627(□, □) = □
Calculation:  ready - fill the boxes, press = and the answer appears right of =
Try it:       python operator_row_math_for_algebra_word_problems/preview.py percent/0627
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Percent 0627'
KEY = 'percent/0627'
LIBRARY_KEY = 'percent/0627'    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = 'Percent 0627(□, □) = □'
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = 'ready'
INPUTS = ['number 1', 'number 2']    # what each box (left to right) is: the numbers of the problem in the order they appear in its text
DEFAULTS = ['60', '1360']    # the numbers as written in the stored problem
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'Percent 0627('), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)

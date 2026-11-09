"""Algebra word problem 0685   [Percent (markup)]

Problem : A store marks up a rug by 50% and sells it for $127.50. What did the store pay for it?
Let     : c = cost
Equation: 1.5c = 127.5
Solve   : 1.5c = 127.5 → c = 85
Answer  : $85.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0685'
KEY = 'percent_markup/0685'
NAME = 'Percent (markup) 0685'
CATEGORY = 'Percent (markup)'
PROBLEM = 'A store marks up a rug by 50% and sells it for $127.50. What did the store pay for it?'
LET = 'c = cost'
EQUATION = '1.5c = 127.5'
SOLVE = '1.5c = 127.5 → c = 85'
ANSWER = '$85.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A store marks up a rug by {0}% and sells it for ${1}. What did the store pay for it?'
NUMBERS = ['50', '127.50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

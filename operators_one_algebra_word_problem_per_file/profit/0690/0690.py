"""Algebra word problem 0690   [Profit]

Problem : A bakery stall has fixed costs of $750. Each item costs $2 to make and sells for $4. How many items must be sold to make a profit of $302?
Let     : n = items
Equation: 4n − (750 + 2n) = 302
Solve   : 2n = 1052 → n = 526
Answer  : 526 items

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0690'
KEY = 'profit/0690'
NAME = 'Profit 0690'
CATEGORY = 'Profit'
PROBLEM = 'A bakery stall has fixed costs of $750. Each item costs $2 to make and sells for $4. How many items must be sold to make a profit of $302?'
LET = 'n = items'
EQUATION = '4n − (750 + 2n) = 302'
SOLVE = '2n = 1052 → n = 526'
ANSWER = '526 items'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A bakery stall has fixed costs of ${0}. Each item costs ${1} to make and sells for ${2}. How many items must be sold to make a profit of ${3}?'
NUMBERS = ['750', '2', '4', '302']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

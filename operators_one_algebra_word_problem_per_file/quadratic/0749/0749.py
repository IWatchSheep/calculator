"""Algebra word problem 0749   [Quadratic]

Problem : The sum of two numbers is 54 and their product is 728. Find the numbers.
Let     : x = one number; other = 54 − x
Equation: x(54 − x) = 728
Solve   : x² − 54x + 728 = 0 → x = 26 (the other root, 28, gives the same pair)
Answer  : 26 and 28

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0749'
KEY = 'quadratic/0749'
NAME = 'Quadratic 0749'
CATEGORY = 'Quadratic'
PROBLEM = 'The sum of two numbers is 54 and their product is 728. Find the numbers.'
LET = 'x = one number; other = 54 − x'
EQUATION = 'x(54 − x) = 728'
SOLVE = 'x² − 54x + 728 = 0 → x = 26 (the other root, 28, gives the same pair)'
ANSWER = '26 and 28'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of two numbers is {0} and their product is {1}. Find the numbers.'
NUMBERS = ['54', '728']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

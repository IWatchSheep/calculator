"""Algebra word problem 0745   [Quadratic]

Problem : The square of a positive number plus 16 times the number equals 105. Find the number.
Let     : x = the number
Equation: x² + 16x = 105
Solve   : x² + 16x − 105 = 0 → (x − 5)(x + 21) = 0 → x = 5
Answer  : 5

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0745'
KEY = 'quadratic/0745'
NAME = 'Quadratic 0745'
CATEGORY = 'Quadratic'
PROBLEM = 'The square of a positive number plus 16 times the number equals 105. Find the number.'
LET = 'x = the number'
EQUATION = 'x² + 16x = 105'
SOLVE = 'x² + 16x − 105 = 0 → (x − 5)(x + 21) = 0 → x = 5'
ANSWER = '5'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The square of a positive number plus {0} times the number equals {1}. Find the number.'
NUMBERS = ['16', '105']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

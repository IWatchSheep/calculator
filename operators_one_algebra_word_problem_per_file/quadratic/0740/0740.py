"""Algebra word problem 0740   [Quadratic]

Problem : The square of a positive number plus 10 times the number equals 56. Find the number.
Let     : x = the number
Equation: x² + 10x = 56
Solve   : x² + 10x − 56 = 0 → (x − 4)(x + 14) = 0 → x = 4
Answer  : 4

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0740'
KEY = 'quadratic/0740'
NAME = 'Quadratic 0740'
CATEGORY = 'Quadratic'
PROBLEM = 'The square of a positive number plus 10 times the number equals 56. Find the number.'
LET = 'x = the number'
EQUATION = 'x² + 10x = 56'
SOLVE = 'x² + 10x − 56 = 0 → (x − 4)(x + 14) = 0 → x = 4'
ANSWER = '4'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The square of a positive number plus {0} times the number equals {1}. Find the number.'
NUMBERS = ['10', '56']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

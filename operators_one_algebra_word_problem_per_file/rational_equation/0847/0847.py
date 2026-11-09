"""Algebra word problem 0847   [Rational equation]

Problem : A number plus its reciprocal equals 10/3. Find the number.
Let     : x = the number
Equation: x + 1/x = 10/3
Solve   : Multiply by x: x² − (10/3)x + 1 = 0 → x = 3
Answer  : 3 or 1/3

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0847'
KEY = 'rational_equation/0847'
NAME = 'Rational equation 0847'
CATEGORY = 'Rational equation'
PROBLEM = 'A number plus its reciprocal equals 10/3. Find the number.'
LET = 'x = the number'
EQUATION = 'x + 1/x = 10/3'
SOLVE = 'Multiply by x: x² − (10/3)x + 1 = 0 → x = 3'
ANSWER = '3 or 1/3'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A number plus its reciprocal equals {0}/{1}. Find the number.'
NUMBERS = ['10', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

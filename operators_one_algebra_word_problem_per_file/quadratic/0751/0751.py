"""Algebra word problem 0751   [Quadratic]

Problem : The square of a positive number is 48 more than 8 times the number. Find the number.
Let     : x = the number
Equation: x² = 8x + 48
Solve   : x² − 8x − 48 = 0 → x = 12 (the other root, -4, is rejected)
Answer  : 12

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0751'
KEY = 'quadratic/0751'
NAME = 'Quadratic 0751'
CATEGORY = 'Quadratic'
PROBLEM = 'The square of a positive number is 48 more than 8 times the number. Find the number.'
LET = 'x = the number'
EQUATION = 'x² = 8x + 48'
SOLVE = 'x² − 8x − 48 = 0 → x = 12 (the other root, -4, is rejected)'
ANSWER = '12'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The square of a positive number is {0} more than {1} times the number. Find the number.'
NUMBERS = ['48', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

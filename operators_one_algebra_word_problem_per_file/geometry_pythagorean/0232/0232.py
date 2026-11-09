"""Algebra word problem 0232   [Geometry (Pythagorean)]

Problem : A rectangular TV screen is 60 in tall with a diagonal of 87 in. How wide is it?
Let     : x = width
Equation: 60² + x² = 87²
Solve   : x² − 3969 = 0 → x = 63 (the other root, -63, is rejected)
Answer  : 63 in

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0232'
KEY = 'geometry_pythagorean/0232'
NAME = 'Geometry (Pythagorean) 0232'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'A rectangular TV screen is 60 in tall with a diagonal of 87 in. How wide is it?'
LET = 'x = width'
EQUATION = '60² + x² = 87²'
SOLVE = 'x² − 3969 = 0 → x = 63 (the other root, -63, is rejected)'
ANSWER = '63 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangular TV screen is {0} in tall with a diagonal of {1} in. How wide is it?'
NUMBERS = ['60', '87']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

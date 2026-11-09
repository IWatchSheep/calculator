"""Algebra word problem 0233   [Geometry (Pythagorean)]

Problem : A rectangular field is 36 m long. A diagonal path across it is 45 m long. How wide is the field?
Let     : x = width
Equation: x² + 36² = 45²
Solve   : x² − 729 = 0 → x = 27 (the other root, -27, is rejected)
Answer  : 27 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0233'
KEY = 'geometry_pythagorean/0233'
NAME = 'Geometry (Pythagorean) 0233'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'A rectangular field is 36 m long. A diagonal path across it is 45 m long. How wide is the field?'
LET = 'x = width'
EQUATION = 'x² + 36² = 45²'
SOLVE = 'x² − 729 = 0 → x = 27 (the other root, -27, is rejected)'
ANSWER = '27 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangular field is {0} m long. A diagonal path across it is {1} m long. How wide is the field?'
NUMBERS = ['36', '45']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

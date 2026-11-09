"""Algebra word problem 0312   [Geometry (quadratic)]

Problem : A rectangle's length is 12 m more than its width, and its area is 640 m². Find the dimensions.
Let     : w = width
Equation: w(w + 12) = 640
Solve   : w² + 12w − 640 = 0 → (w − 20)(w + 32) = 0 → w = 20 (reject negative)
Answer  : Width 20 m, length 32 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0312'
KEY = 'geometry_quadratic/0312'
NAME = 'Geometry (quadratic) 0312'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = "A rectangle's length is 12 m more than its width, and its area is 640 m². Find the dimensions."
LET = 'w = width'
EQUATION = 'w(w + 12) = 640'
SOLVE = 'w² + 12w − 640 = 0 → (w − 20)(w + 32) = 0 → w = 20 (reject negative)'
ANSWER = 'Width 20 m, length 32 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A rectangle's length is {0} m more than its width, and its area is {1} m². Find the dimensions."
NUMBERS = ['12', '640']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0326   [Geometry (quadratic)]

Problem : A rectangle's length is 9 m more than its width, and its area is 850 m². Find the dimensions.
Let     : w = width
Equation: w(w + 9) = 850
Solve   : w² + 9w − 850 = 0 → (w − 25)(w + 34) = 0 → w = 25 (reject negative)
Answer  : Width 25 m, length 34 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0326'
KEY = 'geometry_quadratic/0326'
NAME = 'Geometry (quadratic) 0326'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = "A rectangle's length is 9 m more than its width, and its area is 850 m². Find the dimensions."
LET = 'w = width'
EQUATION = 'w(w + 9) = 850'
SOLVE = 'w² + 9w − 850 = 0 → (w − 25)(w + 34) = 0 → w = 25 (reject negative)'
ANSWER = 'Width 25 m, length 34 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A rectangle's length is {0} m more than its width, and its area is {1} m². Find the dimensions."
NUMBERS = ['9', '850']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

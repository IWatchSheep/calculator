"""Algebra word problem 0332   [Geometry (quadratic)]

Problem : A rectangle's length is 1 m more than its width, and its area is 306 m². Find the dimensions.
Let     : w = width
Equation: w(w + 1) = 306
Solve   : w² + w − 306 = 0 → (w − 17)(w + 18) = 0 → w = 17 (reject negative)
Answer  : Width 17 m, length 18 m

Status  : ready: archive_geometry_quadratic_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0332'
KEY = 'geometry_quadratic/0332'
NAME = 'Geometry (quadratic) 0332'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = "A rectangle's length is 1 m more than its width, and its area is 306 m². Find the dimensions."
LET = 'w = width'
EQUATION = 'w(w + 1) = 306'
SOLVE = 'w² + w − 306 = 0 → (w − 17)(w + 18) = 0 → w = 17 (reject negative)'
ANSWER = 'Width 17 m, length 18 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_quadratic_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A rectangle's length is {0} m more than its width, and its area is {1} m². Find the dimensions."
NUMBERS = ['1', '306']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

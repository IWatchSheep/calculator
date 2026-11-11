"""Algebra word problem 0322   [Geometry (quadratic)]

Problem : A rectangle's length is 10 m more than its width, and its area is 200 m². Find the dimensions.
Let     : w = width
Equation: w(w + 10) = 200
Solve   : w² + 10w − 200 = 0 → (w − 10)(w + 20) = 0 → w = 10 (reject negative)
Answer  : Width 10 m, length 20 m

Status  : ready: archive_geometry_quadratic_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0322'
KEY = 'geometry_quadratic/0322'
NAME = 'Geometry (quadratic) 0322'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = "A rectangle's length is 10 m more than its width, and its area is 200 m². Find the dimensions."
LET = 'w = width'
EQUATION = 'w(w + 10) = 200'
SOLVE = 'w² + 10w − 200 = 0 → (w − 10)(w + 20) = 0 → w = 10 (reject negative)'
ANSWER = 'Width 10 m, length 20 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_quadratic_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A rectangle's length is {0} m more than its width, and its area is {1} m². Find the dimensions."
NUMBERS = ['10', '200']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

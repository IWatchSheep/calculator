"""Algebra word problem 0335   [Geometry (quadratic)]

Problem : A rectangle has a perimeter of 84 ft and an area of 405 ft². Find its length and width.
Let     : w = width; length = 42 − w
Equation: w(42 − w) = 405
Solve   : w² − 42w + 405 = 0 → w = 15 (the other root, 27, just swaps length and width)
Answer  : 27 ft by 15 ft

Status  : ready: rectangle_from_perimeter_area answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0335'
KEY = 'geometry_quadratic/0335'
NAME = 'Geometry (quadratic) 0335'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A rectangle has a perimeter of 84 ft and an area of 405 ft². Find its length and width.'
LET = 'w = width; length = 42 − w'
EQUATION = 'w(42 − w) = 405'
SOLVE = 'w² − 42w + 405 = 0 → w = 15 (the other root, 27, just swaps length and width)'
ANSWER = '27 ft by 15 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'rectangle_from_perimeter_area'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangle has a perimeter of {0} ft and an area of {1} ft². Find its length and width.'
NUMBERS = ['84', '405']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0309   [Geometry (quadratic)]

Problem : A rectangle has a perimeter of 40 ft and an area of 36 ft². Find its length and width.
Let     : w = width; length = 20 − w
Equation: w(20 − w) = 36
Solve   : w² − 20w + 36 = 0 → w = 2 (the other root, 18, just swaps length and width)
Answer  : 18 ft by 2 ft

Status  : ready: rectangle_from_perimeter_area answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0309'
KEY = 'geometry_quadratic/0309'
NAME = 'Geometry (quadratic) 0309'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A rectangle has a perimeter of 40 ft and an area of 36 ft². Find its length and width.'
LET = 'w = width; length = 20 − w'
EQUATION = 'w(20 − w) = 36'
SOLVE = 'w² − 20w + 36 = 0 → w = 2 (the other root, 18, just swaps length and width)'
ANSWER = '18 ft by 2 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'rectangle_from_perimeter_area'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangle has a perimeter of {0} ft and an area of {1} ft². Find its length and width.'
NUMBERS = ['40', '36']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

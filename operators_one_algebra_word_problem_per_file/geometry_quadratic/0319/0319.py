"""Algebra word problem 0319   [Geometry (quadratic)]

Problem : A rectangle has a perimeter of 104 ft and an area of 651 ft². Find its length and width.
Let     : w = width; length = 52 − w
Equation: w(52 − w) = 651
Solve   : w² − 52w + 651 = 0 → w = 21 (the other root, 31, just swaps length and width)
Answer  : 31 ft by 21 ft

Status  : ready: rectangle_from_perimeter_area answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0319'
KEY = 'geometry_quadratic/0319'
NAME = 'Geometry (quadratic) 0319'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A rectangle has a perimeter of 104 ft and an area of 651 ft². Find its length and width.'
LET = 'w = width; length = 52 − w'
EQUATION = 'w(52 − w) = 651'
SOLVE = 'w² − 52w + 651 = 0 → w = 21 (the other root, 31, just swaps length and width)'
ANSWER = '31 ft by 21 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'rectangle_from_perimeter_area'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangle has a perimeter of {0} ft and an area of {1} ft². Find its length and width.'
NUMBERS = ['104', '651']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0275   [Geometry (area)]

Problem : A rectangle's length is twice its width. If the length is decreased by 6 m and the width increased by 4 m, the area stays the same. Find the original dimensions.
Let     : w = width
Equation: (2w − 6)(w + 4) = 2w²
Solve   : 2w = 24 → w = 12
Answer  : Width 12 m, length 24 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0275'
KEY = 'geometry_area/0275'
NAME = 'Geometry (area) 0275'
CATEGORY = 'Geometry (area)'
PROBLEM = "A rectangle's length is twice its width. If the length is decreased by 6 m and the width increased by 4 m, the area stays the same. Find the original dimensions."
LET = 'w = width'
EQUATION = '(2w − 6)(w + 4) = 2w²'
SOLVE = '2w = 24 → w = 12'
ANSWER = 'Width 12 m, length 24 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A rectangle's length is twice its width. If the length is decreased by {0} m and the width increased by {1} m, the area stays the same. Find the original dimensions."
NUMBERS = ['6', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

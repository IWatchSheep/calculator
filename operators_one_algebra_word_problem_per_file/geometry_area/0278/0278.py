"""Algebra word problem 0278   [Geometry (area)]

Problem : A rectangle's length is twice its width. If the length is decreased by 5 m and the width increased by 3 m, the area stays the same. Find the original dimensions.
Let     : w = width
Equation: (2w − 5)(w + 3) = 2w²
Solve   : Collect like terms → w = 15
Answer  : Width 15 m, length 30 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0278'
KEY = 'geometry_area/0278'
NAME = 'Geometry (area) 0278'
CATEGORY = 'Geometry (area)'
PROBLEM = "A rectangle's length is twice its width. If the length is decreased by 5 m and the width increased by 3 m, the area stays the same. Find the original dimensions."
LET = 'w = width'
EQUATION = '(2w − 5)(w + 3) = 2w²'
SOLVE = 'Collect like terms → w = 15'
ANSWER = 'Width 15 m, length 30 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A rectangle's length is twice its width. If the length is decreased by {0} m and the width increased by {1} m, the area stays the same. Find the original dimensions."
NUMBERS = ['5', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

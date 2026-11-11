"""Algebra word problem 0286   [Geometry (area)]

Problem : A trapezoid has parallel sides of 10 cm and 9 cm and an area of 85.5 cm². Find its height.
Let     : h = height
Equation: (1/2)(10 + 9)h = 85.5
Solve   : 9.5h = 85.5 → h = 9
Answer  : 9 cm

Status  : ready: archive_geometry_area_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0286'
KEY = 'geometry_area/0286'
NAME = 'Geometry (area) 0286'
CATEGORY = 'Geometry (area)'
PROBLEM = 'A trapezoid has parallel sides of 10 cm and 9 cm and an area of 85.5 cm². Find its height.'
LET = 'h = height'
EQUATION = '(1/2)(10 + 9)h = 85.5'
SOLVE = '9.5h = 85.5 → h = 9'
ANSWER = '9 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_area_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A trapezoid has parallel sides of {0} cm and {1} cm and an area of {2} cm². Find its height.'
NUMBERS = ['10', '9', '85.5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

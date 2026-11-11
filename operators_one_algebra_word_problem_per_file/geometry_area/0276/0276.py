"""Algebra word problem 0276   [Geometry (area)]

Problem : A trapezoid has parallel sides of 7 cm and 29 cm and an area of 270 cm². Find its height.
Let     : h = height
Equation: (1/2)(7 + 29)h = 270
Solve   : 18h = 270 → h = 15
Answer  : 15 cm

Status  : ready: archive_geometry_area_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0276'
KEY = 'geometry_area/0276'
NAME = 'Geometry (area) 0276'
CATEGORY = 'Geometry (area)'
PROBLEM = 'A trapezoid has parallel sides of 7 cm and 29 cm and an area of 270 cm². Find its height.'
LET = 'h = height'
EQUATION = '(1/2)(7 + 29)h = 270'
SOLVE = '18h = 270 → h = 15'
ANSWER = '15 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_area_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A trapezoid has parallel sides of {0} cm and {1} cm and an area of {2} cm². Find its height.'
NUMBERS = ['7', '29', '270']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

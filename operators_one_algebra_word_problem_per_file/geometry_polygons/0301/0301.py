"""Algebra word problem 0301   [Geometry (polygons)]

Problem : The interior angles of a polygon add up to 720°. How many sides does it have?
Let     : n = number of sides
Equation: 180(n − 2) = 720
Solve   : 180n = 1080 → n = 6
Answer  : 6 sides

Status  : ready: polygon_angle_sum answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0301'
KEY = 'geometry_polygons/0301'
NAME = 'Geometry (polygons) 0301'
CATEGORY = 'Geometry (polygons)'
PROBLEM = 'The interior angles of a polygon add up to 720°. How many sides does it have?'
LET = 'n = number of sides'
EQUATION = '180(n − 2) = 720'
SOLVE = '180n = 1080 → n = 6'
ANSWER = '6 sides'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'polygon_angle_sum'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The interior angles of a polygon add up to {0}°. How many sides does it have?'
NUMBERS = ['720']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

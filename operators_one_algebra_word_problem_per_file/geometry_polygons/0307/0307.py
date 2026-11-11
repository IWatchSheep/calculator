"""Algebra word problem 0307   [Geometry (polygons)]

Problem : Each interior angle of a regular polygon measures 135°. How many sides does the polygon have?
Let     : n = number of sides
Equation: 180(n − 2)/n = 135
Solve   : Multiply by n: 180n − 360 = 135n → n = 8
Answer  : 8 sides

Status  : ready: archive_geometry_polygons_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0307'
KEY = 'geometry_polygons/0307'
NAME = 'Geometry (polygons) 0307'
CATEGORY = 'Geometry (polygons)'
PROBLEM = 'Each interior angle of a regular polygon measures 135°. How many sides does the polygon have?'
LET = 'n = number of sides'
EQUATION = '180(n − 2)/n = 135'
SOLVE = 'Multiply by n: 180n − 360 = 135n → n = 8'
ANSWER = '8 sides'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_polygons_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Each interior angle of a regular polygon measures {0}°. How many sides does the polygon have?'
NUMBERS = ['135']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

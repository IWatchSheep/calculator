"""Algebra word problem 0304   [Geometry (polygons)]

Problem : Each exterior angle of a regular polygon is 18°. How many sides does it have?
Let     : n = number of sides
Equation: 360/n = 18
Solve   : Multiply by n → n = 20
Answer  : 20 sides

Status  : ready: archive_geometry_polygons_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0304'
KEY = 'geometry_polygons/0304'
NAME = 'Geometry (polygons) 0304'
CATEGORY = 'Geometry (polygons)'
PROBLEM = 'Each exterior angle of a regular polygon is 18°. How many sides does it have?'
LET = 'n = number of sides'
EQUATION = '360/n = 18'
SOLVE = 'Multiply by n → n = 20'
ANSWER = '20 sides'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_polygons_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Each exterior angle of a regular polygon is {0}°. How many sides does it have?'
NUMBERS = ['18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

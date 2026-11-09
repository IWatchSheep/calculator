"""Algebra word problem 0300   [Geometry (polygons)]

Problem : Each interior angle of a regular polygon measures 150°. How many sides does the polygon have?
Let     : n = number of sides
Equation: 180(n − 2)/n = 150
Solve   : Multiply by n: 180n − 360 = 150n → n = 12
Answer  : 12 sides

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0300'
KEY = 'geometry_polygons/0300'
NAME = 'Geometry (polygons) 0300'
CATEGORY = 'Geometry (polygons)'
PROBLEM = 'Each interior angle of a regular polygon measures 150°. How many sides does the polygon have?'
LET = 'n = number of sides'
EQUATION = '180(n − 2)/n = 150'
SOLVE = 'Multiply by n: 180n − 360 = 150n → n = 12'
ANSWER = '12 sides'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Each interior angle of a regular polygon measures {0}°. How many sides does the polygon have?'
NUMBERS = ['150']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

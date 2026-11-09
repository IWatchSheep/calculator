"""Algebra word problem 0284   [Geometry (area)]

Problem : A trapezoid has parallel sides of 19 cm and 19 cm and an area of 247 cm². Find its height.
Let     : h = height
Equation: (1/2)(19 + 19)h = 247
Solve   : 19h = 247 → h = 13
Answer  : 13 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0284'
KEY = 'geometry_area/0284'
NAME = 'Geometry (area) 0284'
CATEGORY = 'Geometry (area)'
PROBLEM = 'A trapezoid has parallel sides of 19 cm and 19 cm and an area of 247 cm². Find its height.'
LET = 'h = height'
EQUATION = '(1/2)(19 + 19)h = 247'
SOLVE = '19h = 247 → h = 13'
ANSWER = '13 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A trapezoid has parallel sides of {0} cm and {1} cm and an area of {2} cm². Find its height.'
NUMBERS = ['19', '19', '247']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

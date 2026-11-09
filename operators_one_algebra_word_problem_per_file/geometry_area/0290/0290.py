"""Algebra word problem 0290   [Geometry (area)]

Problem : A trapezoid has parallel sides of 11 cm and 11 cm and an area of 66 cm². Find its height.
Let     : h = height
Equation: (1/2)(11 + 11)h = 66
Solve   : 11h = 66 → h = 6
Answer  : 6 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0290'
KEY = 'geometry_area/0290'
NAME = 'Geometry (area) 0290'
CATEGORY = 'Geometry (area)'
PROBLEM = 'A trapezoid has parallel sides of 11 cm and 11 cm and an area of 66 cm². Find its height.'
LET = 'h = height'
EQUATION = '(1/2)(11 + 11)h = 66'
SOLVE = '11h = 66 → h = 6'
ANSWER = '6 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A trapezoid has parallel sides of {0} cm and {1} cm and an area of {2} cm². Find its height.'
NUMBERS = ['11', '11', '66']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

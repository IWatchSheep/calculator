"""Algebra word problem 0277   [Geometry (area)]

Problem : A triangle has an area of 60 m² and a height of 3 m. How long is its base?
Let     : b = base
Equation: (1/2)b(3) = 60
Solve   : 1.5b = 60 → b = 40
Answer  : 40 m

Status  : ready: archive_geometry_area_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0277'
KEY = 'geometry_area/0277'
NAME = 'Geometry (area) 0277'
CATEGORY = 'Geometry (area)'
PROBLEM = 'A triangle has an area of 60 m² and a height of 3 m. How long is its base?'
LET = 'b = base'
EQUATION = '(1/2)b(3) = 60'
SOLVE = '1.5b = 60 → b = 40'
ANSWER = '40 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_area_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A triangle has an area of {0} m² and a height of {1} m. How long is its base?'
NUMBERS = ['60', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0288   [Geometry (area)]

Problem : A triangle has an area of 87 m² and a height of 29 m. How long is its base?
Let     : b = base
Equation: (1/2)b(29) = 87
Solve   : 14.5b = 87 → b = 6
Answer  : 6 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0288'
KEY = 'geometry_area/0288'
NAME = 'Geometry (area) 0288'
CATEGORY = 'Geometry (area)'
PROBLEM = 'A triangle has an area of 87 m² and a height of 29 m. How long is its base?'
LET = 'b = base'
EQUATION = '(1/2)b(29) = 87'
SOLVE = '14.5b = 87 → b = 6'
ANSWER = '6 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A triangle has an area of {0} m² and a height of {1} m. How long is its base?'
NUMBERS = ['87', '29']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

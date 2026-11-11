"""Algebra word problem 0295   [Geometry (perimeter)]

Problem : A window is a rectangle 18 ft tall topped by an equilateral triangle. The triangle's sides equal the rectangle's width. The outside perimeter is 66 ft. How wide is the window?
Let     : w = width
Equation: w + 2(18) + 2w = 66
Solve   : 3w = 30 → w = 10
Answer  : 10 ft

Status  : ready: archive_geometry_perimeter_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0295'
KEY = 'geometry_perimeter/0295'
NAME = 'Geometry (perimeter) 0295'
CATEGORY = 'Geometry (perimeter)'
PROBLEM = "A window is a rectangle 18 ft tall topped by an equilateral triangle. The triangle's sides equal the rectangle's width. The outside perimeter is 66 ft. How wide is the window?"
LET = 'w = width'
EQUATION = 'w + 2(18) + 2w = 66'
SOLVE = '3w = 30 → w = 10'
ANSWER = '10 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_perimeter_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A window is a rectangle {0} ft tall topped by an equilateral triangle. The triangle's sides equal the rectangle's width. The outside perimeter is {1} ft. How wide is the window?"
NUMBERS = ['18', '66']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

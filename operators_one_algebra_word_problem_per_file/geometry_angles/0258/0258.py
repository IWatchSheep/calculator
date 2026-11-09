"""Algebra word problem 0258   [Geometry (angles)]

Problem : The angles of a triangle are in the ratio 2:6:7. Find each angle.
Let     : x = scale factor
Equation: 2x + 6x + 7x = 180
Solve   : 15x = 180 → x = 12
Answer  : 24°, 72°, 84°

Status  : ready: triangle_ratio answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0258'
KEY = 'geometry_angles/0258'
NAME = 'Geometry (angles) 0258'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'The angles of a triangle are in the ratio 2:6:7. Find each angle.'
LET = 'x = scale factor'
EQUATION = '2x + 6x + 7x = 180'
SOLVE = '15x = 180 → x = 12'
ANSWER = '24°, 72°, 84°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'triangle_ratio'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The angles of a triangle are in the ratio {0}:{1}:{2}. Find each angle.'
NUMBERS = ['2', '6', '7']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

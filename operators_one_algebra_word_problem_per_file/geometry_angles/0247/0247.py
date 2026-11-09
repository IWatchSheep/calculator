"""Algebra word problem 0247   [Geometry (angles)]

Problem : The angles of a triangle are in the ratio 5:6:7. Find each angle.
Let     : x = scale factor
Equation: 5x + 6x + 7x = 180
Solve   : 18x = 180 → x = 10
Answer  : 50°, 60°, 70°

Status  : ready: triangle_ratio answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0247'
KEY = 'geometry_angles/0247'
NAME = 'Geometry (angles) 0247'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'The angles of a triangle are in the ratio 5:6:7. Find each angle.'
LET = 'x = scale factor'
EQUATION = '5x + 6x + 7x = 180'
SOLVE = '18x = 180 → x = 10'
ANSWER = '50°, 60°, 70°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'triangle_ratio'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The angles of a triangle are in the ratio {0}:{1}:{2}. Find each angle.'
NUMBERS = ['5', '6', '7']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

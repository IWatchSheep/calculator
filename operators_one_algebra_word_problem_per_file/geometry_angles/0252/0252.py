"""Algebra word problem 0252   [Geometry (angles)]

Problem : Where two lines cross, opposite angles are (3x − 10)° and (6x − 118)°. Find the angle.
Let     : x = unknown
Equation: 3x − 10 = 6x − 118
Solve   : 3x = 108 → x = 36
Answer  : x = 36; each angle is 98°

Status  : ready: opposite_angles_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0252'
KEY = 'geometry_angles/0252'
NAME = 'Geometry (angles) 0252'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Where two lines cross, opposite angles are (3x − 10)° and (6x − 118)°. Find the angle.'
LET = 'x = unknown'
EQUATION = '3x − 10 = 6x − 118'
SOLVE = '3x = 108 → x = 36'
ANSWER = 'x = 36; each angle is 98°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'opposite_angles_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Where two lines cross, opposite angles are ({0}x − {1})° and ({2}x − {3})°. Find the angle.'
NUMBERS = ['3', '10', '6', '118']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

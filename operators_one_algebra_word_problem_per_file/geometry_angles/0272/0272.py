"""Algebra word problem 0272   [Geometry (angles)]

Problem : Where two lines cross, opposite angles are (3x + 17)° and (4x − 16)°. Find the angle.
Let     : x = unknown
Equation: 3x + 17 = 4x − 16
Solve   : Collect like terms → x = 33
Answer  : x = 33; each angle is 116°

Status  : ready: opposite_angles_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0272'
KEY = 'geometry_angles/0272'
NAME = 'Geometry (angles) 0272'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Where two lines cross, opposite angles are (3x + 17)° and (4x − 16)°. Find the angle.'
LET = 'x = unknown'
EQUATION = '3x + 17 = 4x − 16'
SOLVE = 'Collect like terms → x = 33'
ANSWER = 'x = 33; each angle is 116°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'opposite_angles_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Where two lines cross, opposite angles are ({0}x + {1})° and ({2}x − {3})°. Find the angle.'
NUMBERS = ['3', '17', '4', '16']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

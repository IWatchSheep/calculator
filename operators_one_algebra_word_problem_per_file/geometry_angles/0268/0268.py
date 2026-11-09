"""Algebra word problem 0268   [Geometry (angles)]

Problem : Two parallel lines are cut by a transversal. A pair of alternate exterior angles measure (3x + 32)° and (1x + 66)°. Find x and the angle.
Let     : x = unknown
Equation: 3x + 32 = x + 66
Solve   : 2x = 34 → x = 17
Answer  : x = 17; each angle is 83°

Status  : ready: transversal_equal_angles answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0268'
KEY = 'geometry_angles/0268'
NAME = 'Geometry (angles) 0268'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Two parallel lines are cut by a transversal. A pair of alternate exterior angles measure (3x + 32)° and (1x + 66)°. Find x and the angle.'
LET = 'x = unknown'
EQUATION = '3x + 32 = x + 66'
SOLVE = '2x = 34 → x = 17'
ANSWER = 'x = 17; each angle is 83°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'transversal_equal_angles'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two parallel lines are cut by a transversal. A pair of alternate exterior angles measure ({0}x + {1})° and ({2}x + {3})°. Find x and the angle.'
NUMBERS = ['3', '32', '1', '66']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

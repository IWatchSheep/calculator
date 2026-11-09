"""Algebra word problem 0273   [Geometry (angles)]

Problem : Two parallel lines are cut by a transversal. A pair of alternate interior angles measure (2x + 1)° and (1x + 33)°. Find x and the angle.
Let     : x = unknown
Equation: 2x + 1 = x + 33
Solve   : Collect like terms → x = 32
Answer  : x = 32; each angle is 65°

Status  : ready: transversal_equal_angles answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0273'
KEY = 'geometry_angles/0273'
NAME = 'Geometry (angles) 0273'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Two parallel lines are cut by a transversal. A pair of alternate interior angles measure (2x + 1)° and (1x + 33)°. Find x and the angle.'
LET = 'x = unknown'
EQUATION = '2x + 1 = x + 33'
SOLVE = 'Collect like terms → x = 32'
ANSWER = 'x = 32; each angle is 65°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'transversal_equal_angles'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two parallel lines are cut by a transversal. A pair of alternate interior angles measure ({0}x + {1})° and ({2}x + {3})°. Find x and the angle.'
NUMBERS = ['2', '1', '1', '33']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

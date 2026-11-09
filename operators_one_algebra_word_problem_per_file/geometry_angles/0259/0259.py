"""Algebra word problem 0259   [Geometry (angles)]

Problem : Two angles are complementary. One angle is 15 more than 4 times the other. Find both angles.
Let     : x = smaller angle
Equation: x + (4x + 15) = 90
Solve   : 5x = 75 → x = 15
Answer  : 15° and 75°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0259'
KEY = 'geometry_angles/0259'
NAME = 'Geometry (angles) 0259'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Two angles are complementary. One angle is 15 more than 4 times the other. Find both angles.'
LET = 'x = smaller angle'
EQUATION = 'x + (4x + 15) = 90'
SOLVE = '5x = 75 → x = 15'
ANSWER = '15° and 75°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two angles are complementary. One angle is {0} more than {1} times the other. Find both angles.'
NUMBERS = ['15', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

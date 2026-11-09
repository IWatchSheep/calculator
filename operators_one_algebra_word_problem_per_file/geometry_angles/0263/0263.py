"""Algebra word problem 0263   [Geometry (angles)]

Problem : Two angles are supplementary. One angle is 6 less than 5 times the other. Find both angles.
Let     : x = smaller angle
Equation: x + (5x − 6) = 180
Solve   : 6x = 186 → x = 31
Answer  : 31° and 149°

Status  : ready: complementary_supplementary answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0263'
KEY = 'geometry_angles/0263'
NAME = 'Geometry (angles) 0263'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Two angles are supplementary. One angle is 6 less than 5 times the other. Find both angles.'
LET = 'x = smaller angle'
EQUATION = 'x + (5x − 6) = 180'
SOLVE = '6x = 186 → x = 31'
ANSWER = '31° and 149°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'complementary_supplementary'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two angles are supplementary. One angle is {0} less than {1} times the other. Find both angles.'
NUMBERS = ['6', '5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

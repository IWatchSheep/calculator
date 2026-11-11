"""Algebra word problem 0243   [Geometry (angles)]

Problem : In a triangle, the second angle is 3 times the first, and the third angle is 75 more than the first. Find all three angles.
Let     : x = first angle
Equation: x + 3x + (x + 75) = 180
Solve   : 5x + 75 = 180 → x = 21
Answer  : 21°, 63°, 96°

Status  : ready: archive_geometry_angles_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0243'
KEY = 'geometry_angles/0243'
NAME = 'Geometry (angles) 0243'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'In a triangle, the second angle is 3 times the first, and the third angle is 75 more than the first. Find all three angles.'
LET = 'x = first angle'
EQUATION = 'x + 3x + (x + 75) = 180'
SOLVE = '5x + 75 = 180 → x = 21'
ANSWER = '21°, 63°, 96°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_angles_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In a triangle, the second angle is {0} times the first, and the third angle is {1} more than the first. Find all three angles.'
NUMBERS = ['3', '75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

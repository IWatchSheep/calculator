"""Algebra word problem 0267   [Geometry (angles)]

Problem : In a triangle, the second angle is 2 times the first, and the third angle is 40 more than the first. Find all three angles.
Let     : x = first angle
Equation: x + 2x + (x + 40) = 180
Solve   : 4x + 40 = 180 → x = 35
Answer  : 35°, 70°, 75°

Status  : ready: archive_geometry_angles_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0267'
KEY = 'geometry_angles/0267'
NAME = 'Geometry (angles) 0267'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'In a triangle, the second angle is 2 times the first, and the third angle is 40 more than the first. Find all three angles.'
LET = 'x = first angle'
EQUATION = 'x + 2x + (x + 40) = 180'
SOLVE = '4x + 40 = 180 → x = 35'
ANSWER = '35°, 70°, 75°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_angles_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In a triangle, the second angle is {0} times the first, and the third angle is {1} more than the first. Find all three angles.'
NUMBERS = ['2', '40']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

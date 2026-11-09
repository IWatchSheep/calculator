"""Algebra word problem 0246   [Geometry (angles)]

Problem : In an isosceles triangle, the vertex angle is 72° more than each base angle. Find all three angles.
Let     : x = each base angle
Equation: x + x + (x + 72) = 180
Solve   : 3x = 108 → x = 36
Answer  : 36°, 36°, 108°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0246'
KEY = 'geometry_angles/0246'
NAME = 'Geometry (angles) 0246'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'In an isosceles triangle, the vertex angle is 72° more than each base angle. Find all three angles.'
LET = 'x = each base angle'
EQUATION = 'x + x + (x + 72) = 180'
SOLVE = '3x = 108 → x = 36'
ANSWER = '36°, 36°, 108°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In an isosceles triangle, the vertex angle is {0}° more than each base angle. Find all three angles.'
NUMBERS = ['72']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

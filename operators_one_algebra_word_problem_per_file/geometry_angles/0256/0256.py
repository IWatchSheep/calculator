"""Algebra word problem 0256   [Geometry (angles)]

Problem : In an isosceles triangle, the vertex angle is 12° less than each base angle. Find all three angles.
Let     : x = each base angle
Equation: x + x + (x − 12) = 180
Solve   : 3x = 192 → x = 64
Answer  : 64°, 64°, 52°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0256'
KEY = 'geometry_angles/0256'
NAME = 'Geometry (angles) 0256'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'In an isosceles triangle, the vertex angle is 12° less than each base angle. Find all three angles.'
LET = 'x = each base angle'
EQUATION = 'x + x + (x − 12) = 180'
SOLVE = '3x = 192 → x = 64'
ANSWER = '64°, 64°, 52°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In an isosceles triangle, the vertex angle is {0}° less than each base angle. Find all three angles.'
NUMBERS = ['12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

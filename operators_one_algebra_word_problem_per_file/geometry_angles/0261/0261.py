"""Algebra word problem 0261   [Geometry (angles)]

Problem : An exterior angle of a triangle measures (7x + 38)°. The two remote interior angles measure (4x + 15)° and (5x − 3)°. Find x and the exterior angle.
Let     : x = unknown
Equation: (4x + 15) + (5x − 3) = 7x + 38
Solve   : 2x = 26 → x = 13
Answer  : x = 13; exterior angle = 129°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0261'
KEY = 'geometry_angles/0261'
NAME = 'Geometry (angles) 0261'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'An exterior angle of a triangle measures (7x + 38)°. The two remote interior angles measure (4x + 15)° and (5x − 3)°. Find x and the exterior angle.'
LET = 'x = unknown'
EQUATION = '(4x + 15) + (5x − 3) = 7x + 38'
SOLVE = '2x = 26 → x = 13'
ANSWER = 'x = 13; exterior angle = 129°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An exterior angle of a triangle measures ({0}x + {1})°. The two remote interior angles measure ({2}x + {3})° and ({4}x − {5})°. Find x and the exterior angle.'
NUMBERS = ['7', '38', '4', '15', '5', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

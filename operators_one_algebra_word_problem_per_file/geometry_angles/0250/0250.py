"""Algebra word problem 0250   [Geometry (angles)]

Problem : An exterior angle of a triangle measures (1x + 55)°. The two remote interior angles measure (1x + 18)° and (2x − 5)°. Find x and the exterior angle.
Let     : x = unknown
Equation: (x + 18) + (2x − 5) = x + 55
Solve   : 2x = 42 → x = 21
Answer  : x = 21; exterior angle = 76°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0250'
KEY = 'geometry_angles/0250'
NAME = 'Geometry (angles) 0250'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'An exterior angle of a triangle measures (1x + 55)°. The two remote interior angles measure (1x + 18)° and (2x − 5)°. Find x and the exterior angle.'
LET = 'x = unknown'
EQUATION = '(x + 18) + (2x − 5) = x + 55'
SOLVE = '2x = 42 → x = 21'
ANSWER = 'x = 21; exterior angle = 76°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An exterior angle of a triangle measures ({0}x + {1})°. The two remote interior angles measure ({2}x + {3})° and ({4}x − {5})°. Find x and the exterior angle.'
NUMBERS = ['1', '55', '1', '18', '2', '5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

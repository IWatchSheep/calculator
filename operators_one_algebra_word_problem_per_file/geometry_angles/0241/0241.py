"""Algebra word problem 0241   [Geometry (angles)]

Problem : Two angles form a linear pair. One measures (4x + 29)° and the other (1x + 41)°. Find both angles.
Let     : x = unknown
Equation: (4x + 29) + (x + 41) = 180
Solve   : 5x = 110 → x = 22
Answer  : x = 22; the angles are 117° and 63°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0241'
KEY = 'geometry_angles/0241'
NAME = 'Geometry (angles) 0241'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Two angles form a linear pair. One measures (4x + 29)° and the other (1x + 41)°. Find both angles.'
LET = 'x = unknown'
EQUATION = '(4x + 29) + (x + 41) = 180'
SOLVE = '5x = 110 → x = 22'
ANSWER = 'x = 22; the angles are 117° and 63°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two angles form a linear pair. One measures ({0}x + {1})° and the other ({2}x + {3})°. Find both angles.'
NUMBERS = ['4', '29', '1', '41']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

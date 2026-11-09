"""Algebra word problem 0253   [Geometry (angles)]

Problem : Two vertical angles measure (6x − 13)° and (4x + 17)°. Find x and the angle measure.
Let     : x = unknown
Equation: 6x − 13 = 4x + 17
Solve   : 2x = 30 → x = 15
Answer  : x = 15; each angle is 77°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0253'
KEY = 'geometry_angles/0253'
NAME = 'Geometry (angles) 0253'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Two vertical angles measure (6x − 13)° and (4x + 17)°. Find x and the angle measure.'
LET = 'x = unknown'
EQUATION = '6x − 13 = 4x + 17'
SOLVE = '2x = 30 → x = 15'
ANSWER = 'x = 15; each angle is 77°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two vertical angles measure ({0}x − {1})° and ({2}x + {3})°. Find x and the angle measure.'
NUMBERS = ['6', '13', '4', '17']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

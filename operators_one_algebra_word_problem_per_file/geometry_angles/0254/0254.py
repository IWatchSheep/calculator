"""Algebra word problem 0254   [Geometry (angles)]

Problem : Angles A and B lie on a straight line. A = (1x + 2)° and B = (3x + 138)°. What are A and B?
Let     : x = unknown
Equation: (x + 2) + (3x + 138) = 180
Solve   : 4x = 40 → x = 10
Answer  : x = 10; the angles are 12° and 168°

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0254'
KEY = 'geometry_angles/0254'
NAME = 'Geometry (angles) 0254'
CATEGORY = 'Geometry (angles)'
PROBLEM = 'Angles A and B lie on a straight line. A = (1x + 2)° and B = (3x + 138)°. What are A and B?'
LET = 'x = unknown'
EQUATION = '(x + 2) + (3x + 138) = 180'
SOLVE = '4x = 40 → x = 10'
ANSWER = 'x = 10; the angles are 12° and 168°'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Angles A and B lie on a straight line. A = ({0}x + {1})° and B = ({2}x + {3})°. What are A and B?'
NUMBERS = ['1', '2', '3', '138']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

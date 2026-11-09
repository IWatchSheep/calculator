"""Algebra word problem 0296   [Geometry (perimeter)]

Problem : Each side of a square is (1x + 16) cm. The perimeter is 72 cm. Find x and the side length.
Let     : x = unknown
Equation: 4(x + 16) = 72
Solve   : 4x = 8 → x = 2
Answer  : x = 2; side = 18 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0296'
KEY = 'geometry_perimeter/0296'
NAME = 'Geometry (perimeter) 0296'
CATEGORY = 'Geometry (perimeter)'
PROBLEM = 'Each side of a square is (1x + 16) cm. The perimeter is 72 cm. Find x and the side length.'
LET = 'x = unknown'
EQUATION = '4(x + 16) = 72'
SOLVE = '4x = 8 → x = 2'
ANSWER = 'x = 2; side = 18 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Each side of a square is ({0}x + {1}) cm. The perimeter is {2} cm. Find x and the side length.'
NUMBERS = ['1', '16', '72']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

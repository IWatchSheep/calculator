"""Algebra word problem 0327   [Geometry (quadratic)]

Problem : Squares of side x are cut from each corner of a 24 cm by 19 cm sheet, and the sides are folded up to make an open box. The base of the box has area 126 cm². Find x.
Let     : x = side of each cut square
Equation: (24 − 2x)(19 − 2x) = 126
Solve   : 2x² − 43x + 165 = 0 → x = 5 (the other root, 16.5, is rejected)
Answer  : 5 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0327'
KEY = 'geometry_quadratic/0327'
NAME = 'Geometry (quadratic) 0327'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'Squares of side x are cut from each corner of a 24 cm by 19 cm sheet, and the sides are folded up to make an open box. The base of the box has area 126 cm². Find x.'
LET = 'x = side of each cut square'
EQUATION = '(24 − 2x)(19 − 2x) = 126'
SOLVE = '2x² − 43x + 165 = 0 → x = 5 (the other root, 16.5, is rejected)'
ANSWER = '5 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Squares of side x are cut from each corner of a {0} cm by {1} cm sheet, and the sides are folded up to make an open box. The base of the box has area {2} cm². Find x.'
NUMBERS = ['24', '19', '126']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

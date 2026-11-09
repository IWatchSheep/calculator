"""Algebra word problem 0337   [Geometry (quadratic)]

Problem : Squares of side x are cut from each corner of a 26 cm by 13 cm sheet, and the sides are folded up to make an open box. The base of the box has area 48 cm². Find x.
Let     : x = side of each cut square
Equation: (26 − 2x)(13 − 2x) = 48
Solve   : 2x² − 39x + 145 = 0 → x = 5 (the other root, 14.5, is rejected)
Answer  : 5 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0337'
KEY = 'geometry_quadratic/0337'
NAME = 'Geometry (quadratic) 0337'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'Squares of side x are cut from each corner of a 26 cm by 13 cm sheet, and the sides are folded up to make an open box. The base of the box has area 48 cm². Find x.'
LET = 'x = side of each cut square'
EQUATION = '(26 − 2x)(13 − 2x) = 48'
SOLVE = '2x² − 39x + 145 = 0 → x = 5 (the other root, 14.5, is rejected)'
ANSWER = '5 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Squares of side x are cut from each corner of a {0} cm by {1} cm sheet, and the sides are folded up to make an open box. The base of the box has area {2} cm². Find x.'
NUMBERS = ['26', '13', '48']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

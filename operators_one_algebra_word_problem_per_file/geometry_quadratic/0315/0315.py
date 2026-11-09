"""Algebra word problem 0315   [Geometry (quadratic)]

Problem : A 18 in × 15 in photo is surrounded by a frame of uniform width. The framed picture covers 418 in². How wide is the frame?
Let     : x = frame width
Equation: (18 + 2x)(15 + 2x) = 418
Solve   : 2x² + 33x − 74 = 0 → x = 2 (the other root, -18.5, is rejected)
Answer  : 2 in

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0315'
KEY = 'geometry_quadratic/0315'
NAME = 'Geometry (quadratic) 0315'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A 18 in × 15 in photo is surrounded by a frame of uniform width. The framed picture covers 418 in². How wide is the frame?'
LET = 'x = frame width'
EQUATION = '(18 + 2x)(15 + 2x) = 418'
SOLVE = '2x² + 33x − 74 = 0 → x = 2 (the other root, -18.5, is rejected)'
ANSWER = '2 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} in × {1} in photo is surrounded by a frame of uniform width. The framed picture covers {2} in². How wide is the frame?'
NUMBERS = ['18', '15', '418']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

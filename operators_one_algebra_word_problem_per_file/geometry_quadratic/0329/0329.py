"""Algebra word problem 0329   [Geometry (quadratic)]

Problem : A 12 in × 20 in photo is surrounded by a frame of uniform width. The framed picture covers 468 in². How wide is the frame?
Let     : x = frame width
Equation: (12 + 2x)(20 + 2x) = 468
Solve   : x² + 16x − 57 = 0 → x = 3 (the other root, -19, is rejected)
Answer  : 3 in

Status  : ready: archive_geometry_quadratic_3 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0329'
KEY = 'geometry_quadratic/0329'
NAME = 'Geometry (quadratic) 0329'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A 12 in × 20 in photo is surrounded by a frame of uniform width. The framed picture covers 468 in². How wide is the frame?'
LET = 'x = frame width'
EQUATION = '(12 + 2x)(20 + 2x) = 468'
SOLVE = 'x² + 16x − 57 = 0 → x = 3 (the other root, -19, is rejected)'
ANSWER = '3 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_quadratic_3'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} in × {1} in photo is surrounded by a frame of uniform width. The framed picture covers {2} in². How wide is the frame?'
NUMBERS = ['12', '20', '468']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

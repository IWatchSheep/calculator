"""Algebra word problem 0321   [Geometry (quadratic)]

Problem : A 19 in × 16 in photo is surrounded by a frame of uniform width. The framed picture covers 460 in². How wide is the frame?
Let     : x = frame width
Equation: (19 + 2x)(16 + 2x) = 460
Solve   : 2x² + 35x − 78 = 0 → x = 2 (the other root, -19.5, is rejected)
Answer  : 2 in

Status  : ready: archive_geometry_quadratic_3 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0321'
KEY = 'geometry_quadratic/0321'
NAME = 'Geometry (quadratic) 0321'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A 19 in × 16 in photo is surrounded by a frame of uniform width. The framed picture covers 460 in². How wide is the frame?'
LET = 'x = frame width'
EQUATION = '(19 + 2x)(16 + 2x) = 460'
SOLVE = '2x² + 35x − 78 = 0 → x = 2 (the other root, -19.5, is rejected)'
ANSWER = '2 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_quadratic_3'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} in × {1} in photo is surrounded by a frame of uniform width. The framed picture covers {2} in². How wide is the frame?'
NUMBERS = ['19', '16', '460']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

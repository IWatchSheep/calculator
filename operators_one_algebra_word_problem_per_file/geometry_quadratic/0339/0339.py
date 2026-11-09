"""Algebra word problem 0339   [Geometry (quadratic)]

Problem : A 9 in × 5 in photo is surrounded by a frame of uniform width. The framed picture covers 117 in². How wide is the frame?
Let     : x = frame width
Equation: (9 + 2x)(5 + 2x) = 117
Solve   : x² + 7x − 18 = 0 → x = 2 (the other root, -9, is rejected)
Answer  : 2 in

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0339'
KEY = 'geometry_quadratic/0339'
NAME = 'Geometry (quadratic) 0339'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A 9 in × 5 in photo is surrounded by a frame of uniform width. The framed picture covers 117 in². How wide is the frame?'
LET = 'x = frame width'
EQUATION = '(9 + 2x)(5 + 2x) = 117'
SOLVE = 'x² + 7x − 18 = 0 → x = 2 (the other root, -9, is rejected)'
ANSWER = '2 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} in × {1} in photo is surrounded by a frame of uniform width. The framed picture covers {2} in². How wide is the frame?'
NUMBERS = ['9', '5', '117']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

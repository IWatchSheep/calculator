"""Algebra word problem 0317   [Geometry (quadratic)]

Problem : A 10 ft by 15 ft garden has a path of uniform width around it. The path's area is 54 ft². How wide is the path?
Let     : x = path width
Equation: (10 + 2x)(15 + 2x) − 150 = 54
Solve   : 4x² + 50x − 54 = 0 → x = 1 (reject negative)
Answer  : 1 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0317'
KEY = 'geometry_quadratic/0317'
NAME = 'Geometry (quadratic) 0317'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = "A 10 ft by 15 ft garden has a path of uniform width around it. The path's area is 54 ft². How wide is the path?"
LET = 'x = path width'
EQUATION = '(10 + 2x)(15 + 2x) − 150 = 54'
SOLVE = '4x² + 50x − 54 = 0 → x = 1 (reject negative)'
ANSWER = '1 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A {0} ft by {1} ft garden has a path of uniform width around it. The path's area is {2} ft². How wide is the path?"
NUMBERS = ['10', '15', '54']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

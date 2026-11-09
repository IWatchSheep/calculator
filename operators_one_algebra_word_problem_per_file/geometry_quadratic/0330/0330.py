"""Algebra word problem 0330   [Geometry (quadratic)]

Problem : A 5 ft by 13 ft garden has a path of uniform width around it. The path's area is 280 ft². How wide is the path?
Let     : x = path width
Equation: (5 + 2x)(13 + 2x) − 65 = 280
Solve   : 4x² + 36x − 280 = 0 → x = 5 (reject negative)
Answer  : 5 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0330'
KEY = 'geometry_quadratic/0330'
NAME = 'Geometry (quadratic) 0330'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = "A 5 ft by 13 ft garden has a path of uniform width around it. The path's area is 280 ft². How wide is the path?"
LET = 'x = path width'
EQUATION = '(5 + 2x)(13 + 2x) − 65 = 280'
SOLVE = '4x² + 36x − 280 = 0 → x = 5 (reject negative)'
ANSWER = '5 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A {0} ft by {1} ft garden has a path of uniform width around it. The path's area is {2} ft². How wide is the path?"
NUMBERS = ['5', '13', '280']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

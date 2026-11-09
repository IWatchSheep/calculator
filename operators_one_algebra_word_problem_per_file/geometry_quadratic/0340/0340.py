"""Algebra word problem 0340   [Geometry (quadratic)]

Problem : A 7 ft by 17 ft garden has a path of uniform width around it. The path's area is 112 ft². How wide is the path?
Let     : x = path width
Equation: (7 + 2x)(17 + 2x) − 119 = 112
Solve   : 4x² + 48x − 112 = 0 → x = 2 (reject negative)
Answer  : 2 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0340'
KEY = 'geometry_quadratic/0340'
NAME = 'Geometry (quadratic) 0340'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = "A 7 ft by 17 ft garden has a path of uniform width around it. The path's area is 112 ft². How wide is the path?"
LET = 'x = path width'
EQUATION = '(7 + 2x)(17 + 2x) − 119 = 112'
SOLVE = '4x² + 48x − 112 = 0 → x = 2 (reject negative)'
ANSWER = '2 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A {0} ft by {1} ft garden has a path of uniform width around it. The path's area is {2} ft². How wide is the path?"
NUMBERS = ['7', '17', '112']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0328   [Geometry (quadratic)]

Problem : The height of a triangle is 6 cm more than its base. The area is 56 cm². Find the base and height.
Let     : b = base
Equation: (1/2)b(b + 6) = 56
Solve   : b² + 6b − 112 = 0 → b = 8 (the other root, -14, is rejected)
Answer  : Base 8 cm, height 14 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0328'
KEY = 'geometry_quadratic/0328'
NAME = 'Geometry (quadratic) 0328'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'The height of a triangle is 6 cm more than its base. The area is 56 cm². Find the base and height.'
LET = 'b = base'
EQUATION = '(1/2)b(b + 6) = 56'
SOLVE = 'b² + 6b − 112 = 0 → b = 8 (the other root, -14, is rejected)'
ANSWER = 'Base 8 cm, height 14 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The height of a triangle is {0} cm more than its base. The area is {1} cm². Find the base and height.'
NUMBERS = ['6', '56']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

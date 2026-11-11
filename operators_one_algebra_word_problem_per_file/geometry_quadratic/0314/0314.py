"""Algebra word problem 0314   [Geometry (quadratic)]

Problem : The height of a triangle is 9 cm more than its base. The area is 243 cm². Find the base and height.
Let     : b = base
Equation: (1/2)b(b + 9) = 243
Solve   : b² + 9b − 486 = 0 → b = 18 (the other root, -27, is rejected)
Answer  : Base 18 cm, height 27 cm

Status  : ready: archive_geometry_quadratic_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0314'
KEY = 'geometry_quadratic/0314'
NAME = 'Geometry (quadratic) 0314'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'The height of a triangle is 9 cm more than its base. The area is 243 cm². Find the base and height.'
LET = 'b = base'
EQUATION = '(1/2)b(b + 9) = 243'
SOLVE = 'b² + 9b − 486 = 0 → b = 18 (the other root, -27, is rejected)'
ANSWER = 'Base 18 cm, height 27 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_quadratic_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The height of a triangle is {0} cm more than its base. The area is {1} cm². Find the base and height.'
NUMBERS = ['9', '243']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

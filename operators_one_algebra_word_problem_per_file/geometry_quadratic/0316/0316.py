"""Algebra word problem 0316   [Geometry (quadratic)]

Problem : The height of a triangle is 8 cm more than its base. The area is 234 cm². Find the base and height.
Let     : b = base
Equation: (1/2)b(b + 8) = 234
Solve   : b² + 8b − 468 = 0 → b = 18 (the other root, -26, is rejected)
Answer  : Base 18 cm, height 26 cm

Status  : ready: archive_geometry_quadratic_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0316'
KEY = 'geometry_quadratic/0316'
NAME = 'Geometry (quadratic) 0316'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'The height of a triangle is 8 cm more than its base. The area is 234 cm². Find the base and height.'
LET = 'b = base'
EQUATION = '(1/2)b(b + 8) = 234'
SOLVE = 'b² + 8b − 468 = 0 → b = 18 (the other root, -26, is rejected)'
ANSWER = 'Base 18 cm, height 26 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_quadratic_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The height of a triangle is {0} cm more than its base. The area is {1} cm². Find the base and height.'
NUMBERS = ['8', '234']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

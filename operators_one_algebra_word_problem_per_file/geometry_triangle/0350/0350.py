"""Algebra word problem 0350   [Geometry (triangle)]

Problem : Each of the two equal sides of an isosceles triangle is 5 cm longer than the base. The perimeter is 67 cm. Find the side lengths.
Let     : x = base
Equation: x + 2(x + 5) = 67
Solve   : 3x + 10 = 67 → x = 19
Answer  : Base 19 cm, equal sides 24 cm

Status  : ready: archive_geometry_triangle_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0350'
KEY = 'geometry_triangle/0350'
NAME = 'Geometry (triangle) 0350'
CATEGORY = 'Geometry (triangle)'
PROBLEM = 'Each of the two equal sides of an isosceles triangle is 5 cm longer than the base. The perimeter is 67 cm. Find the side lengths.'
LET = 'x = base'
EQUATION = 'x + 2(x + 5) = 67'
SOLVE = '3x + 10 = 67 → x = 19'
ANSWER = 'Base 19 cm, equal sides 24 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_triangle_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Each of the two equal sides of an isosceles triangle is {0} cm longer than the base. The perimeter is {1} cm. Find the side lengths.'
NUMBERS = ['5', '67']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

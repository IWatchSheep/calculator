"""Algebra word problem 0352   [Geometry (triangle)]

Problem : Each of the two equal sides of an isosceles triangle is 11 cm longer than the base. The perimeter is 70 cm. Find the side lengths.
Let     : x = base
Equation: x + 2(x + 11) = 70
Solve   : 3x + 22 = 70 → x = 16
Answer  : Base 16 cm, equal sides 27 cm

Status  : ready: archive_geometry_triangle_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0352'
KEY = 'geometry_triangle/0352'
NAME = 'Geometry (triangle) 0352'
CATEGORY = 'Geometry (triangle)'
PROBLEM = 'Each of the two equal sides of an isosceles triangle is 11 cm longer than the base. The perimeter is 70 cm. Find the side lengths.'
LET = 'x = base'
EQUATION = 'x + 2(x + 11) = 70'
SOLVE = '3x + 22 = 70 → x = 16'
ANSWER = 'Base 16 cm, equal sides 27 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_triangle_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Each of the two equal sides of an isosceles triangle is {0} cm longer than the base. The perimeter is {1} cm. Find the side lengths.'
NUMBERS = ['11', '70']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

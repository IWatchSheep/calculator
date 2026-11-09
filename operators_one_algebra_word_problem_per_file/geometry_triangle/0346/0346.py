"""Algebra word problem 0346   [Geometry (triangle)]

Problem : Each of the two equal sides of an isosceles triangle is 2 cm longer than the base. The perimeter is 52 cm. Find the side lengths.
Let     : x = base
Equation: x + 2(x + 2) = 52
Solve   : 3x + 4 = 52 → x = 16
Answer  : Base 16 cm, equal sides 18 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0346'
KEY = 'geometry_triangle/0346'
NAME = 'Geometry (triangle) 0346'
CATEGORY = 'Geometry (triangle)'
PROBLEM = 'Each of the two equal sides of an isosceles triangle is 2 cm longer than the base. The perimeter is 52 cm. Find the side lengths.'
LET = 'x = base'
EQUATION = 'x + 2(x + 2) = 52'
SOLVE = '3x + 4 = 52 → x = 16'
ANSWER = 'Base 16 cm, equal sides 18 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Each of the two equal sides of an isosceles triangle is {0} cm longer than the base. The perimeter is {1} cm. Find the side lengths.'
NUMBERS = ['2', '52']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

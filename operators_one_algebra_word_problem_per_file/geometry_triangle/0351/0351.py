"""Algebra word problem 0351   [Geometry (triangle)]

Problem : A triangle's second side is 6 in longer than the first, and its third side is 7 in less than twice the first. If the perimeter is 95 in, how long is each side?
Let     : x = first side
Equation: x + (x + 6) + (2x − 7) = 95
Solve   : 4x = 96 → x = 24
Answer  : 24 in, 30 in, 41 in

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0351'
KEY = 'geometry_triangle/0351'
NAME = 'Geometry (triangle) 0351'
CATEGORY = 'Geometry (triangle)'
PROBLEM = "A triangle's second side is 6 in longer than the first, and its third side is 7 in less than twice the first. If the perimeter is 95 in, how long is each side?"
LET = 'x = first side'
EQUATION = 'x + (x + 6) + (2x − 7) = 95'
SOLVE = '4x = 96 → x = 24'
ANSWER = '24 in, 30 in, 41 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A triangle's second side is {0} in longer than the first, and its third side is {1} in less than twice the first. If the perimeter is {2} in, how long is each side?"
NUMBERS = ['6', '7', '95']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0354   [Geometry (triangle)]

Problem : The sides of a triangle are x, x + 8, and 2x − 1 inches long. The perimeter is 75 inches. Find each side.
Let     : x = first side
Equation: x + (x + 8) + (2x − 1) = 75
Solve   : 4x = 68 → x = 17
Answer  : 17 in, 25 in, 33 in

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0354'
KEY = 'geometry_triangle/0354'
NAME = 'Geometry (triangle) 0354'
CATEGORY = 'Geometry (triangle)'
PROBLEM = 'The sides of a triangle are x, x + 8, and 2x − 1 inches long. The perimeter is 75 inches. Find each side.'
LET = 'x = first side'
EQUATION = 'x + (x + 8) + (2x − 1) = 75'
SOLVE = '4x = 68 → x = 17'
ANSWER = '17 in, 25 in, 33 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sides of a triangle are x, x + {0}, and {1}x − {2} inches long. The perimeter is {3} inches. Find each side.'
NUMBERS = ['8', '2', '1', '75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

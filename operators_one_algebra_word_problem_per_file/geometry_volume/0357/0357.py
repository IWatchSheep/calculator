"""Algebra word problem 0357   [Geometry (volume)]

Problem : A rectangular box is 20 in long and 4 in wide. Its volume is 400 in³. How tall is it?
Let     : h = height
Equation: 20 × 4 × h = 400
Solve   : 80h = 400 → h = 5
Answer  : 5 in

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0357'
KEY = 'geometry_volume/0357'
NAME = 'Geometry (volume) 0357'
CATEGORY = 'Geometry (volume)'
PROBLEM = 'A rectangular box is 20 in long and 4 in wide. Its volume is 400 in³. How tall is it?'
LET = 'h = height'
EQUATION = '20 × 4 × h = 400'
SOLVE = '80h = 400 → h = 5'
ANSWER = '5 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangular box is {0} in long and {1} in wide. Its volume is {2} in³. How tall is it?'
NUMBERS = ['20', '4', '400']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

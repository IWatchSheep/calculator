"""Algebra word problem 0355   [Geometry (volume)]

Problem : A rectangular box is 16 in long and 5 in wide. Its volume is 320 in³. How tall is it?
Let     : h = height
Equation: 16 × 5 × h = 320
Solve   : 80h = 320 → h = 4
Answer  : 4 in

Status  : ready: archive_geometry_volume_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0355'
KEY = 'geometry_volume/0355'
NAME = 'Geometry (volume) 0355'
CATEGORY = 'Geometry (volume)'
PROBLEM = 'A rectangular box is 16 in long and 5 in wide. Its volume is 320 in³. How tall is it?'
LET = 'h = height'
EQUATION = '16 × 5 × h = 320'
SOLVE = '80h = 320 → h = 4'
ANSWER = '4 in'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_geometry_volume_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangular box is {0} in long and {1} in wide. Its volume is {2} in³. How tall is it?'
NUMBERS = ['16', '5', '320']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

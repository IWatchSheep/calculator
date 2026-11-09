"""Algebra word problem 0133   [Distance (catch-up)]

Problem : Two runners start together on a 300 m track, one at 4 m/s and the other at 6 m/s. After how many seconds does the faster one lap the slower one?
Let     : t = seconds
Equation: 6t − 4t = 300
Solve   : 2t = 300 → t = 150
Answer  : 150 seconds

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0133'
KEY = 'distance_catch_up/0133'
NAME = 'Distance (catch-up) 0133'
CATEGORY = 'Distance (catch-up)'
PROBLEM = 'Two runners start together on a 300 m track, one at 4 m/s and the other at 6 m/s. After how many seconds does the faster one lap the slower one?'
LET = 't = seconds'
EQUATION = '6t − 4t = 300'
SOLVE = '2t = 300 → t = 150'
ANSWER = '150 seconds'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two runners start together on a {0} m track, one at {1} m/s and the other at {2} m/s. After how many seconds does the faster one lap the slower one?'
NUMBERS = ['300', '4', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

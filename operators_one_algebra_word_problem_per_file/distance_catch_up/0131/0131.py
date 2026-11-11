"""Algebra word problem 0131   [Distance (catch-up)]

Problem : Two runners start together on a 200 m track, one at 6 m/s and the other at 7 m/s. After how many seconds does the faster one lap the slower one?
Let     : t = seconds
Equation: 7t − 6t = 200
Solve   : Collect like terms → t = 200
Answer  : 200 seconds

Status  : ready: archive_distance_catch_up_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0131'
KEY = 'distance_catch_up/0131'
NAME = 'Distance (catch-up) 0131'
CATEGORY = 'Distance (catch-up)'
PROBLEM = 'Two runners start together on a 200 m track, one at 6 m/s and the other at 7 m/s. After how many seconds does the faster one lap the slower one?'
LET = 't = seconds'
EQUATION = '7t − 6t = 200'
SOLVE = 'Collect like terms → t = 200'
ANSWER = '200 seconds'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_distance_catch_up_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two runners start together on a {0} m track, one at {1} m/s and the other at {2} m/s. After how many seconds does the faster one lap the slower one?'
NUMBERS = ['200', '6', '7']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

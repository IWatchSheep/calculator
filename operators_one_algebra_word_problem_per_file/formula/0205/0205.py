"""Algebra word problem 0205   [Formula]

Problem : Using distance = speed × time, how long does it take to travel 264 km at 20 km/h?
Let     : t = hours
Equation: 20t = 264
Solve   : 20t = 264 → t = 13.2
Answer  : 13.2 hours

Status  : ready: distance_speed_time answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0205'
KEY = 'formula/0205'
NAME = 'Formula 0205'
CATEGORY = 'Formula'
PROBLEM = 'Using distance = speed × time, how long does it take to travel 264 km at 20 km/h?'
LET = 't = hours'
EQUATION = '20t = 264'
SOLVE = '20t = 264 → t = 13.2'
ANSWER = '13.2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'distance_speed_time'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Using distance = speed × time, how long does it take to travel {0} km at {1} km/h?'
NUMBERS = ['264', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

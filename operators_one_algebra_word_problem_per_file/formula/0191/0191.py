"""Algebra word problem 0191   [Formula]

Problem : Using v = u + at, how long does it take an object to go from 7 m/s to 11 m/s with acceleration 4 m/s²?
Let     : t = seconds
Equation: 7 + 4t = 11
Solve   : 4t = 4 → t = 1
Answer  : 1 second

Status  : ready: kinematics_time answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0191'
KEY = 'formula/0191'
NAME = 'Formula 0191'
CATEGORY = 'Formula'
PROBLEM = 'Using v = u + at, how long does it take an object to go from 7 m/s to 11 m/s with acceleration 4 m/s²?'
LET = 't = seconds'
EQUATION = '7 + 4t = 11'
SOLVE = '4t = 4 → t = 1'
ANSWER = '1 second'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'kinematics_time'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Using v = u + at, how long does it take an object to go from {0} m/s to {1} m/s with acceleration {2} m/s²?'
NUMBERS = ['7', '11', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

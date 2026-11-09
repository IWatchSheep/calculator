"""Algebra word problem 0155   [Distance (toward each other)]

Problem : Two cyclists are 540 km apart and ride toward each other at 51 km/h and 57 km/h. How long until they meet?
Let     : t = hours
Equation: 51t + 57t = 540
Solve   : 108t = 540 → t = 5
Answer  : 5 hours

Status  : ready: toward_each_other answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0155'
KEY = 'distance_toward_each_other/0155'
NAME = 'Distance (toward each other) 0155'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Two cyclists are 540 km apart and ride toward each other at 51 km/h and 57 km/h. How long until they meet?'
LET = 't = hours'
EQUATION = '51t + 57t = 540'
SOLVE = '108t = 540 → t = 5'
ANSWER = '5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'toward_each_other'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two cyclists are {0} km apart and ride toward each other at {1} km/h and {2} km/h. How long until they meet?'
NUMBERS = ['540', '51', '57']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

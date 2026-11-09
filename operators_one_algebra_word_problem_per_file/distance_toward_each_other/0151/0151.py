"""Algebra word problem 0151   [Distance (toward each other)]

Problem : Two cyclists are 198 km apart and ride toward each other at 64 km/h and 35 km/h. How long until they meet?
Let     : t = hours
Equation: 64t + 35t = 198
Solve   : 99t = 198 → t = 2
Answer  : 2 hours

Status  : ready: toward_each_other answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0151'
KEY = 'distance_toward_each_other/0151'
NAME = 'Distance (toward each other) 0151'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Two cyclists are 198 km apart and ride toward each other at 64 km/h and 35 km/h. How long until they meet?'
LET = 't = hours'
EQUATION = '64t + 35t = 198'
SOLVE = '99t = 198 → t = 2'
ANSWER = '2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'toward_each_other'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two cyclists are {0} km apart and ride toward each other at {1} km/h and {2} km/h. How long until they meet?'
NUMBERS = ['198', '64', '35']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

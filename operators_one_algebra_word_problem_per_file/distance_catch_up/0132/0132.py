"""Algebra word problem 0132   [Distance (catch-up)]

Problem : Maya leaves at 38 mph. 3 hours later, Omar follows the same route at 50 mph. How long after Omar leaves will Omar catch up?
Let     : t = hours Omar drives
Equation: 50t = 38(t + 3)
Solve   : 12t = 114 → t = 9.5
Answer  : 9.5 hours

Status  : ready: catch_up answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0132'
KEY = 'distance_catch_up/0132'
NAME = 'Distance (catch-up) 0132'
CATEGORY = 'Distance (catch-up)'
PROBLEM = 'Maya leaves at 38 mph. 3 hours later, Omar follows the same route at 50 mph. How long after Omar leaves will Omar catch up?'
LET = 't = hours Omar drives'
EQUATION = '50t = 38(t + 3)'
SOLVE = '12t = 114 → t = 9.5'
ANSWER = '9.5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'catch_up'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Maya leaves at {0} mph. {1} hours later, Omar follows the same route at {2} mph. How long after Omar leaves will Omar catch up?'
NUMBERS = ['38', '3', '50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

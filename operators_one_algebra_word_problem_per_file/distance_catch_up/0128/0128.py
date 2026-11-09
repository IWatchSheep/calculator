"""Algebra word problem 0128   [Distance (catch-up)]

Problem : Rosa leaves at 39 mph. 1 hour later, Dev follows the same route at 45 mph. How long after Dev leaves will Dev catch up?
Let     : t = hours Dev drives
Equation: 45t = 39(t + 1)
Solve   : 6t = 39 → t = 6.5
Answer  : 6.5 hours

Status  : ready: catch_up answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0128'
KEY = 'distance_catch_up/0128'
NAME = 'Distance (catch-up) 0128'
CATEGORY = 'Distance (catch-up)'
PROBLEM = 'Rosa leaves at 39 mph. 1 hour later, Dev follows the same route at 45 mph. How long after Dev leaves will Dev catch up?'
LET = 't = hours Dev drives'
EQUATION = '45t = 39(t + 1)'
SOLVE = '6t = 39 → t = 6.5'
ANSWER = '6.5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'catch_up'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Rosa leaves at {0} mph. {1} hour later, Dev follows the same route at {2} mph. How long after Dev leaves will Dev catch up?'
NUMBERS = ['39', '1', '45']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

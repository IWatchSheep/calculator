"""Algebra word problem 0130   [Distance (catch-up)]

Problem : Jamal leaves at 38 mph. 1 hour later, Nia follows the same route at 57 mph. How long after Nia leaves will Nia catch up?
Let     : t = hours Nia drives
Equation: 57t = 38(t + 1)
Solve   : 19t = 38 → t = 2
Answer  : 2 hours

Status  : ready: catch_up answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0130'
KEY = 'distance_catch_up/0130'
NAME = 'Distance (catch-up) 0130'
CATEGORY = 'Distance (catch-up)'
PROBLEM = 'Jamal leaves at 38 mph. 1 hour later, Nia follows the same route at 57 mph. How long after Nia leaves will Nia catch up?'
LET = 't = hours Nia drives'
EQUATION = '57t = 38(t + 1)'
SOLVE = '19t = 38 → t = 2'
ANSWER = '2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'catch_up'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Jamal leaves at {0} mph. {1} hour later, Nia follows the same route at {2} mph. How long after Nia leaves will Nia catch up?'
NUMBERS = ['38', '1', '57']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

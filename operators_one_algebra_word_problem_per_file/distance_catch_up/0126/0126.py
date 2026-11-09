"""Algebra word problem 0126   [Distance (catch-up)]

Problem : Caleb leaves at 39 mph. 2 hours later, Aiden follows the same route at 63 mph. How long after Aiden leaves will Aiden catch up?
Let     : t = hours Aiden drives
Equation: 63t = 39(t + 2)
Solve   : 24t = 78 → t = 3.25
Answer  : 3.25 hours

Status  : ready: catch_up answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0126'
KEY = 'distance_catch_up/0126'
NAME = 'Distance (catch-up) 0126'
CATEGORY = 'Distance (catch-up)'
PROBLEM = 'Caleb leaves at 39 mph. 2 hours later, Aiden follows the same route at 63 mph. How long after Aiden leaves will Aiden catch up?'
LET = 't = hours Aiden drives'
EQUATION = '63t = 39(t + 2)'
SOLVE = '24t = 78 → t = 3.25'
ANSWER = '3.25 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'catch_up'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Caleb leaves at {0} mph. {1} hours later, Aiden follows the same route at {2} mph. How long after Aiden leaves will Aiden catch up?'
NUMBERS = ['39', '2', '63']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

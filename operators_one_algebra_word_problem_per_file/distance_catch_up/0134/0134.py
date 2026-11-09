"""Algebra word problem 0134   [Distance (catch-up)]

Problem : Sofia leaves at 47 mph. 3 hours later, Mateo follows the same route at 59 mph. How long after Mateo leaves will Mateo catch up?
Let     : t = hours Mateo drives
Equation: 59t = 47(t + 3)
Solve   : 12t = 141 → t = 11.75
Answer  : 11.75 hours

Status  : ready: catch_up answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0134'
KEY = 'distance_catch_up/0134'
NAME = 'Distance (catch-up) 0134'
CATEGORY = 'Distance (catch-up)'
PROBLEM = 'Sofia leaves at 47 mph. 3 hours later, Mateo follows the same route at 59 mph. How long after Mateo leaves will Mateo catch up?'
LET = 't = hours Mateo drives'
EQUATION = '59t = 47(t + 3)'
SOLVE = '12t = 141 → t = 11.75'
ANSWER = '11.75 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'catch_up'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Sofia leaves at {0} mph. {1} hours later, Mateo follows the same route at {2} mph. How long after Mateo leaves will Mateo catch up?'
NUMBERS = ['47', '3', '59']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

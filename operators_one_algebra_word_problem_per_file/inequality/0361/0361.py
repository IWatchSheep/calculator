"""Algebra word problem 0361   [Inequality]

Problem : The temperature is 26°F and falling 3°F per hour. For how many whole hours will it stay at or above 1°F?
Let     : h = hours
Equation: 26 − 3h ≥ 1
Solve   : h ≤ 25/3 → h = 8 (largest whole number that works)
Answer  : 8 hours

Status  : ready: temperature_whole_hours answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0361'
KEY = 'inequality/0361'
NAME = 'Inequality 0361'
CATEGORY = 'Inequality'
PROBLEM = 'The temperature is 26°F and falling 3°F per hour. For how many whole hours will it stay at or above 1°F?'
LET = 'h = hours'
EQUATION = '26 − 3h ≥ 1'
SOLVE = 'h ≤ 25/3 → h = 8 (largest whole number that works)'
ANSWER = '8 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'temperature_whole_hours'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The temperature is {0}°F and falling {1}°F per hour. For how many whole hours will it stay at or above {2}°F?'
NUMBERS = ['26', '3', '1']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

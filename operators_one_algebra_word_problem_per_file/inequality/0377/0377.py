"""Algebra word problem 0377   [Inequality]

Problem : The temperature is 29°F and falling 4°F per hour. For how many whole hours will it stay at or above 22°F?
Let     : h = hours
Equation: 29 − 4h ≥ 22
Solve   : h ≤ 1.75 → h = 1 (largest whole number that works)
Answer  : 1 hour

Status  : ready: temperature_whole_hours answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0377'
KEY = 'inequality/0377'
NAME = 'Inequality 0377'
CATEGORY = 'Inequality'
PROBLEM = 'The temperature is 29°F and falling 4°F per hour. For how many whole hours will it stay at or above 22°F?'
LET = 'h = hours'
EQUATION = '29 − 4h ≥ 22'
SOLVE = 'h ≤ 1.75 → h = 1 (largest whole number that works)'
ANSWER = '1 hour'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'temperature_whole_hours'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The temperature is {0}°F and falling {1}°F per hour. For how many whole hours will it stay at or above {2}°F?'
NUMBERS = ['29', '4', '22']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0371   [Inequality]

Problem : An elevator holds at most 1200 lb. A 180 lb worker is loading 60 lb boxes. How many boxes can go up with the worker in one trip?
Let     : b = boxes
Equation: 180 + 60b ≤ 1200
Solve   : b ≤ 17 → b = 17 (largest whole number that works)
Answer  : 17 boxes

Status  : ready: most_that_fits answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0371'
KEY = 'inequality/0371'
NAME = 'Inequality 0371'
CATEGORY = 'Inequality'
PROBLEM = 'An elevator holds at most 1200 lb. A 180 lb worker is loading 60 lb boxes. How many boxes can go up with the worker in one trip?'
LET = 'b = boxes'
EQUATION = '180 + 60b ≤ 1200'
SOLVE = 'b ≤ 17 → b = 17 (largest whole number that works)'
ANSWER = '17 boxes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'most_that_fits'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An elevator holds at most {0} lb. A {1} lb worker is loading {2} lb boxes. How many boxes can go up with the worker in one trip?'
NUMBERS = ['1200', '180', '60']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

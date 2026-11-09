"""Algebra word problem 0390   [Inequality]

Problem : An elevator holds at most 1800 lb. A 150 lb worker is loading 50 lb boxes. How many boxes can go up with the worker in one trip?
Let     : b = boxes
Equation: 150 + 50b ≤ 1800
Solve   : b ≤ 33 → b = 33 (largest whole number that works)
Answer  : 33 boxes

Status  : ready: most_that_fits answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0390'
KEY = 'inequality/0390'
NAME = 'Inequality 0390'
CATEGORY = 'Inequality'
PROBLEM = 'An elevator holds at most 1800 lb. A 150 lb worker is loading 50 lb boxes. How many boxes can go up with the worker in one trip?'
LET = 'b = boxes'
EQUATION = '150 + 50b ≤ 1800'
SOLVE = 'b ≤ 33 → b = 33 (largest whole number that works)'
ANSWER = '33 boxes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'most_that_fits'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An elevator holds at most {0} lb. A {1} lb worker is loading {2} lb boxes. How many boxes can go up with the worker in one trip?'
NUMBERS = ['1800', '150', '50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

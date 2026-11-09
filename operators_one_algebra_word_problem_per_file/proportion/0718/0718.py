"""Algebra word problem 0718   [Proportion]

Problem : A cookie recipe needs 4 eggs for 36 cookies. How many eggs for 18 cookies?
Let     : x = eggs
Equation: 4/36 = x/18
Solve   : x/18 = 1/9 → x = 1/9 × 18 = 2
Answer  : 2 eggs

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0718'
KEY = 'proportion/0718'
NAME = 'Proportion 0718'
CATEGORY = 'Proportion'
PROBLEM = 'A cookie recipe needs 4 eggs for 36 cookies. How many eggs for 18 cookies?'
LET = 'x = eggs'
EQUATION = '4/36 = x/18'
SOLVE = 'x/18 = 1/9 → x = 1/9 × 18 = 2'
ANSWER = '2 eggs'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A cookie recipe needs {0} eggs for {1} cookies. How many eggs for {2} cookies?'
NUMBERS = ['4', '36', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0699   [Proportion]

Problem : A cookie recipe needs 4 eggs for 18 cookies. How many eggs for 27 cookies?
Let     : x = eggs
Equation: 4/18 = x/27
Solve   : x/27 = 2/9 → x = 2/9 × 27 = 6
Answer  : 6 eggs

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0699'
KEY = 'proportion/0699'
NAME = 'Proportion 0699'
CATEGORY = 'Proportion'
PROBLEM = 'A cookie recipe needs 4 eggs for 18 cookies. How many eggs for 27 cookies?'
LET = 'x = eggs'
EQUATION = '4/18 = x/27'
SOLVE = 'x/27 = 2/9 → x = 2/9 × 27 = 6'
ANSWER = '6 eggs'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A cookie recipe needs {0} eggs for {1} cookies. How many eggs for {2} cookies?'
NUMBERS = ['4', '18', '27']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

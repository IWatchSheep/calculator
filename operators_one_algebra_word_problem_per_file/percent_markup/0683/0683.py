"""Algebra word problem 0683   [Percent (markup)]

Problem : A store marks up a jacket by 25% and sells it for $425.00. What did the store pay for it?
Let     : c = cost
Equation: 1.25c = 425
Solve   : 1.25c = 425 → c = 340
Answer  : $340.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0683'
KEY = 'percent_markup/0683'
NAME = 'Percent (markup) 0683'
CATEGORY = 'Percent (markup)'
PROBLEM = 'A store marks up a jacket by 25% and sells it for $425.00. What did the store pay for it?'
LET = 'c = cost'
EQUATION = '1.25c = 425'
SOLVE = '1.25c = 425 → c = 340'
ANSWER = '$340.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A store marks up a jacket by {0}% and sells it for ${1}. What did the store pay for it?'
NUMBERS = ['25', '425.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

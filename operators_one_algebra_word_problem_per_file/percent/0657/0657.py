"""Algebra word problem 0657   [Percent]

Problem : 84 out of 240 students passed. What percent passed?
Let     : p = percent
Equation: (p/100)(240) = 84
Solve   : 2.4p = 84 → p = 35
Answer  : 35%

Status  : ready: archive_percent_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0657'
KEY = 'percent/0657'
NAME = 'Percent 0657'
CATEGORY = 'Percent'
PROBLEM = '84 out of 240 students passed. What percent passed?'
LET = 'p = percent'
EQUATION = '(p/100)(240) = 84'
SOLVE = '2.4p = 84 → p = 35'
ANSWER = '35%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_percent_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} out of {1} students passed. What percent passed?'
NUMBERS = ['84', '240']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

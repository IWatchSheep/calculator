"""Algebra word problem 0620   [Percent]

Problem : What percent of 95 is 114?
Let     : p = percent
Equation: (p/100)(95) = 114
Solve   : 0.95p = 114 → p = 120
Answer  : 120%

Status  : ready: archive_percent_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0620'
KEY = 'percent/0620'
NAME = 'Percent 0620'
CATEGORY = 'Percent'
PROBLEM = 'What percent of 95 is 114?'
LET = 'p = percent'
EQUATION = '(p/100)(95) = 114'
SOLVE = '0.95p = 114 → p = 120'
ANSWER = '120%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_percent_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'What percent of {0} is {1}?'
NUMBERS = ['95', '114']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0637   [Percent]

Problem : After a 40% discount, a lamp costs $27.00. What was the original price?
Let     : p = original price
Equation: 0.6p = 27
Solve   : p = 27 ÷ 0.6 = 45
Answer  : $45.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0637'
KEY = 'percent/0637'
NAME = 'Percent 0637'
CATEGORY = 'Percent'
PROBLEM = 'After a 40% discount, a lamp costs $27.00. What was the original price?'
LET = 'p = original price'
EQUATION = '0.6p = 27'
SOLVE = 'p = 27 ÷ 0.6 = 45'
ANSWER = '$45.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'After a {0}% discount, a lamp costs ${1}. What was the original price?'
NUMBERS = ['40', '27.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

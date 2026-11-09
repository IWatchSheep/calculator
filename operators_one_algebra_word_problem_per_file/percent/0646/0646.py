"""Algebra word problem 0646   [Percent]

Problem : The total cost of an item including 10% sales tax is $203.28. What was the price before tax?
Let     : p = pre-tax price
Equation: 1.1p = 203.28
Solve   : p = 203.28 ÷ 1.1 = 184.80
Answer  : $184.80

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0646'
KEY = 'percent/0646'
NAME = 'Percent 0646'
CATEGORY = 'Percent'
PROBLEM = 'The total cost of an item including 10% sales tax is $203.28. What was the price before tax?'
LET = 'p = pre-tax price'
EQUATION = '1.1p = 203.28'
SOLVE = 'p = 203.28 ÷ 1.1 = 184.80'
ANSWER = '$184.80'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The total cost of an item including {0}% sales tax is ${1}. What was the price before tax?'
NUMBERS = ['10', '203.28']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

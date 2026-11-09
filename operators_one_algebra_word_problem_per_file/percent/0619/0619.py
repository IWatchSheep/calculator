"""Algebra word problem 0619   [Percent]

Problem : The total cost of an item including 7.5% sales tax is $46.87. What was the price before tax?
Let     : p = pre-tax price
Equation: 1.075p = 46.87
Solve   : p = 46.87 ÷ 1.075 = 43.60
Answer  : $43.60

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0619'
KEY = 'percent/0619'
NAME = 'Percent 0619'
CATEGORY = 'Percent'
PROBLEM = 'The total cost of an item including 7.5% sales tax is $46.87. What was the price before tax?'
LET = 'p = pre-tax price'
EQUATION = '1.075p = 46.87'
SOLVE = 'p = 46.87 ÷ 1.075 = 43.60'
ANSWER = '$43.60'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The total cost of an item including {0}% sales tax is ${1}. What was the price before tax?'
NUMBERS = ['7.5', '46.87']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

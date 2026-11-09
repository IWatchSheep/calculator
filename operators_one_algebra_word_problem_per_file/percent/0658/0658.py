"""Algebra word problem 0658   [Percent]

Problem : The total cost of an item including 7.5% sales tax is $325.51. What was the price before tax?
Let     : p = pre-tax price
Equation: 1.075p = 325.51
Solve   : p = 325.51 ÷ 1.075 = 302.80
Answer  : $302.80

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0658'
KEY = 'percent/0658'
NAME = 'Percent 0658'
CATEGORY = 'Percent'
PROBLEM = 'The total cost of an item including 7.5% sales tax is $325.51. What was the price before tax?'
LET = 'p = pre-tax price'
EQUATION = '1.075p = 325.51'
SOLVE = 'p = 325.51 ÷ 1.075 = 302.80'
ANSWER = '$302.80'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The total cost of an item including {0}% sales tax is ${1}. What was the price before tax?'
NUMBERS = ['7.5', '325.51']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0663   [Percent]

Problem : After a 5% raise, Hiro's salary is $93,450.00. What was the salary before the raise?
Let     : s = old salary
Equation: 1.05s = 93450
Solve   : s = 93450 ÷ 1.05 = 89000
Answer  : $89,000.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0663'
KEY = 'percent/0663'
NAME = 'Percent 0663'
CATEGORY = 'Percent'
PROBLEM = "After a 5% raise, Hiro's salary is $93,450.00. What was the salary before the raise?"
LET = 's = old salary'
EQUATION = '1.05s = 93450'
SOLVE = 's = 93450 ÷ 1.05 = 89000'
ANSWER = '$89,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "After a {0}% raise, Hiro's salary is ${1}. What was the salary before the raise?"
NUMBERS = ['5', '93450.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

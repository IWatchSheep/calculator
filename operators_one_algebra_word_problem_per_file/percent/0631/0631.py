"""Algebra word problem 0631   [Percent]

Problem : After a 2% raise, Kira's salary is $55,080.00. What was the salary before the raise?
Let     : s = old salary
Equation: 1.02s = 55080
Solve   : s = 55080 ÷ 1.02 = 54000
Answer  : $54,000.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0631'
KEY = 'percent/0631'
NAME = 'Percent 0631'
CATEGORY = 'Percent'
PROBLEM = "After a 2% raise, Kira's salary is $55,080.00. What was the salary before the raise?"
LET = 's = old salary'
EQUATION = '1.02s = 55080'
SOLVE = 's = 55080 ÷ 1.02 = 54000'
ANSWER = '$54,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "After a {0}% raise, Kira's salary is ${1}. What was the salary before the raise?"
NUMBERS = ['2', '55080.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

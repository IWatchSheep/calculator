"""Algebra word problem 0999   [Work rate]

Problem : Dana can clean the house in 15 hours. Priya can do it in 10 hours. How long will it take them working together?
Let     : t = hours together
Equation: t/15 + t/10 = 1
Solve   : t(25)/150 = 1 → t = 150/25
Answer  : 6 hours

Status  : ready: work_together answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0999'
KEY = 'work_rate/0999'
NAME = 'Work rate 0999'
CATEGORY = 'Work rate'
PROBLEM = 'Dana can clean the house in 15 hours. Priya can do it in 10 hours. How long will it take them working together?'
LET = 't = hours together'
EQUATION = 't/15 + t/10 = 1'
SOLVE = 't(25)/150 = 1 → t = 150/25'
ANSWER = '6 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'work_together'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Dana can clean the house in {0} hours. Priya can do it in {1} hours. How long will it take them working together?'
NUMBERS = ['15', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

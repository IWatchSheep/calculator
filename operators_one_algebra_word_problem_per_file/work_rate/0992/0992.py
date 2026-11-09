"""Algebra word problem 0992   [Work rate]

Problem : Maya can wash the cars in 10 hours. Kira can do it in 20 hours. How long will it take them working together?
Let     : t = hours together
Equation: t/10 + t/20 = 1
Solve   : t(30)/200 = 1 → t = 200/30
Answer  : 20/3 hours (6.67 h)

Status  : ready: work_together answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0992'
KEY = 'work_rate/0992'
NAME = 'Work rate 0992'
CATEGORY = 'Work rate'
PROBLEM = 'Maya can wash the cars in 10 hours. Kira can do it in 20 hours. How long will it take them working together?'
LET = 't = hours together'
EQUATION = 't/10 + t/20 = 1'
SOLVE = 't(30)/200 = 1 → t = 200/30'
ANSWER = '20/3 hours (6.67 h)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'work_together'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Maya can wash the cars in {0} hours. Kira can do it in {1} hours. How long will it take them working together?'
NUMBERS = ['10', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

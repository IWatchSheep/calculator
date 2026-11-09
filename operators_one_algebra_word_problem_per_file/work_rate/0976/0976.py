"""Algebra word problem 0976   [Work rate]

Problem : Lena can paint a fence in 5 hours. Ava can do it in 10 hours. How long will it take them working together?
Let     : t = hours together
Equation: t/5 + t/10 = 1
Solve   : t(15)/50 = 1 → t = 50/15
Answer  : 10/3 hours (3.33 h)

Status  : ready: work_together answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0976'
KEY = 'work_rate/0976'
NAME = 'Work rate 0976'
CATEGORY = 'Work rate'
PROBLEM = 'Lena can paint a fence in 5 hours. Ava can do it in 10 hours. How long will it take them working together?'
LET = 't = hours together'
EQUATION = 't/5 + t/10 = 1'
SOLVE = 't(15)/50 = 1 → t = 50/15'
ANSWER = '10/3 hours (3.33 h)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'work_together'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Lena can paint a fence in {0} hours. Ava can do it in {1} hours. How long will it take them working together?'
NUMBERS = ['5', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

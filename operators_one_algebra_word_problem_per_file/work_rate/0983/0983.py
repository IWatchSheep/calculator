"""Algebra word problem 0983   [Work rate]

Problem : Bea can mow a lawn in 12 hours. Yara can do it in 18 hours. How long will it take them working together?
Let     : t = hours together
Equation: t/12 + t/18 = 1
Solve   : t(30)/216 = 1 → t = 216/30
Answer  : 7.2 hours (7.20 h)

Status  : ready: work_together answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0983'
KEY = 'work_rate/0983'
NAME = 'Work rate 0983'
CATEGORY = 'Work rate'
PROBLEM = 'Bea can mow a lawn in 12 hours. Yara can do it in 18 hours. How long will it take them working together?'
LET = 't = hours together'
EQUATION = 't/12 + t/18 = 1'
SOLVE = 't(30)/216 = 1 → t = 216/30'
ANSWER = '7.2 hours (7.20 h)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'work_together'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Bea can mow a lawn in {0} hours. Yara can do it in {1} hours. How long will it take them working together?'
NUMBERS = ['12', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0965   [Work rate]

Problem : Rosa can assemble the shelves in 15 hours. Fatima can do it in 3 hours. How long will it take them working together?
Let     : t = hours together
Equation: t/15 + t/3 = 1
Solve   : t(18)/45 = 1 → t = 45/18
Answer  : 2.5 hours (2.50 h)

Status  : ready: work_together answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0965'
KEY = 'work_rate/0965'
NAME = 'Work rate 0965'
CATEGORY = 'Work rate'
PROBLEM = 'Rosa can assemble the shelves in 15 hours. Fatima can do it in 3 hours. How long will it take them working together?'
LET = 't = hours together'
EQUATION = 't/15 + t/3 = 1'
SOLVE = 't(18)/45 = 1 → t = 45/18'
ANSWER = '2.5 hours (2.50 h)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'work_together'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Rosa can assemble the shelves in {0} hours. Fatima can do it in {1} hours. How long will it take them working together?'
NUMBERS = ['15', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

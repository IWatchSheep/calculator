"""Algebra word problem 0979   [Work rate]

Problem : Two typists type 70 and 30 words per minute. Working together, how long will they take to type 3800 words?
Let     : t = minutes
Equation: 70t + 30t = 3800
Solve   : 100t = 3800 → t = 38
Answer  : 38 minutes

Status  : ready: two_rates_one_pile answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0979'
KEY = 'work_rate/0979'
NAME = 'Work rate 0979'
CATEGORY = 'Work rate'
PROBLEM = 'Two typists type 70 and 30 words per minute. Working together, how long will they take to type 3800 words?'
LET = 't = minutes'
EQUATION = '70t + 30t = 3800'
SOLVE = '100t = 3800 → t = 38'
ANSWER = '38 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_rates_one_pile'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two typists type {0} and {1} words per minute. Working together, how long will they take to type {2} words?'
NUMBERS = ['70', '30', '3800']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

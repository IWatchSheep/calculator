"""Algebra word problem 0466   [Linear cost]

Problem : Ivan works two jobs paying $14/h and $17/h. Last month 24 hours were worked in total, earning $363. How many hours were worked at the $14 job?
Let     : h = hours at $14
Equation: 14h + 17(24 − h) = 363
Solve   : 3h = 45 → h = 15
Answer  : 15 hours at $14, 9 hours at $17

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0466'
KEY = 'linear_cost/0466'
NAME = 'Linear cost 0466'
CATEGORY = 'Linear cost'
PROBLEM = 'Ivan works two jobs paying $14/h and $17/h. Last month 24 hours were worked in total, earning $363. How many hours were worked at the $14 job?'
LET = 'h = hours at $14'
EQUATION = '14h + 17(24 − h) = 363'
SOLVE = '3h = 45 → h = 15'
ANSWER = '15 hours at $14, 9 hours at $17'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Ivan works two jobs paying ${0}/h and ${1}/h. Last month {2} hours were worked in total, earning ${3}. How many hours were worked at the ${4} job?'
NUMBERS = ['14', '17', '24', '363', '14']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

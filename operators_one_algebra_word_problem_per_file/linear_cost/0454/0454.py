"""Algebra word problem 0454   [Linear cost]

Problem : Pablo works two jobs paying $12/h and $17/h. Last month 21 hours were worked in total, earning $297. How many hours were worked at the $12 job?
Let     : h = hours at $12
Equation: 12h + 17(21 − h) = 297
Solve   : 5h = 60 → h = 12
Answer  : 12 hours at $12, 9 hours at $17

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0454'
KEY = 'linear_cost/0454'
NAME = 'Linear cost 0454'
CATEGORY = 'Linear cost'
PROBLEM = 'Pablo works two jobs paying $12/h and $17/h. Last month 21 hours were worked in total, earning $297. How many hours were worked at the $12 job?'
LET = 'h = hours at $12'
EQUATION = '12h + 17(21 − h) = 297'
SOLVE = '5h = 60 → h = 12'
ANSWER = '12 hours at $12, 9 hours at $17'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pablo works two jobs paying ${0}/h and ${1}/h. Last month {2} hours were worked in total, earning ${3}. How many hours were worked at the ${4} job?'
NUMBERS = ['12', '17', '21', '297', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

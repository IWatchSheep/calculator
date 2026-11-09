"""Algebra word problem 0433   [Linear cost]

Problem : Umar works two jobs paying $18/h and $20/h. Last month 53 hours were worked in total, earning $1010. How many hours were worked at the $18 job?
Let     : h = hours at $18
Equation: 18h + 20(53 − h) = 1010
Solve   : 2h = 50 → h = 25
Answer  : 25 hours at $18, 28 hours at $20

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0433'
KEY = 'linear_cost/0433'
NAME = 'Linear cost 0433'
CATEGORY = 'Linear cost'
PROBLEM = 'Umar works two jobs paying $18/h and $20/h. Last month 53 hours were worked in total, earning $1010. How many hours were worked at the $18 job?'
LET = 'h = hours at $18'
EQUATION = '18h + 20(53 − h) = 1010'
SOLVE = '2h = 50 → h = 25'
ANSWER = '25 hours at $18, 28 hours at $20'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Umar works two jobs paying ${0}/h and ${1}/h. Last month {2} hours were worked in total, earning ${3}. How many hours were worked at the ${4} job?'
NUMBERS = ['18', '20', '53', '1010', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

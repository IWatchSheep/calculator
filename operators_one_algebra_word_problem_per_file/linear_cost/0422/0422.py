"""Algebra word problem 0422   [Linear cost]

Problem : Yara works two jobs paying $16/h and $22/h. Last month 61 hours were worked in total, earning $1156. How many hours were worked at the $16 job?
Let     : h = hours at $16
Equation: 16h + 22(61 − h) = 1156
Solve   : 6h = 186 → h = 31
Answer  : 31 hours at $16, 30 hours at $22

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0422'
KEY = 'linear_cost/0422'
NAME = 'Linear cost 0422'
CATEGORY = 'Linear cost'
PROBLEM = 'Yara works two jobs paying $16/h and $22/h. Last month 61 hours were worked in total, earning $1156. How many hours were worked at the $16 job?'
LET = 'h = hours at $16'
EQUATION = '16h + 22(61 − h) = 1156'
SOLVE = '6h = 186 → h = 31'
ANSWER = '31 hours at $16, 30 hours at $22'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Yara works two jobs paying ${0}/h and ${1}/h. Last month {2} hours were worked in total, earning ${3}. How many hours were worked at the ${4} job?'
NUMBERS = ['16', '22', '61', '1156', '16']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

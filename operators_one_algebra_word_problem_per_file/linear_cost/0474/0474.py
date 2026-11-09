"""Algebra word problem 0474   [Linear cost]

Problem : Pablo works two jobs paying $14/h and $16/h. Last month 53 hours were worked in total, earning $796. How many hours were worked at the $14 job?
Let     : h = hours at $14
Equation: 14h + 16(53 − h) = 796
Solve   : 2h = 52 → h = 26
Answer  : 26 hours at $14, 27 hours at $16

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0474'
KEY = 'linear_cost/0474'
NAME = 'Linear cost 0474'
CATEGORY = 'Linear cost'
PROBLEM = 'Pablo works two jobs paying $14/h and $16/h. Last month 53 hours were worked in total, earning $796. How many hours were worked at the $14 job?'
LET = 'h = hours at $14'
EQUATION = '14h + 16(53 − h) = 796'
SOLVE = '2h = 52 → h = 26'
ANSWER = '26 hours at $14, 27 hours at $16'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pablo works two jobs paying ${0}/h and ${1}/h. Last month {2} hours were worked in total, earning ${3}. How many hours were worked at the ${4} job?'
NUMBERS = ['14', '16', '53', '796', '14']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

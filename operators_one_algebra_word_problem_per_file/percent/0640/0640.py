"""Algebra word problem 0640   [Percent]

Problem : 12 is 10% of what number?
Let     : x = the number
Equation: 0.1x = 12
Solve   : x = 12 ÷ 0.1 = 120
Answer  : 120

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0640'
KEY = 'percent/0640'
NAME = 'Percent 0640'
CATEGORY = 'Percent'
PROBLEM = '12 is 10% of what number?'
LET = 'x = the number'
EQUATION = '0.1x = 12'
SOLVE = 'x = 12 ÷ 0.1 = 120'
ANSWER = '120'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} is {1}% of what number?'
NUMBERS = ['12', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

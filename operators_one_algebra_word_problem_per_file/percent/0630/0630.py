"""Algebra word problem 0630   [Percent]

Problem : 21 is 12% of what number?
Let     : x = the number
Equation: 0.12x = 21
Solve   : x = 21 ÷ 0.12 = 175
Answer  : 175

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0630'
KEY = 'percent/0630'
NAME = 'Percent 0630'
CATEGORY = 'Percent'
PROBLEM = '21 is 12% of what number?'
LET = 'x = the number'
EQUATION = '0.12x = 21'
SOLVE = 'x = 21 ÷ 0.12 = 175'
ANSWER = '175'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} is {1}% of what number?'
NUMBERS = ['21', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

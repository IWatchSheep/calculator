"""Algebra word problem 0042   [Break-even]

Problem : Phone plan A costs $20.00 plus $0.10 per minute. Plan B costs $3.00 plus $0.15 per minute. For how many minutes do they cost the same?
Let     : x = number of minutes
Equation: 20 + 0.1x = 3 + 0.15x
Solve   : 0.05x = 17 → x = 340
Answer  : 340 minutes

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0042'
KEY = 'break_even/0042'
NAME = 'Break-even 0042'
CATEGORY = 'Break-even'
PROBLEM = 'Phone plan A costs $20.00 plus $0.10 per minute. Plan B costs $3.00 plus $0.15 per minute. For how many minutes do they cost the same?'
LET = 'x = number of minutes'
EQUATION = '20 + 0.1x = 3 + 0.15x'
SOLVE = '0.05x = 17 → x = 340'
ANSWER = '340 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Phone plan A costs ${0} plus ${1} per minute. Plan B costs ${2} plus ${3} per minute. For how many minutes do they cost the same?'
NUMBERS = ['20.00', '0.10', '3.00', '0.15']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0038   [Break-even]

Problem : Service A has a $240 sign-up fee and costs $12/month. Service B has no fee and costs $22/month. After how many months is the total cost the same?
Let     : n = months
Equation: 240 + 12n = 22n
Solve   : 10n = 240 → n = 24
Answer  : 24 months

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0038'
KEY = 'break_even/0038'
NAME = 'Break-even 0038'
CATEGORY = 'Break-even'
PROBLEM = 'Service A has a $240 sign-up fee and costs $12/month. Service B has no fee and costs $22/month. After how many months is the total cost the same?'
LET = 'n = months'
EQUATION = '240 + 12n = 22n'
SOLVE = '10n = 240 → n = 24'
ANSWER = '24 months'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Service A has a ${0} sign-up fee and costs ${1}/month. Service B has no fee and costs ${2}/month. After how many months is the total cost the same?'
NUMBERS = ['240', '12', '22']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

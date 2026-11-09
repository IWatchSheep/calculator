"""Algebra word problem 0052   [Break-even]

Problem : Service A has a $90 sign-up fee and costs $8/month. Service B has no fee and costs $11/month. After how many months is the total cost the same?
Let     : n = months
Equation: 90 + 8n = 11n
Solve   : 3n = 90 → n = 30
Answer  : 30 months

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0052'
KEY = 'break_even/0052'
NAME = 'Break-even 0052'
CATEGORY = 'Break-even'
PROBLEM = 'Service A has a $90 sign-up fee and costs $8/month. Service B has no fee and costs $11/month. After how many months is the total cost the same?'
LET = 'n = months'
EQUATION = '90 + 8n = 11n'
SOLVE = '3n = 90 → n = 30'
ANSWER = '30 months'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Service A has a ${0} sign-up fee and costs ${1}/month. Service B has no fee and costs ${2}/month. After how many months is the total cost the same?'
NUMBERS = ['90', '8', '11']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0046   [Break-even]

Problem : Service A has a $140 sign-up fee and costs $8/month. Service B has no fee and costs $13/month. After how many months is the total cost the same?
Let     : n = months
Equation: 140 + 8n = 13n
Solve   : 5n = 140 → n = 28
Answer  : 28 months

Status  : ready: archive_break_even_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0046'
KEY = 'break_even/0046'
NAME = 'Break-even 0046'
CATEGORY = 'Break-even'
PROBLEM = 'Service A has a $140 sign-up fee and costs $8/month. Service B has no fee and costs $13/month. After how many months is the total cost the same?'
LET = 'n = months'
EQUATION = '140 + 8n = 13n'
SOLVE = '5n = 140 → n = 28'
ANSWER = '28 months'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_break_even_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Service A has a ${0} sign-up fee and costs ${1}/month. Service B has no fee and costs ${2}/month. After how many months is the total cost the same?'
NUMBERS = ['140', '8', '13']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0442   [Linear cost]

Problem : Pablo earns $16/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $832.00. How many overtime hours were worked?
Let     : h = overtime hours
Equation: 40(16) + 24h = 832
Solve   : 24h = 192 → h = 8
Answer  : 8 overtime hours (48 hours total)

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0442'
KEY = 'linear_cost/0442'
NAME = 'Linear cost 0442'
CATEGORY = 'Linear cost'
PROBLEM = "Pablo earns $16/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $832.00. How many overtime hours were worked?"
LET = 'h = overtime hours'
EQUATION = '40(16) + 24h = 832'
SOLVE = '24h = 192 → h = 8'
ANSWER = '8 overtime hours (48 hours total)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "Pablo earns ${0}/hour for the first {1} hours and time-and-a-half after that. Last week's pay was ${2}. How many overtime hours were worked?"
NUMBERS = ['16', '40', '832.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0852   [Savings]

Problem : Jamal has $60 and saves $20 per week to buy a game console that costs $320. How many weeks until there is enough?
Let     : w = weeks
Equation: 60 + 20w = 320
Solve   : 20w = 260 → w = 13
Answer  : 13 weeks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0852'
KEY = 'savings/0852'
NAME = 'Savings 0852'
CATEGORY = 'Savings'
PROBLEM = 'Jamal has $60 and saves $20 per week to buy a game console that costs $320. How many weeks until there is enough?'
LET = 'w = weeks'
EQUATION = '60 + 20w = 320'
SOLVE = '20w = 260 → w = 13'
ANSWER = '13 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Jamal has ${0} and saves ${1} per week to buy a game console that costs ${2}. How many weeks until there is enough?'
NUMBERS = ['60', '20', '320']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0856   [Savings]

Problem : Finn has $50 and saves $15 per week to buy concert tickets that costs $320. How many weeks until there is enough?
Let     : w = weeks
Equation: 50 + 15w = 320
Solve   : 15w = 270 → w = 18
Answer  : 18 weeks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0856'
KEY = 'savings/0856'
NAME = 'Savings 0856'
CATEGORY = 'Savings'
PROBLEM = 'Finn has $50 and saves $15 per week to buy concert tickets that costs $320. How many weeks until there is enough?'
LET = 'w = weeks'
EQUATION = '50 + 15w = 320'
SOLVE = '15w = 270 → w = 18'
ANSWER = '18 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Finn has ${0} and saves ${1} per week to buy concert tickets that costs ${2}. How many weeks until there is enough?'
NUMBERS = ['50', '15', '320']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

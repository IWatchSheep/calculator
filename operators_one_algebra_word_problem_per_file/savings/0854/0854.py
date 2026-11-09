"""Algebra word problem 0854   [Savings]

Problem : Lena has $0 and saves $30 per week to buy a guitar that costs $750. How many weeks until there is enough?
Let     : w = weeks
Equation: 0 + 30w = 750
Solve   : 30w = 750 → w = 25
Answer  : 25 weeks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0854'
KEY = 'savings/0854'
NAME = 'Savings 0854'
CATEGORY = 'Savings'
PROBLEM = 'Lena has $0 and saves $30 per week to buy a guitar that costs $750. How many weeks until there is enough?'
LET = 'w = weeks'
EQUATION = '0 + 30w = 750'
SOLVE = '30w = 750 → w = 25'
ANSWER = '25 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Lena has ${0} and saves ${1} per week to buy a guitar that costs ${2}. How many weeks until there is enough?'
NUMBERS = ['0', '30', '750']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

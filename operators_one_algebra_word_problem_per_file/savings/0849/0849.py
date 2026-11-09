"""Algebra word problem 0849   [Savings]

Problem : Ben has $70 and saves $15 per week to buy a laptop that costs $220. How many weeks until there is enough?
Let     : w = weeks
Equation: 70 + 15w = 220
Solve   : 15w = 150 → w = 10
Answer  : 10 weeks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0849'
KEY = 'savings/0849'
NAME = 'Savings 0849'
CATEGORY = 'Savings'
PROBLEM = 'Ben has $70 and saves $15 per week to buy a laptop that costs $220. How many weeks until there is enough?'
LET = 'w = weeks'
EQUATION = '70 + 15w = 220'
SOLVE = '15w = 150 → w = 10'
ANSWER = '10 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Ben has ${0} and saves ${1} per week to buy a laptop that costs ${2}. How many weeks until there is enough?'
NUMBERS = ['70', '15', '220']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

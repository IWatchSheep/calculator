"""Algebra word problem 0060   [Coins]

Problem : A jar has quarters, dimes, and nickels worth $2.90. There are 2 more dimes than quarters and twice as many nickels as quarters. How many of each coin?
Let     : q = quarters
Equation: 25q + 10(q + 2) + 5(2q) = 290
Solve   : 45q = 270 → q = 6
Answer  : 6 quarters, 8 dimes, 12 nickels

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0060'
KEY = 'coins/0060'
NAME = 'Coins 0060'
CATEGORY = 'Coins'
PROBLEM = 'A jar has quarters, dimes, and nickels worth $2.90. There are 2 more dimes than quarters and twice as many nickels as quarters. How many of each coin?'
LET = 'q = quarters'
EQUATION = '25q + 10(q + 2) + 5(2q) = 290'
SOLVE = '45q = 270 → q = 6'
ANSWER = '6 quarters, 8 dimes, 12 nickels'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A jar has quarters, dimes, and nickels worth ${0}. There are {1} more dimes than quarters and twice as many nickels as quarters. How many of each coin?'
NUMBERS = ['2.90', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

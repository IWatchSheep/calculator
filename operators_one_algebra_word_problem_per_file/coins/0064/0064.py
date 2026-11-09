"""Algebra word problem 0064   [Coins]

Problem : Yusuf has 79 coins, all nickels and quarters, worth $11.95 in total. How many of each coin are there?
Let     : x = number of nickels; 79 − x = number of quarters
Equation: 5x + 25(79 − x) = 1195
Solve   : 20x = 780 → x = 39
Answer  : 39 nickels and 40 quarters

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0064'
KEY = 'coins/0064'
NAME = 'Coins 0064'
CATEGORY = 'Coins'
PROBLEM = 'Yusuf has 79 coins, all nickels and quarters, worth $11.95 in total. How many of each coin are there?'
LET = 'x = number of nickels; 79 − x = number of quarters'
EQUATION = '5x + 25(79 − x) = 1195'
SOLVE = '20x = 780 → x = 39'
ANSWER = '39 nickels and 40 quarters'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Yusuf has {0} coins, all nickels and quarters, worth ${1} in total. How many of each coin are there?'
NUMBERS = ['79', '11.95']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

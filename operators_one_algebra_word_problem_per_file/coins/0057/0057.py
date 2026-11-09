"""Algebra word problem 0057   [Coins]

Problem : Pablo has 45 coins, all nickels and quarters, worth $7.45 in total. How many of each coin are there?
Let     : x = number of nickels; 45 − x = number of quarters
Equation: 5x + 25(45 − x) = 745
Solve   : 20x = 380 → x = 19
Answer  : 19 nickels and 26 quarters

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0057'
KEY = 'coins/0057'
NAME = 'Coins 0057'
CATEGORY = 'Coins'
PROBLEM = 'Pablo has 45 coins, all nickels and quarters, worth $7.45 in total. How many of each coin are there?'
LET = 'x = number of nickels; 45 − x = number of quarters'
EQUATION = '5x + 25(45 − x) = 745'
SOLVE = '20x = 380 → x = 19'
ANSWER = '19 nickels and 26 quarters'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pablo has {0} coins, all nickels and quarters, worth ${1} in total. How many of each coin are there?'
NUMBERS = ['45', '7.45']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0059   [Coins]

Problem : Theo has 37 coins, all nickels and quarters, worth $2.85 in total. How many of each coin are there?
Let     : x = number of nickels; 37 − x = number of quarters
Equation: 5x + 25(37 − x) = 285
Solve   : 20x = 640 → x = 32
Answer  : 32 nickels and 5 quarters

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0059'
KEY = 'coins/0059'
NAME = 'Coins 0059'
CATEGORY = 'Coins'
PROBLEM = 'Theo has 37 coins, all nickels and quarters, worth $2.85 in total. How many of each coin are there?'
LET = 'x = number of nickels; 37 − x = number of quarters'
EQUATION = '5x + 25(37 − x) = 285'
SOLVE = '20x = 640 → x = 32'
ANSWER = '32 nickels and 5 quarters'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Theo has {0} coins, all nickels and quarters, worth ${1} in total. How many of each coin are there?'
NUMBERS = ['37', '2.85']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0065   [Coins]

Problem : Oscar has 30 coins, all dimes and quarters, worth $3.45 in total. How many of each coin are there?
Let     : x = number of dimes; 30 − x = number of quarters
Equation: 10x + 25(30 − x) = 345
Solve   : 15x = 405 → x = 27
Answer  : 27 dimes and 3 quarters

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0065'
KEY = 'coins/0065'
NAME = 'Coins 0065'
CATEGORY = 'Coins'
PROBLEM = 'Oscar has 30 coins, all dimes and quarters, worth $3.45 in total. How many of each coin are there?'
LET = 'x = number of dimes; 30 − x = number of quarters'
EQUATION = '10x + 25(30 − x) = 345'
SOLVE = '15x = 405 → x = 27'
ANSWER = '27 dimes and 3 quarters'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Oscar has {0} coins, all dimes and quarters, worth ${1} in total. How many of each coin are there?'
NUMBERS = ['30', '3.45']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

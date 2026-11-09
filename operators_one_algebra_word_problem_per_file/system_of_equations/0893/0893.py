"""Algebra word problem 0893   [System of equations]

Problem : A lot has motorcycles and cars. There are 113 vehicles and 344 wheels. How many of each are there?
Let     : x = motorcycles, y = cars
Equation: x + y = 113;  2x + 4y = 344
Solve   : 2x + 4(113 − x) = 344 → x = 54, y = 59
Answer  : 54 motorcycles and 59 cars

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0893'
KEY = 'system_of_equations/0893'
NAME = 'System of equations 0893'
CATEGORY = 'System of equations'
PROBLEM = 'A lot has motorcycles and cars. There are 113 vehicles and 344 wheels. How many of each are there?'
LET = 'x = motorcycles, y = cars'
EQUATION = 'x + y = 113;  2x + 4y = 344'
SOLVE = '2x + 4(113 − x) = 344 → x = 54, y = 59'
ANSWER = '54 motorcycles and 59 cars'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A lot has motorcycles and cars. There are {0} vehicles and {1} wheels. How many of each are there?'
NUMBERS = ['113', '344']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

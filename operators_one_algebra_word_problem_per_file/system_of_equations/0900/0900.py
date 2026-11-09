"""Algebra word problem 0900   [System of equations]

Problem : A lot has bicycles and tricycles. There are 112 vehicles and 277 wheels. How many of each are there?
Let     : x = bicycles, y = tricycles
Equation: x + y = 112;  2x + 3y = 277
Solve   : 2x + 3(112 − x) = 277 → x = 59, y = 53
Answer  : 59 bicycles and 53 tricycles

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0900'
KEY = 'system_of_equations/0900'
NAME = 'System of equations 0900'
CATEGORY = 'System of equations'
PROBLEM = 'A lot has bicycles and tricycles. There are 112 vehicles and 277 wheels. How many of each are there?'
LET = 'x = bicycles, y = tricycles'
EQUATION = 'x + y = 112;  2x + 3y = 277'
SOLVE = '2x + 3(112 − x) = 277 → x = 59, y = 53'
ANSWER = '59 bicycles and 53 tricycles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A lot has bicycles and tricycles. There are {0} vehicles and {1} wheels. How many of each are there?'
NUMBERS = ['112', '277']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0695   [Proportion]

Problem : Suppose 1 dollar buys 1.25 units of a foreign currency. How many dollars do you need to get 1875 units?
Let     : d = dollars
Equation: 1.25d = 1875
Solve   : 1.25d = 1875 → d = 1500
Answer  : $1,500.00

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0695'
KEY = 'proportion/0695'
NAME = 'Proportion 0695'
CATEGORY = 'Proportion'
PROBLEM = 'Suppose 1 dollar buys 1.25 units of a foreign currency. How many dollars do you need to get 1875 units?'
LET = 'd = dollars'
EQUATION = '1.25d = 1875'
SOLVE = '1.25d = 1875 → d = 1500'
ANSWER = '$1,500.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Suppose {0} dollar buys {1} units of a foreign currency. How many dollars do you need to get {2} units?'
NUMBERS = ['1', '1.25', '1875']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

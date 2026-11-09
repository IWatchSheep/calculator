"""Algebra word problem 0867   [Simple interest]

Problem : Victor invests $20,500.00, part at 5% and the rest at 7% simple annual interest. After one year the total interest is $1,055.00. How much was invested at each rate?
Let     : x = amount at 5%; 20500 − x = amount at 7%
Equation: 0.05x + 0.07(20500 − x) = 1055
Solve   : 0.02x = 380 → x = 19000
Answer  : $19,000.00 at 5% and $1,500.00 at 7%

Status  : ready: two_rate_interest answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0867'
KEY = 'simple_interest/0867'
NAME = 'Simple interest 0867'
CATEGORY = 'Simple interest'
PROBLEM = 'Victor invests $20,500.00, part at 5% and the rest at 7% simple annual interest. After one year the total interest is $1,055.00. How much was invested at each rate?'
LET = 'x = amount at 5%; 20500 − x = amount at 7%'
EQUATION = '0.05x + 0.07(20500 − x) = 1055'
SOLVE = '0.02x = 380 → x = 19000'
ANSWER = '$19,000.00 at 5% and $1,500.00 at 7%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_rate_interest'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Victor invests ${0}, part at {1}% and the rest at {2}% simple annual interest. After one year the total interest is ${3}. How much was invested at each rate?'
NUMBERS = ['20500.00', '5', '7', '1055.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

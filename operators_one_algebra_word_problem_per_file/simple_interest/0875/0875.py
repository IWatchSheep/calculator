"""Algebra word problem 0875   [Simple interest]

Problem : Dana invests $13,500.00, part at 2% and the rest at 5% simple annual interest. After one year the total interest is $450.00. How much was invested at each rate?
Let     : x = amount at 2%; 13500 − x = amount at 5%
Equation: 0.02x + 0.05(13500 − x) = 450
Solve   : 0.03x = 225 → x = 7500
Answer  : $7,500.00 at 2% and $6,000.00 at 5%

Status  : ready: two_rate_interest answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0875'
KEY = 'simple_interest/0875'
NAME = 'Simple interest 0875'
CATEGORY = 'Simple interest'
PROBLEM = 'Dana invests $13,500.00, part at 2% and the rest at 5% simple annual interest. After one year the total interest is $450.00. How much was invested at each rate?'
LET = 'x = amount at 2%; 13500 − x = amount at 5%'
EQUATION = '0.02x + 0.05(13500 − x) = 450'
SOLVE = '0.03x = 225 → x = 7500'
ANSWER = '$7,500.00 at 2% and $6,000.00 at 5%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_rate_interest'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Dana invests ${0}, part at {1}% and the rest at {2}% simple annual interest. After one year the total interest is ${3}. How much was invested at each rate?'
NUMBERS = ['13500.00', '2', '5', '450.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

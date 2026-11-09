"""Algebra word problem 0863   [Simple interest]

Problem : Quinn invests $31,000.00, part at 2% and the rest at 3% simple annual interest. After one year the total interest is $770.00. How much was invested at each rate?
Let     : x = amount at 2%; 31000 − x = amount at 3%
Equation: 0.02x + 0.03(31000 − x) = 770
Solve   : 0.01x = 160 → x = 16000
Answer  : $16,000.00 at 2% and $15,000.00 at 3%

Status  : ready: two_rate_interest answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0863'
KEY = 'simple_interest/0863'
NAME = 'Simple interest 0863'
CATEGORY = 'Simple interest'
PROBLEM = 'Quinn invests $31,000.00, part at 2% and the rest at 3% simple annual interest. After one year the total interest is $770.00. How much was invested at each rate?'
LET = 'x = amount at 2%; 31000 − x = amount at 3%'
EQUATION = '0.02x + 0.03(31000 − x) = 770'
SOLVE = '0.01x = 160 → x = 16000'
ANSWER = '$16,000.00 at 2% and $15,000.00 at 3%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_rate_interest'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Quinn invests ${0}, part at {1}% and the rest at {2}% simple annual interest. After one year the total interest is ${3}. How much was invested at each rate?'
NUMBERS = ['31000.00', '2', '3', '770.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

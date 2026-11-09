"""Algebra word problem 0872   [Simple interest]

Problem : Kofi invests $30,500.00, part at 2% and the rest at 4% simple annual interest. After one year the total interest is $830.00. How much was invested at each rate?
Let     : x = amount at 2%; 30500 − x = amount at 4%
Equation: 0.02x + 0.04(30500 − x) = 830
Solve   : 0.02x = 390 → x = 19500
Answer  : $19,500.00 at 2% and $11,000.00 at 4%

Status  : ready: two_rate_interest answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0872'
KEY = 'simple_interest/0872'
NAME = 'Simple interest 0872'
CATEGORY = 'Simple interest'
PROBLEM = 'Kofi invests $30,500.00, part at 2% and the rest at 4% simple annual interest. After one year the total interest is $830.00. How much was invested at each rate?'
LET = 'x = amount at 2%; 30500 − x = amount at 4%'
EQUATION = '0.02x + 0.04(30500 − x) = 830'
SOLVE = '0.02x = 390 → x = 19500'
ANSWER = '$19,500.00 at 2% and $11,000.00 at 4%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_rate_interest'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Kofi invests ${0}, part at {1}% and the rest at {2}% simple annual interest. After one year the total interest is ${3}. How much was invested at each rate?'
NUMBERS = ['30500.00', '2', '4', '830.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

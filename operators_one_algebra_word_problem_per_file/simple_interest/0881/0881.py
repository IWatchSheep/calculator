"""Algebra word problem 0881   [Simple interest]

Problem : Mateo invests $40,000.00, part at 2% and the rest at 8% simple annual interest. After one year the total interest is $2,000.00. How much was invested at each rate?
Let     : x = amount at 2%; 40000 − x = amount at 8%
Equation: 0.02x + 0.08(40000 − x) = 2000
Solve   : 0.06x = 1200 → x = 20000
Answer  : $20,000.00 at 2% and $20,000.00 at 8%

Status  : ready: two_rate_interest answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0881'
KEY = 'simple_interest/0881'
NAME = 'Simple interest 0881'
CATEGORY = 'Simple interest'
PROBLEM = 'Mateo invests $40,000.00, part at 2% and the rest at 8% simple annual interest. After one year the total interest is $2,000.00. How much was invested at each rate?'
LET = 'x = amount at 2%; 40000 − x = amount at 8%'
EQUATION = '0.02x + 0.08(40000 − x) = 2000'
SOLVE = '0.06x = 1200 → x = 20000'
ANSWER = '$20,000.00 at 2% and $20,000.00 at 8%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_rate_interest'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Mateo invests ${0}, part at {1}% and the rest at {2}% simple annual interest. After one year the total interest is ${3}. How much was invested at each rate?'
NUMBERS = ['40000.00', '2', '8', '2000.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

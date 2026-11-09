"""Algebra word problem 0625   [Percent]

Problem : A stock's price rose 10% one month and then fell 40% the next, ending at $580.80. What was the starting price?
Let     : p = starting price
Equation: 1.1 × 0.6 × p = 580.8
Solve   : 0.66p = 580.8 → p = 880
Answer  : $880.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0625'
KEY = 'percent/0625'
NAME = 'Percent 0625'
CATEGORY = 'Percent'
PROBLEM = "A stock's price rose 10% one month and then fell 40% the next, ending at $580.80. What was the starting price?"
LET = 'p = starting price'
EQUATION = '1.1 × 0.6 × p = 580.8'
SOLVE = '0.66p = 580.8 → p = 880'
ANSWER = '$880.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A stock's price rose {0}% one month and then fell {1}% the next, ending at ${2}. What was the starting price?"
NUMBERS = ['10', '40', '580.80']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

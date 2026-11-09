"""Algebra word problem 0660   [Percent]

Problem : A stock's price rose 20% one month and then fell 25% the next, ending at $792.00. What was the starting price?
Let     : p = starting price
Equation: 1.2 × 0.75 × p = 792
Solve   : 0.9p = 792 → p = 880
Answer  : $880.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0660'
KEY = 'percent/0660'
NAME = 'Percent 0660'
CATEGORY = 'Percent'
PROBLEM = "A stock's price rose 20% one month and then fell 25% the next, ending at $792.00. What was the starting price?"
LET = 'p = starting price'
EQUATION = '1.2 × 0.75 × p = 792'
SOLVE = '0.9p = 792 → p = 880'
ANSWER = '$880.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A stock's price rose {0}% one month and then fell {1}% the next, ending at ${2}. What was the starting price?"
NUMBERS = ['20', '25', '792.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

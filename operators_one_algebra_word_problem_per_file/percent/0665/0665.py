"""Algebra word problem 0665   [Percent]

Problem : A coat is marked 25% off, and then an extra 20% is taken off the sale price. The final price is $240.00. What was the original price?
Let     : p = original price
Equation: 0.75 × 0.8 × p = 240
Solve   : 0.6p = 240 → p = 400
Answer  : $400.00

Status  : ready: two_discounts answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0665'
KEY = 'percent/0665'
NAME = 'Percent 0665'
CATEGORY = 'Percent'
PROBLEM = 'A coat is marked 25% off, and then an extra 20% is taken off the sale price. The final price is $240.00. What was the original price?'
LET = 'p = original price'
EQUATION = '0.75 × 0.8 × p = 240'
SOLVE = '0.6p = 240 → p = 400'
ANSWER = '$400.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_discounts'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A coat is marked {0}% off, and then an extra {1}% is taken off the sale price. The final price is ${2}. What was the original price?'
NUMBERS = ['25', '20', '240.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

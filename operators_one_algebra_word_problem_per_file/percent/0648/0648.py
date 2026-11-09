"""Algebra word problem 0648   [Percent]

Problem : A coat is marked 50% off, and then an extra 25% is taken off the sale price. The final price is $296.25. What was the original price?
Let     : p = original price
Equation: 0.5 × 0.75 × p = 296.25
Solve   : 0.375p = 296.25 → p = 790
Answer  : $790.00

Status  : ready: two_discounts answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0648'
KEY = 'percent/0648'
NAME = 'Percent 0648'
CATEGORY = 'Percent'
PROBLEM = 'A coat is marked 50% off, and then an extra 25% is taken off the sale price. The final price is $296.25. What was the original price?'
LET = 'p = original price'
EQUATION = '0.5 × 0.75 × p = 296.25'
SOLVE = '0.375p = 296.25 → p = 790'
ANSWER = '$790.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_discounts'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A coat is marked {0}% off, and then an extra {1}% is taken off the sale price. The final price is ${2}. What was the original price?'
NUMBERS = ['50', '25', '296.25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

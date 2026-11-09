"""Algebra word problem 0884   [System of equations]

Problem : 1 burgers and 3 fries cost $43.00. 5 burgers and 1 fries cost $65.90. Find the price of one of each.
Let     : x = price of one of the burgers, y = price of one of the fries
Equation: x + 3y = 43;  5x + y = 65.9
Solve   : By elimination or substitution: x = 11.05, y = 10.65
Answer  : burgers: $11.05 each, fries: $10.65 each

Status  : ready: two_purchases answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0884'
KEY = 'system_of_equations/0884'
NAME = 'System of equations 0884'
CATEGORY = 'System of equations'
PROBLEM = '1 burgers and 3 fries cost $43.00. 5 burgers and 1 fries cost $65.90. Find the price of one of each.'
LET = 'x = price of one of the burgers, y = price of one of the fries'
EQUATION = 'x + 3y = 43;  5x + y = 65.9'
SOLVE = 'By elimination or substitution: x = 11.05, y = 10.65'
ANSWER = 'burgers: $11.05 each, fries: $10.65 each'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_purchases'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} burgers and {1} fries cost ${2}. {3} burgers and {4} fries cost ${5}. Find the price of one of each.'
NUMBERS = ['1', '3', '43.00', '5', '1', '65.90']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

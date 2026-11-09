"""Algebra word problem 0908   [System of equations]

Problem : 2 coffees and 5 muffins cost $33.85. 3 coffees and 5 muffins cost $37.90. Find the price of one of each.
Let     : x = price of one of the coffees, y = price of one of the muffins
Equation: 2x + 5y = 33.85;  3x + 5y = 37.9
Solve   : By elimination or substitution: x = 4.05, y = 5.15
Answer  : coffees: $4.05 each, muffins: $5.15 each

Status  : ready: two_purchases answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0908'
KEY = 'system_of_equations/0908'
NAME = 'System of equations 0908'
CATEGORY = 'System of equations'
PROBLEM = '2 coffees and 5 muffins cost $33.85. 3 coffees and 5 muffins cost $37.90. Find the price of one of each.'
LET = 'x = price of one of the coffees, y = price of one of the muffins'
EQUATION = '2x + 5y = 33.85;  3x + 5y = 37.9'
SOLVE = 'By elimination or substitution: x = 4.05, y = 5.15'
ANSWER = 'coffees: $4.05 each, muffins: $5.15 each'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_purchases'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} coffees and {1} muffins cost ${2}. {3} coffees and {4} muffins cost ${5}. Find the price of one of each.'
NUMBERS = ['2', '5', '33.85', '3', '5', '37.90']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

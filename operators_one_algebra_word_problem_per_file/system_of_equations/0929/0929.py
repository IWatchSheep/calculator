"""Algebra word problem 0929   [System of equations]

Problem : 1 coffees and 2 muffins cost $14.45. 2 coffees and 6 muffins cost $38.50. Find the price of one of each.
Let     : x = price of one of the coffees, y = price of one of the muffins
Equation: x + 2y = 14.45;  2x + 6y = 38.5
Solve   : By elimination or substitution: x = 4.85, y = 4.80
Answer  : coffees: $4.85 each, muffins: $4.80 each

Status  : ready: two_purchases answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0929'
KEY = 'system_of_equations/0929'
NAME = 'System of equations 0929'
CATEGORY = 'System of equations'
PROBLEM = '1 coffees and 2 muffins cost $14.45. 2 coffees and 6 muffins cost $38.50. Find the price of one of each.'
LET = 'x = price of one of the coffees, y = price of one of the muffins'
EQUATION = 'x + 2y = 14.45;  2x + 6y = 38.5'
SOLVE = 'By elimination or substitution: x = 4.85, y = 4.80'
ANSWER = 'coffees: $4.85 each, muffins: $4.80 each'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_purchases'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} coffees and {1} muffins cost ${2}. {3} coffees and {4} muffins cost ${5}. Find the price of one of each.'
NUMBERS = ['1', '2', '14.45', '2', '6', '38.50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

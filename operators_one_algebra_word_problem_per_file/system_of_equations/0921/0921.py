"""Algebra word problem 0921   [System of equations]

Problem : 1 notebooks and 6 pens cost $32.85. 1 notebooks and 3 pens cost $19.20. Find the price of one of each.
Let     : x = price of one of the notebooks, y = price of one of the pens
Equation: x + 6y = 32.85;  x + 3y = 19.2
Solve   : By elimination or substitution: x = 5.55, y = 4.55
Answer  : notebooks: $5.55 each, pens: $4.55 each

Status  : ready: two_purchases answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0921'
KEY = 'system_of_equations/0921'
NAME = 'System of equations 0921'
CATEGORY = 'System of equations'
PROBLEM = '1 notebooks and 6 pens cost $32.85. 1 notebooks and 3 pens cost $19.20. Find the price of one of each.'
LET = 'x = price of one of the notebooks, y = price of one of the pens'
EQUATION = 'x + 6y = 32.85;  x + 3y = 19.2'
SOLVE = 'By elimination or substitution: x = 5.55, y = 4.55'
ANSWER = 'notebooks: $5.55 each, pens: $4.55 each'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_purchases'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} notebooks and {1} pens cost ${2}. {3} notebooks and {4} pens cost ${5}. Find the price of one of each.'
NUMBERS = ['1', '6', '32.85', '1', '3', '19.20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

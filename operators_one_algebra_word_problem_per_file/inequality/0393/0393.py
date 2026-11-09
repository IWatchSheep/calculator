"""Algebra word problem 0393   [Inequality]

Problem : A school dance costs $324 to run. Tickets are $12. How many tickets must be sold for a profit of at least $1400?
Let     : n = tickets
Equation: 12n − 324 ≥ 1400
Solve   : n ≥ 431/3 → n = 144 (smallest whole number that works)
Answer  : 144 tickets

Status  : ready: least_for_profit answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0393'
KEY = 'inequality/0393'
NAME = 'Inequality 0393'
CATEGORY = 'Inequality'
PROBLEM = 'A school dance costs $324 to run. Tickets are $12. How many tickets must be sold for a profit of at least $1400?'
LET = 'n = tickets'
EQUATION = '12n − 324 ≥ 1400'
SOLVE = 'n ≥ 431/3 → n = 144 (smallest whole number that works)'
ANSWER = '144 tickets'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'least_for_profit'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A school dance costs ${0} to run. Tickets are ${1}. How many tickets must be sold for a profit of at least ${2}?'
NUMBERS = ['324', '12', '1400']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

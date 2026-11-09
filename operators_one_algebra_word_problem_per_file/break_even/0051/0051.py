"""Algebra word problem 0051   [Break-even]

Problem : A food truck pays $375 in daily costs, and each meal costs $18 in ingredients. Meals sell for $23. How many meals a day cover the costs?
Let     : n = number of meals
Equation: 23n = 375 + 18n
Solve   : 5n = 375 → n = 75
Answer  : 75 meals

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0051'
KEY = 'break_even/0051'
NAME = 'Break-even 0051'
CATEGORY = 'Break-even'
PROBLEM = 'A food truck pays $375 in daily costs, and each meal costs $18 in ingredients. Meals sell for $23. How many meals a day cover the costs?'
LET = 'n = number of meals'
EQUATION = '23n = 375 + 18n'
SOLVE = '5n = 375 → n = 75'
ANSWER = '75 meals'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A food truck pays ${0} in daily costs, and each meal costs ${1} in ingredients. Meals sell for ${2}. How many meals a day cover the costs?'
NUMBERS = ['375', '18', '23']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

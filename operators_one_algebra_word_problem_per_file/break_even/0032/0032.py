"""Algebra word problem 0032   [Break-even]

Problem : A food truck pays $350 in daily costs, and each meal costs $1 in ingredients. Meals sell for $8. How many meals a day cover the costs?
Let     : n = number of meals
Equation: 8n = 350 + n
Solve   : 7n = 350 → n = 50
Answer  : 50 meals

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0032'
KEY = 'break_even/0032'
NAME = 'Break-even 0032'
CATEGORY = 'Break-even'
PROBLEM = 'A food truck pays $350 in daily costs, and each meal costs $1 in ingredients. Meals sell for $8. How many meals a day cover the costs?'
LET = 'n = number of meals'
EQUATION = '8n = 350 + n'
SOLVE = '7n = 350 → n = 50'
ANSWER = '50 meals'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A food truck pays ${0} in daily costs, and each meal costs ${1} in ingredients. Meals sell for ${2}. How many meals a day cover the costs?'
NUMBERS = ['350', '1', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0469   [Linear cost]

Problem : A gym charges a $100 joining fee and $30 per month. Wren has paid $190 in total. How many months has Wren been a member?
Let     : n = months
Equation: 100 + 30n = 190
Solve   : 30n = 90 → n = 3
Answer  : 3 months

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0469'
KEY = 'linear_cost/0469'
NAME = 'Linear cost 0469'
CATEGORY = 'Linear cost'
PROBLEM = 'A gym charges a $100 joining fee and $30 per month. Wren has paid $190 in total. How many months has Wren been a member?'
LET = 'n = months'
EQUATION = '100 + 30n = 190'
SOLVE = '30n = 90 → n = 3'
ANSWER = '3 months'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A gym charges a ${0} joining fee and ${1} per month. Wren has paid ${2} in total. How many months has Wren been a member?'
NUMBERS = ['100', '30', '190']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

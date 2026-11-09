"""Algebra word problem 0443   [Linear cost]

Problem : A gym charges a $100 joining fee and $15 per month. Caleb has paid $145 in total. How many months has Caleb been a member?
Let     : n = months
Equation: 100 + 15n = 145
Solve   : 15n = 45 → n = 3
Answer  : 3 months

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0443'
KEY = 'linear_cost/0443'
NAME = 'Linear cost 0443'
CATEGORY = 'Linear cost'
PROBLEM = 'A gym charges a $100 joining fee and $15 per month. Caleb has paid $145 in total. How many months has Caleb been a member?'
LET = 'n = months'
EQUATION = '100 + 15n = 145'
SOLVE = '15n = 45 → n = 3'
ANSWER = '3 months'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A gym charges a ${0} joining fee and ${1} per month. Caleb has paid ${2} in total. How many months has Caleb been a member?'
NUMBERS = ['100', '15', '145']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

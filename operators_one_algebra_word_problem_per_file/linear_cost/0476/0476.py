"""Algebra word problem 0476   [Linear cost]

Problem : A gym charges a $99 joining fee and $15 per month. Dana has paid $219 in total. How many months has Dana been a member?
Let     : n = months
Equation: 99 + 15n = 219
Solve   : 15n = 120 → n = 8
Answer  : 8 months

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0476'
KEY = 'linear_cost/0476'
NAME = 'Linear cost 0476'
CATEGORY = 'Linear cost'
PROBLEM = 'A gym charges a $99 joining fee and $15 per month. Dana has paid $219 in total. How many months has Dana been a member?'
LET = 'n = months'
EQUATION = '99 + 15n = 219'
SOLVE = '15n = 120 → n = 8'
ANSWER = '8 months'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A gym charges a ${0} joining fee and ${1} per month. Dana has paid ${2} in total. How many months has Dana been a member?'
NUMBERS = ['99', '15', '219']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0869   [Simple interest]

Problem : Emeka has $6,000.00 invested at 2%. How much more must be invested at 8% so that the total earns 5% overall?
Let     : x = extra amount
Equation: 0.02(6000) + 0.08x = 0.05(6000 + x)
Solve   : 0.03x = 180 → x = 6000
Answer  : $6,000.00

Status  : ready: more_invested_for_overall_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0869'
KEY = 'simple_interest/0869'
NAME = 'Simple interest 0869'
CATEGORY = 'Simple interest'
PROBLEM = 'Emeka has $6,000.00 invested at 2%. How much more must be invested at 8% so that the total earns 5% overall?'
LET = 'x = extra amount'
EQUATION = '0.02(6000) + 0.08x = 0.05(6000 + x)'
SOLVE = '0.03x = 180 → x = 6000'
ANSWER = '$6,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'more_invested_for_overall_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Emeka has ${0} invested at {1}%. How much more must be invested at {2}% so that the total earns {3}% overall?'
NUMBERS = ['6000.00', '2', '8', '5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

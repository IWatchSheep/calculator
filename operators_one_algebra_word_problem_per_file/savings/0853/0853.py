"""Algebra word problem 0853   [Savings]

Problem : Yusuf has $350 saved and adds $25 each week. Umar has $630 saved and adds $20 each week. After how many weeks will they have the same amount?
Let     : w = weeks
Equation: 350 + 25w = 630 + 20w
Solve   : 5w = 280 → w = 56
Answer  : 56 weeks (each will have $1750)

Status  : ready: savings_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0853'
KEY = 'savings/0853'
NAME = 'Savings 0853'
CATEGORY = 'Savings'
PROBLEM = 'Yusuf has $350 saved and adds $25 each week. Umar has $630 saved and adds $20 each week. After how many weeks will they have the same amount?'
LET = 'w = weeks'
EQUATION = '350 + 25w = 630 + 20w'
SOLVE = '5w = 280 → w = 56'
ANSWER = '56 weeks (each will have $1750)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'savings_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Yusuf has ${0} saved and adds ${1} each week. Umar has ${2} saved and adds ${3} each week. After how many weeks will they have the same amount?'
NUMBERS = ['350', '25', '630', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

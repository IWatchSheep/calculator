"""Algebra word problem 0850   [Savings]

Problem : Victor has $0 saved and adds $25 each week. Kira has $180 saved and adds $10 each week. After how many weeks will they have the same amount?
Let     : w = weeks
Equation: 0 + 25w = 180 + 10w
Solve   : 15w = 180 → w = 12
Answer  : 12 weeks (each will have $300)

Status  : ready: savings_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0850'
KEY = 'savings/0850'
NAME = 'Savings 0850'
CATEGORY = 'Savings'
PROBLEM = 'Victor has $0 saved and adds $25 each week. Kira has $180 saved and adds $10 each week. After how many weeks will they have the same amount?'
LET = 'w = weeks'
EQUATION = '0 + 25w = 180 + 10w'
SOLVE = '15w = 180 → w = 12'
ANSWER = '12 weeks (each will have $300)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'savings_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Victor has ${0} saved and adds ${1} each week. Kira has ${2} saved and adds ${3} each week. After how many weeks will they have the same amount?'
NUMBERS = ['0', '25', '180', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

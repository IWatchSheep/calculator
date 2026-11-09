"""Algebra word problem 0848   [Savings]

Problem : Ben has $150 saved and adds $25 each week. Ava has $310 saved and adds $15 each week. After how many weeks will they have the same amount?
Let     : w = weeks
Equation: 150 + 25w = 310 + 15w
Solve   : 10w = 160 → w = 16
Answer  : 16 weeks (each will have $550)

Status  : ready: savings_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0848'
KEY = 'savings/0848'
NAME = 'Savings 0848'
CATEGORY = 'Savings'
PROBLEM = 'Ben has $150 saved and adds $25 each week. Ava has $310 saved and adds $15 each week. After how many weeks will they have the same amount?'
LET = 'w = weeks'
EQUATION = '150 + 25w = 310 + 15w'
SOLVE = '10w = 160 → w = 16'
ANSWER = '16 weeks (each will have $550)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'savings_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Ben has ${0} saved and adds ${1} each week. Ava has ${2} saved and adds ${3} each week. After how many weeks will they have the same amount?'
NUMBERS = ['150', '25', '310', '15']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

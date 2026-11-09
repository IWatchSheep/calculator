"""Algebra word problem 0855   [Savings]

Problem : Rhea has $330 saved and adds $15 each week. Jamal has $440 saved and adds $10 each week. After how many weeks will they have the same amount?
Let     : w = weeks
Equation: 330 + 15w = 440 + 10w
Solve   : 5w = 110 → w = 22
Answer  : 22 weeks (each will have $660)

Status  : ready: savings_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0855'
KEY = 'savings/0855'
NAME = 'Savings 0855'
CATEGORY = 'Savings'
PROBLEM = 'Rhea has $330 saved and adds $15 each week. Jamal has $440 saved and adds $10 each week. After how many weeks will they have the same amount?'
LET = 'w = weeks'
EQUATION = '330 + 15w = 440 + 10w'
SOLVE = '5w = 110 → w = 22'
ANSWER = '22 weeks (each will have $660)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'savings_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Rhea has ${0} saved and adds ${1} each week. Jamal has ${2} saved and adds ${3} each week. After how many weeks will they have the same amount?'
NUMBERS = ['330', '15', '440', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

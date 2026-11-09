"""Algebra word problem 0375   [Inequality]

Problem : Plan A costs $28 plus $0.15 per minute. Plan B costs $48 plus $0.05 per minute. What is the fewest whole minutes for which Plan B is cheaper?
Let     : m = minutes
Equation: 48 + 0.05m < 28 + 0.15m
Solve   : m ≥ 200 → m = 201 (smallest whole number that works)
Answer  : 201 minutes

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0375'
KEY = 'inequality/0375'
NAME = 'Inequality 0375'
CATEGORY = 'Inequality'
PROBLEM = 'Plan A costs $28 plus $0.15 per minute. Plan B costs $48 plus $0.05 per minute. What is the fewest whole minutes for which Plan B is cheaper?'
LET = 'm = minutes'
EQUATION = '48 + 0.05m < 28 + 0.15m'
SOLVE = 'm ≥ 200 → m = 201 (smallest whole number that works)'
ANSWER = '201 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Plan A costs ${0} plus ${1} per minute. Plan B costs ${2} plus ${3} per minute. What is the fewest whole minutes for which Plan B is cheaper?'
NUMBERS = ['28', '0.15', '48', '0.05']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

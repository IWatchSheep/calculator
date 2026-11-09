"""Algebra word problem 0364   [Inequality]

Problem : Plan A costs $21 plus $0.10 per minute. Plan B costs $33 plus $0.03 per minute. What is the fewest whole minutes for which Plan B is cheaper?
Let     : m = minutes
Equation: 33 + 0.03m < 21 + 0.1m
Solve   : m ≥ 1200/7 → m = 172 (smallest whole number that works)
Answer  : 172 minutes

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0364'
KEY = 'inequality/0364'
NAME = 'Inequality 0364'
CATEGORY = 'Inequality'
PROBLEM = 'Plan A costs $21 plus $0.10 per minute. Plan B costs $33 plus $0.03 per minute. What is the fewest whole minutes for which Plan B is cheaper?'
LET = 'm = minutes'
EQUATION = '33 + 0.03m < 21 + 0.1m'
SOLVE = 'm ≥ 1200/7 → m = 172 (smallest whole number that works)'
ANSWER = '172 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Plan A costs ${0} plus ${1} per minute. Plan B costs ${2} plus ${3} per minute. What is the fewest whole minutes for which Plan B is cheaper?'
NUMBERS = ['21', '0.10', '33', '0.03']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

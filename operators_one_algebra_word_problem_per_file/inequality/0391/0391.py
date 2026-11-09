"""Algebra word problem 0391   [Inequality]

Problem : Plan A costs $9 plus $0.25 per minute. Plan B costs $32 plus $0.05 per minute. What is the fewest whole minutes for which Plan B is cheaper?
Let     : m = minutes
Equation: 32 + 0.05m < 9 + 0.25m
Solve   : m ≥ 115 → m = 116 (smallest whole number that works)
Answer  : 116 minutes

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0391'
KEY = 'inequality/0391'
NAME = 'Inequality 0391'
CATEGORY = 'Inequality'
PROBLEM = 'Plan A costs $9 plus $0.25 per minute. Plan B costs $32 plus $0.05 per minute. What is the fewest whole minutes for which Plan B is cheaper?'
LET = 'm = minutes'
EQUATION = '32 + 0.05m < 9 + 0.25m'
SOLVE = 'm ≥ 115 → m = 116 (smallest whole number that works)'
ANSWER = '116 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Plan A costs ${0} plus ${1} per minute. Plan B costs ${2} plus ${3} per minute. What is the fewest whole minutes for which Plan B is cheaper?'
NUMBERS = ['9', '0.25', '32', '0.05']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0219   [Fractions]

Problem : A gas tank is 1/2 full. Adding 12 gallons fills it to 5/6. How much does the tank hold?
Let     : c = capacity
Equation: (1/2)c + 12 = (5/6)c
Solve   : c/3 = 12 → c = 12 × 3 = 36
Answer  : 36

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0219'
KEY = 'fractions/0219'
NAME = 'Fractions 0219'
CATEGORY = 'Fractions'
PROBLEM = 'A gas tank is 1/2 full. Adding 12 gallons fills it to 5/6. How much does the tank hold?'
LET = 'c = capacity'
EQUATION = '(1/2)c + 12 = (5/6)c'
SOLVE = 'c/3 = 12 → c = 12 × 3 = 36'
ANSWER = '36'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A gas tank is {0}/{1} full. Adding {2} gallons fills it to {3}/{4}. How much does the tank hold?'
NUMBERS = ['1', '2', '12', '5', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

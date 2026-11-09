"""Algebra word problem 0541   [Mixture]

Problem : A 6 L batch of 80% juice concentrate is diluted with water to 12% juice. How much water is added?
Let     : w = liters of water
Equation: 0.8(6) = 0.12(6 + w)
Solve   : 0.12w = 4.08 → w = 34
Answer  : 34 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0541'
KEY = 'mixture/0541'
NAME = 'Mixture 0541'
CATEGORY = 'Mixture'
PROBLEM = 'A 6 L batch of 80% juice concentrate is diluted with water to 12% juice. How much water is added?'
LET = 'w = liters of water'
EQUATION = '0.8(6) = 0.12(6 + w)'
SOLVE = '0.12w = 4.08 → w = 34'
ANSWER = '34 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} L batch of {1}% juice concentrate is diluted with water to {2}% juice. How much water is added?'
NUMBERS = ['6', '80', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

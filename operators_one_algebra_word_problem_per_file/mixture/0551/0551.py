"""Algebra word problem 0551   [Mixture]

Problem : A 20 L batch of 60% juice concentrate is diluted with water to 30% juice. How much water is added?
Let     : w = liters of water
Equation: 0.6(20) = 0.3(20 + w)
Solve   : 0.3w = 6 → w = 20
Answer  : 20 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0551'
KEY = 'mixture/0551'
NAME = 'Mixture 0551'
CATEGORY = 'Mixture'
PROBLEM = 'A 20 L batch of 60% juice concentrate is diluted with water to 30% juice. How much water is added?'
LET = 'w = liters of water'
EQUATION = '0.6(20) = 0.3(20 + w)'
SOLVE = '0.3w = 6 → w = 20'
ANSWER = '20 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} L batch of {1}% juice concentrate is diluted with water to {2}% juice. How much water is added?'
NUMBERS = ['20', '60', '30']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0535   [Mixture]

Problem : How much water must be added to 4 L of a 30% salt solution to make it 5% salt?
Let     : w = liters of water
Equation: 0.3(4) = 0.05(4 + w)
Solve   : w/20 = 1 → w = 1 × 20 = 20
Answer  : 20 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0535'
KEY = 'mixture/0535'
NAME = 'Mixture 0535'
CATEGORY = 'Mixture'
PROBLEM = 'How much water must be added to 4 L of a 30% salt solution to make it 5% salt?'
LET = 'w = liters of water'
EQUATION = '0.3(4) = 0.05(4 + w)'
SOLVE = 'w/20 = 1 → w = 1 × 20 = 20'
ANSWER = '20 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How much water must be added to {0} L of a {1}% salt solution to make it {2}% salt?'
NUMBERS = ['4', '30', '5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0567   [Mixture]

Problem : How many liters of pure antifreeze must be added to 12 L of a 50% antifreeze mix to get a 75% mix?
Let     : x = liters of pure antifreeze
Equation: 0.5(12) + x = 0.75(12 + x)
Solve   : x/4 = 3 → x = 3 × 4 = 12
Answer  : 12 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0567'
KEY = 'mixture/0567'
NAME = 'Mixture 0567'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of pure antifreeze must be added to 12 L of a 50% antifreeze mix to get a 75% mix?'
LET = 'x = liters of pure antifreeze'
EQUATION = '0.5(12) + x = 0.75(12 + x)'
SOLVE = 'x/4 = 3 → x = 3 × 4 = 12'
ANSWER = '12 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of pure antifreeze must be added to {0} L of a {1}% antifreeze mix to get a {2}% mix?'
NUMBERS = ['12', '50', '75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

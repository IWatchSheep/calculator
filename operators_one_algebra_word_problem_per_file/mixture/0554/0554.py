"""Algebra word problem 0554   [Mixture]

Problem : How many liters of pure antifreeze must be added to 6 L of a 25% antifreeze mix to get a 80% mix?
Let     : x = liters of pure antifreeze
Equation: 0.25(6) + x = 0.8(6 + x)
Solve   : x/5 = 3.3 → x = 3.3 × 5 = 16.5
Answer  : 16.5 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0554'
KEY = 'mixture/0554'
NAME = 'Mixture 0554'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of pure antifreeze must be added to 6 L of a 25% antifreeze mix to get a 80% mix?'
LET = 'x = liters of pure antifreeze'
EQUATION = '0.25(6) + x = 0.8(6 + x)'
SOLVE = 'x/5 = 3.3 → x = 3.3 × 5 = 16.5'
ANSWER = '16.5 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of pure antifreeze must be added to {0} L of a {1}% antifreeze mix to get a {2}% mix?'
NUMBERS = ['6', '25', '80']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

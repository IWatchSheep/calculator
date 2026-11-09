"""Algebra word problem 0538   [Mixture]

Problem : How many liters of pure antifreeze must be added to 4 L of a 30% antifreeze mix to get a 80% mix?
Let     : x = liters of pure antifreeze
Equation: 0.3(4) + x = 0.8(4 + x)
Solve   : x/5 = 2 → x = 2 × 5 = 10
Answer  : 10 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0538'
KEY = 'mixture/0538'
NAME = 'Mixture 0538'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of pure antifreeze must be added to 4 L of a 30% antifreeze mix to get a 80% mix?'
LET = 'x = liters of pure antifreeze'
EQUATION = '0.3(4) + x = 0.8(4 + x)'
SOLVE = 'x/5 = 2 → x = 2 × 5 = 10'
ANSWER = '10 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of pure antifreeze must be added to {0} L of a {1}% antifreeze mix to get a {2}% mix?'
NUMBERS = ['4', '30', '80']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0542   [Mixture]

Problem : How many liters of pure antifreeze must be added to 6 L of a 20% antifreeze mix to get a 40% mix?
Let     : x = liters of pure antifreeze
Equation: 0.2(6) + x = 0.4(6 + x)
Solve   : 0.6x = 1.2 → x = 2
Answer  : 2 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0542'
KEY = 'mixture/0542'
NAME = 'Mixture 0542'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of pure antifreeze must be added to 6 L of a 20% antifreeze mix to get a 40% mix?'
LET = 'x = liters of pure antifreeze'
EQUATION = '0.2(6) + x = 0.4(6 + x)'
SOLVE = '0.6x = 1.2 → x = 2'
ANSWER = '2 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of pure antifreeze must be added to {0} L of a {1}% antifreeze mix to get a {2}% mix?'
NUMBERS = ['6', '20', '40']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

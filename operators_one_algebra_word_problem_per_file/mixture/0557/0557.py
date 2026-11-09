"""Algebra word problem 0557   [Mixture]

Problem : A 24-liter radiator holds a 40% antifreeze mix. How much must be drained and replaced with pure antifreeze to raise it to 60%?
Let     : x = liters replaced
Equation: 0.4(24 − x) + x = 0.6(24)
Solve   : 0.6x = 4.8 → x = 8
Answer  : 8 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0557'
KEY = 'mixture/0557'
NAME = 'Mixture 0557'
CATEGORY = 'Mixture'
PROBLEM = 'A 24-liter radiator holds a 40% antifreeze mix. How much must be drained and replaced with pure antifreeze to raise it to 60%?'
LET = 'x = liters replaced'
EQUATION = '0.4(24 − x) + x = 0.6(24)'
SOLVE = '0.6x = 4.8 → x = 8'
ANSWER = '8 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0}-liter radiator holds a {1}% antifreeze mix. How much must be drained and replaced with pure antifreeze to raise it to {2}%?'
NUMBERS = ['24', '40', '60']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

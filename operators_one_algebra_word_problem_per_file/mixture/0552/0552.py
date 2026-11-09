"""Algebra word problem 0552   [Mixture]

Problem : A 30-liter radiator holds a 50% antifreeze mix. How much must be drained and replaced with pure antifreeze to raise it to 70%?
Let     : x = liters replaced
Equation: 0.5(30 − x) + x = 0.7(30)
Solve   : x/2 = 6 → x = 6 × 2 = 12
Answer  : 12 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0552'
KEY = 'mixture/0552'
NAME = 'Mixture 0552'
CATEGORY = 'Mixture'
PROBLEM = 'A 30-liter radiator holds a 50% antifreeze mix. How much must be drained and replaced with pure antifreeze to raise it to 70%?'
LET = 'x = liters replaced'
EQUATION = '0.5(30 − x) + x = 0.7(30)'
SOLVE = 'x/2 = 6 → x = 6 × 2 = 12'
ANSWER = '12 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0}-liter radiator holds a {1}% antifreeze mix. How much must be drained and replaced with pure antifreeze to raise it to {2}%?'
NUMBERS = ['30', '50', '70']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

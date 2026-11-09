"""Algebra word problem 0193   [Formula]

Problem : An object has a mass of 84 g and a density of 2 g/cm³. Using density = mass/volume, find its volume.
Let     : v = volume
Equation: 2v = 84
Solve   : 2v = 84 → v = 42
Answer  : 42 cm³

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0193'
KEY = 'formula/0193'
NAME = 'Formula 0193'
CATEGORY = 'Formula'
PROBLEM = 'An object has a mass of 84 g and a density of 2 g/cm³. Using density = mass/volume, find its volume.'
LET = 'v = volume'
EQUATION = '2v = 84'
SOLVE = '2v = 84 → v = 42'
ANSWER = '42 cm³'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An object has a mass of {0} g and a density of {1} g/cm³. Using density = mass/volume, find its volume.'
NUMBERS = ['84', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

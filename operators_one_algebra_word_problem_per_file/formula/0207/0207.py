"""Algebra word problem 0207   [Formula]

Problem : An object has a mass of 115 g and a density of 2.5 g/cm³. Using density = mass/volume, find its volume.
Let     : v = volume
Equation: 2.5v = 115
Solve   : 2.5v = 115 → v = 46
Answer  : 46 cm³

Status  : ready: archive_formula_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0207'
KEY = 'formula/0207'
NAME = 'Formula 0207'
CATEGORY = 'Formula'
PROBLEM = 'An object has a mass of 115 g and a density of 2.5 g/cm³. Using density = mass/volume, find its volume.'
LET = 'v = volume'
EQUATION = '2.5v = 115'
SOLVE = '2.5v = 115 → v = 46'
ANSWER = '46 cm³'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_formula_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An object has a mass of {0} g and a density of {1} g/cm³. Using density = mass/volume, find its volume.'
NUMBERS = ['115', '2.5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

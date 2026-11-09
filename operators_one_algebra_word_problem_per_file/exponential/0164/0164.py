"""Algebra word problem 0164   [Exponential]

Problem : A substance has a half-life of 2 years. How long until 200 g decays to 25 g?
Let     : t = years
Equation: 200 × (1/2)^(t/2) = 25
Solve   : (1/2)^(t/2) = 1/8 → t/2 = 3 → t = 6
Answer  : 6 years

Status  : ready: periodic_growth answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0164'
KEY = 'exponential/0164'
NAME = 'Exponential 0164'
CATEGORY = 'Exponential'
PROBLEM = 'A substance has a half-life of 2 years. How long until 200 g decays to 25 g?'
LET = 't = years'
EQUATION = '200 × (1/2)^(t/2) = 25'
SOLVE = '(1/2)^(t/2) = 1/8 → t/2 = 3 → t = 6'
ANSWER = '6 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'periodic_growth'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A substance has a half-life of {0} years. How long until {1} g decays to {2} g?'
NUMBERS = ['2', '200', '25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

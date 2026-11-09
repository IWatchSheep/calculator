"""Algebra word problem 0176   [Exponential]

Problem : A bacteria culture starts with 250 cells and doubles every 2 hours. When will it reach 1,000 cells?
Let     : t = hours
Equation: 250 × 2^(t/2) = 1000
Solve   : 2^(t/2) = 4 = 2^2 → t/2 = 2 → t = 4
Answer  : 4 hours

Status  : ready: periodic_growth answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0176'
KEY = 'exponential/0176'
NAME = 'Exponential 0176'
CATEGORY = 'Exponential'
PROBLEM = 'A bacteria culture starts with 250 cells and doubles every 2 hours. When will it reach 1,000 cells?'
LET = 't = hours'
EQUATION = '250 × 2^(t/2) = 1000'
SOLVE = '2^(t/2) = 4 = 2^2 → t/2 = 2 → t = 4'
ANSWER = '4 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'periodic_growth'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A bacteria culture starts with {0} cells and doubles every {1} hours. When will it reach {2} cells?'
NUMBERS = ['250', '2', '1000']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

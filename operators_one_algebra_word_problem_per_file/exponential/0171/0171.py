"""Algebra word problem 0171   [Exponential]

Problem : A bacteria culture starts with 200 cells and doubles every 6 hours. When will it reach 6,400 cells?
Let     : t = hours
Equation: 200 × 2^(t/6) = 6400
Solve   : 2^(t/6) = 32 = 2^5 → t/6 = 5 → t = 30
Answer  : 30 hours

Status  : ready: periodic_growth answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0171'
KEY = 'exponential/0171'
NAME = 'Exponential 0171'
CATEGORY = 'Exponential'
PROBLEM = 'A bacteria culture starts with 200 cells and doubles every 6 hours. When will it reach 6,400 cells?'
LET = 't = hours'
EQUATION = '200 × 2^(t/6) = 6400'
SOLVE = '2^(t/6) = 32 = 2^5 → t/6 = 5 → t = 30'
ANSWER = '30 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'periodic_growth'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A bacteria culture starts with {0} cells and doubles every {1} hours. When will it reach {2} cells?'
NUMBERS = ['200', '6', '6400']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

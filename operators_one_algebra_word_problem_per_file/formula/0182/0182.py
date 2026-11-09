"""Algebra word problem 0182   [Formula]

Problem : At what Celsius temperature is the Fahrenheit reading exactly 2 times the Celsius reading? (F = (9/5)C + 32)
Let     : c = degrees Celsius
Equation: (9/5)c + 32 = 2c
Solve   : c/5 = 32 → c = 32 × 5 = 160
Answer  : 160°C (320°F)

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0182'
KEY = 'formula/0182'
NAME = 'Formula 0182'
CATEGORY = 'Formula'
PROBLEM = 'At what Celsius temperature is the Fahrenheit reading exactly 2 times the Celsius reading? (F = (9/5)C + 32)'
LET = 'c = degrees Celsius'
EQUATION = '(9/5)c + 32 = 2c'
SOLVE = 'c/5 = 32 → c = 32 × 5 = 160'
ANSWER = '160°C (320°F)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At what Celsius temperature is the Fahrenheit reading exactly {0} times the Celsius reading? (F = ({1}/{2})C + {3})'
NUMBERS = ['2', '9', '5', '32']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

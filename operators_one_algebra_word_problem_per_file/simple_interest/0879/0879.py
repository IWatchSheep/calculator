"""Algebra word problem 0879   [Simple interest]

Problem : $7,000.00 is split between two accounts paying 4% and 3% simple interest. Both accounts earn the same interest in a year. How much is in each?
Let     : x = amount at 4%
Equation: 0.04x = 0.03(7000 − x)
Solve   : 0.07x = 210 → x = 3000
Answer  : $3,000.00 at 4%, $4,000.00 at 3%

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0879'
KEY = 'simple_interest/0879'
NAME = 'Simple interest 0879'
CATEGORY = 'Simple interest'
PROBLEM = '$7,000.00 is split between two accounts paying 4% and 3% simple interest. Both accounts earn the same interest in a year. How much is in each?'
LET = 'x = amount at 4%'
EQUATION = '0.04x = 0.03(7000 − x)'
SOLVE = '0.07x = 210 → x = 3000'
ANSWER = '$3,000.00 at 4%, $4,000.00 at 3%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '${0} is split between two accounts paying {1}% and {2}% simple interest. Both accounts earn the same interest in a year. How much is in each?'
NUMBERS = ['7000.00', '4', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

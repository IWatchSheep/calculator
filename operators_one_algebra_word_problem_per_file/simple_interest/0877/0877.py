"""Algebra word problem 0877   [Simple interest]

Problem : $22,000.00 is split between two accounts paying 10% and 6% simple interest. Both accounts earn the same interest in a year. How much is in each?
Let     : x = amount at 10%
Equation: 0.1x = 0.06(22000 − x)
Solve   : 0.16x = 1320 → x = 8250
Answer  : $8,250.00 at 10%, $13,750.00 at 6%

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0877'
KEY = 'simple_interest/0877'
NAME = 'Simple interest 0877'
CATEGORY = 'Simple interest'
PROBLEM = '$22,000.00 is split between two accounts paying 10% and 6% simple interest. Both accounts earn the same interest in a year. How much is in each?'
LET = 'x = amount at 10%'
EQUATION = '0.1x = 0.06(22000 − x)'
SOLVE = '0.16x = 1320 → x = 8250'
ANSWER = '$8,250.00 at 10%, $13,750.00 at 6%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '${0} is split between two accounts paying {1}% and {2}% simple interest. Both accounts earn the same interest in a year. How much is in each?'
NUMBERS = ['22000.00', '10', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

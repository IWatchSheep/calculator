"""Algebra word problem 0864   [Simple interest]

Problem : $16,500.00 is split between two accounts paying 6% and 4% simple interest. Both accounts earn the same interest in a year. How much is in each?
Let     : x = amount at 6%
Equation: 0.06x = 0.04(16500 − x)
Solve   : x/10 = 660 → x = 660 × 10 = 6600
Answer  : $6,600.00 at 6%, $9,900.00 at 4%

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0864'
KEY = 'simple_interest/0864'
NAME = 'Simple interest 0864'
CATEGORY = 'Simple interest'
PROBLEM = '$16,500.00 is split between two accounts paying 6% and 4% simple interest. Both accounts earn the same interest in a year. How much is in each?'
LET = 'x = amount at 6%'
EQUATION = '0.06x = 0.04(16500 − x)'
SOLVE = 'x/10 = 660 → x = 660 × 10 = 6600'
ANSWER = '$6,600.00 at 6%, $9,900.00 at 4%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '${0} is split between two accounts paying {1}% and {2}% simple interest. Both accounts earn the same interest in a year. How much is in each?'
NUMBERS = ['16500.00', '6', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

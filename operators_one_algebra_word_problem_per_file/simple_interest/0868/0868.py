"""Algebra word problem 0868   [Simple interest]

Problem : $8,500.00 is split between two accounts paying 6% and 2% simple interest. Both accounts earn the same interest in a year. How much is in each?
Let     : x = amount at 6%
Equation: 0.06x = 0.02(8500 − x)
Solve   : 0.08x = 170 → x = 2125
Answer  : $2,125.00 at 6%, $6,375.00 at 2%

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0868'
KEY = 'simple_interest/0868'
NAME = 'Simple interest 0868'
CATEGORY = 'Simple interest'
PROBLEM = '$8,500.00 is split between two accounts paying 6% and 2% simple interest. Both accounts earn the same interest in a year. How much is in each?'
LET = 'x = amount at 6%'
EQUATION = '0.06x = 0.02(8500 − x)'
SOLVE = '0.08x = 170 → x = 2125'
ANSWER = '$2,125.00 at 6%, $6,375.00 at 2%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '${0} is split between two accounts paying {1}% and {2}% simple interest. Both accounts earn the same interest in a year. How much is in each?'
NUMBERS = ['8500.00', '6', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

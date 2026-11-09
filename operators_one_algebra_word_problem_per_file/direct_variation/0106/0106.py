"""Algebra word problem 0106   [Direct variation]

Problem : Pay varies directly with hours worked. Kira earns $900.00 for 40 hours. How much for 42 hours?
Let     : k = hourly rate
Equation: 900 = k·40; pay = k·42
Solve   : k = 22.5 → pay = 945
Answer  : $945.00

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0106'
KEY = 'direct_variation/0106'
NAME = 'Direct variation 0106'
CATEGORY = 'Direct variation'
PROBLEM = 'Pay varies directly with hours worked. Kira earns $900.00 for 40 hours. How much for 42 hours?'
LET = 'k = hourly rate'
EQUATION = '900 = k·40; pay = k·42'
SOLVE = 'k = 22.5 → pay = 945'
ANSWER = '$945.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pay varies directly with hours worked. Kira earns ${0} for {1} hours. How much for {2} hours?'
NUMBERS = ['900.00', '40', '42']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

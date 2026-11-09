"""Algebra word problem 0113   [Direct variation]

Problem : Pay varies directly with hours worked. Kira earns $765.00 for 34 hours. How much for 28 hours?
Let     : k = hourly rate
Equation: 765 = k·34; pay = k·28
Solve   : k = 22.5 → pay = 630
Answer  : $630.00

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0113'
KEY = 'direct_variation/0113'
NAME = 'Direct variation 0113'
CATEGORY = 'Direct variation'
PROBLEM = 'Pay varies directly with hours worked. Kira earns $765.00 for 34 hours. How much for 28 hours?'
LET = 'k = hourly rate'
EQUATION = '765 = k·34; pay = k·28'
SOLVE = 'k = 22.5 → pay = 630'
ANSWER = '$630.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pay varies directly with hours worked. Kira earns ${0} for {1} hours. How much for {2} hours?'
NUMBERS = ['765.00', '34', '28']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0108   [Direct variation]

Problem : Pay varies directly with hours worked. Priya earns $450.00 for 30 hours. How much for 6 hours?
Let     : k = hourly rate
Equation: 450 = k·30; pay = k·6
Solve   : k = 15 → pay = 90
Answer  : $90.00

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0108'
KEY = 'direct_variation/0108'
NAME = 'Direct variation 0108'
CATEGORY = 'Direct variation'
PROBLEM = 'Pay varies directly with hours worked. Priya earns $450.00 for 30 hours. How much for 6 hours?'
LET = 'k = hourly rate'
EQUATION = '450 = k·30; pay = k·6'
SOLVE = 'k = 15 → pay = 90'
ANSWER = '$90.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pay varies directly with hours worked. Priya earns ${0} for {1} hours. How much for {2} hours?'
NUMBERS = ['450.00', '30', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

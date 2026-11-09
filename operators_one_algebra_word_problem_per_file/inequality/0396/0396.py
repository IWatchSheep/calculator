"""Algebra word problem 0396   [Inequality]

Problem : A rectangular garden is 43 ft long, and there is at most 90 ft of fencing. What is the greatest whole-number width possible?
Let     : w = width
Equation: 2(43) + 2w ≤ 90
Solve   : w ≤ 2 → w = 2 (largest whole number that works)
Answer  : 2 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0396'
KEY = 'inequality/0396'
NAME = 'Inequality 0396'
CATEGORY = 'Inequality'
PROBLEM = 'A rectangular garden is 43 ft long, and there is at most 90 ft of fencing. What is the greatest whole-number width possible?'
LET = 'w = width'
EQUATION = '2(43) + 2w ≤ 90'
SOLVE = 'w ≤ 2 → w = 2 (largest whole number that works)'
ANSWER = '2 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangular garden is {0} ft long, and there is at most {1} ft of fencing. What is the greatest whole-number width possible?'
NUMBERS = ['43', '90']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

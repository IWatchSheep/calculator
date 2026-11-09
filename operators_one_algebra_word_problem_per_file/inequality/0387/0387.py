"""Algebra word problem 0387   [Inequality]

Problem : A rectangular garden is 21 ft long, and there is at most 52 ft of fencing. What is the greatest whole-number width possible?
Let     : w = width
Equation: 2(21) + 2w ≤ 52
Solve   : w ≤ 5 → w = 5 (largest whole number that works)
Answer  : 5 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0387'
KEY = 'inequality/0387'
NAME = 'Inequality 0387'
CATEGORY = 'Inequality'
PROBLEM = 'A rectangular garden is 21 ft long, and there is at most 52 ft of fencing. What is the greatest whole-number width possible?'
LET = 'w = width'
EQUATION = '2(21) + 2w ≤ 52'
SOLVE = 'w ≤ 5 → w = 5 (largest whole number that works)'
ANSWER = '5 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rectangular garden is {0} ft long, and there is at most {1} ft of fencing. What is the greatest whole-number width possible?'
NUMBERS = ['21', '52']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

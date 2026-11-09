"""Algebra word problem 0386   [Inequality]

Problem : Lena's test scores are 93, 83, 85. What is the lowest score on the next test that gives an average of at least 88?
Let     : x = next score
Equation: (93 + 83 + 85 + x)/4 ≥ 88
Solve   : x ≥ 91 → x = 91 (smallest whole number that works)
Answer  : 91

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0386'
KEY = 'inequality/0386'
NAME = 'Inequality 0386'
CATEGORY = 'Inequality'
PROBLEM = "Lena's test scores are 93, 83, 85. What is the lowest score on the next test that gives an average of at least 88?"
LET = 'x = next score'
EQUATION = '(93 + 83 + 85 + x)/4 ≥ 88'
SOLVE = 'x ≥ 91 → x = 91 (smallest whole number that works)'
ANSWER = '91'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "Lena's test scores are {0}, {1}, {2}. What is the lowest score on the next test that gives an average of at least {3}?"
NUMBERS = ['93', '83', '85', '88']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

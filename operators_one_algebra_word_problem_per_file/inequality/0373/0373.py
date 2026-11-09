"""Algebra word problem 0373   [Inequality]

Problem : Lena's test scores are 81, 88, 63, 78, 85. What is the lowest score on the next test that gives an average of at least 80?
Let     : x = next score
Equation: (81 + 88 + 63 + 78 + 85 + x)/6 ≥ 80
Solve   : x ≥ 85 → x = 85 (smallest whole number that works)
Answer  : 85

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0373'
KEY = 'inequality/0373'
NAME = 'Inequality 0373'
CATEGORY = 'Inequality'
PROBLEM = "Lena's test scores are 81, 88, 63, 78, 85. What is the lowest score on the next test that gives an average of at least 80?"
LET = 'x = next score'
EQUATION = '(81 + 88 + 63 + 78 + 85 + x)/6 ≥ 80'
SOLVE = 'x ≥ 85 → x = 85 (smallest whole number that works)'
ANSWER = '85'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "Lena's test scores are {0}, {1}, {2}, {3}, {4}. What is the lowest score on the next test that gives an average of at least {5}?"
NUMBERS = ['81', '88', '63', '78', '85', '80']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

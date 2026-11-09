"""Algebra word problem 0366   [Inequality]

Problem : Isla's test scores are 94, 64. What is the lowest score on the next test that gives an average of at least 85?
Let     : x = next score
Equation: (94 + 64 + x)/3 ≥ 85
Solve   : x ≥ 97 → x = 97 (smallest whole number that works)
Answer  : 97

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0366'
KEY = 'inequality/0366'
NAME = 'Inequality 0366'
CATEGORY = 'Inequality'
PROBLEM = "Isla's test scores are 94, 64. What is the lowest score on the next test that gives an average of at least 85?"
LET = 'x = next score'
EQUATION = '(94 + 64 + x)/3 ≥ 85'
SOLVE = 'x ≥ 97 → x = 97 (smallest whole number that works)'
ANSWER = '97'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "Isla's test scores are {0}, {1}. What is the lowest score on the next test that gives an average of at least {2}?"
NUMBERS = ['94', '64', '85']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

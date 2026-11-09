"""Algebra word problem 0098   [Digits]

Problem : The digits of a two-digit number add up to 12. When the digits are reversed, the new number is 18 more than the original. Find the original number.
Let     : t = tens digit, u = units digit
Equation: t + u = 12;  (10u + t) − (10t + u) = 18
Solve   : 9(u − t) = 18 → u − t = 2; with t + u = 12: t = 5, u = 7
Answer  : 57

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0098'
KEY = 'digits/0098'
NAME = 'Digits 0098'
CATEGORY = 'Digits'
PROBLEM = 'The digits of a two-digit number add up to 12. When the digits are reversed, the new number is 18 more than the original. Find the original number.'
LET = 't = tens digit, u = units digit'
EQUATION = 't + u = 12;  (10u + t) − (10t + u) = 18'
SOLVE = '9(u − t) = 18 → u − t = 2; with t + u = 12: t = 5, u = 7'
ANSWER = '57'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The digits of a two-digit number add up to {0}. When the digits are reversed, the new number is {1} more than the original. Find the original number.'
NUMBERS = ['12', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

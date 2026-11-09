"""Algebra word problem 0104   [Digits]

Problem : The digits of a two-digit number add up to 14. When the digits are reversed, the new number is 36 less than the original. Find the original number.
Let     : t = tens digit, u = units digit
Equation: t + u = 14;  (10u + t) − (10t + u) = -36
Solve   : 9(u − t) = -36 → u − t = -4; with t + u = 14: t = 9, u = 5
Answer  : 95

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0104'
KEY = 'digits/0104'
NAME = 'Digits 0104'
CATEGORY = 'Digits'
PROBLEM = 'The digits of a two-digit number add up to 14. When the digits are reversed, the new number is 36 less than the original. Find the original number.'
LET = 't = tens digit, u = units digit'
EQUATION = 't + u = 14;  (10u + t) − (10t + u) = -36'
SOLVE = '9(u − t) = -36 → u − t = -4; with t + u = 14: t = 9, u = 5'
ANSWER = '95'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The digits of a two-digit number add up to {0}. When the digits are reversed, the new number is {1} less than the original. Find the original number.'
NUMBERS = ['14', '36']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

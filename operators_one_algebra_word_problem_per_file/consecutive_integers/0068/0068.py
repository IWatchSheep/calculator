"""Algebra word problem 0068   [Consecutive integers]

Problem : The average of 5 consecutive integers is 50. What is the smallest?
Let     : x = smallest
Equation: (x + (x + 4))/2 = 50
Solve   : Collect like terms → x = 48
Answer  : 48 (the integers are 48 to 52)

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0068'
KEY = 'consecutive_integers/0068'
NAME = 'Consecutive integers 0068'
CATEGORY = 'Consecutive integers'
PROBLEM = 'The average of 5 consecutive integers is 50. What is the smallest?'
LET = 'x = smallest'
EQUATION = '(x + (x + 4))/2 = 50'
SOLVE = 'Collect like terms → x = 48'
ANSWER = '48 (the integers are 48 to 52)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The average of {0} consecutive integers is {1}. What is the smallest?'
NUMBERS = ['5', '50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

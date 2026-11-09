"""Algebra word problem 0017   [Average]

Problem : The mean of 5 numbers is 31. 4 of them are 56, 5, 30, 30. What is the missing number?
Let     : x = missing number
Equation: (56 + 5 + 30 + 30 + x)/5 = 31
Solve   : x/5 = 6.8 → x = 6.8 × 5 = 34
Answer  : 34

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0017'
KEY = 'average/0017'
NAME = 'Average 0017'
CATEGORY = 'Average'
PROBLEM = 'The mean of 5 numbers is 31. 4 of them are 56, 5, 30, 30. What is the missing number?'
LET = 'x = missing number'
EQUATION = '(56 + 5 + 30 + 30 + x)/5 = 31'
SOLVE = 'x/5 = 6.8 → x = 6.8 × 5 = 34'
ANSWER = '34'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The mean of {0} numbers is {1}. {2} of them are {3}, {4}, {5}, {6}. What is the missing number?'
NUMBERS = ['5', '31', '4', '56', '5', '30', '30']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

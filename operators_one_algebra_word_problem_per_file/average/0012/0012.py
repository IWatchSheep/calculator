"""Algebra word problem 0012   [Average]

Problem : The mean of 4 numbers is 26. 3 of them are 9, 26, 50. What is the missing number?
Let     : x = missing number
Equation: (9 + 26 + 50 + x)/4 = 26
Solve   : x/4 = 4.75 → x = 4.75 × 4 = 19
Answer  : 19

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0012'
KEY = 'average/0012'
NAME = 'Average 0012'
CATEGORY = 'Average'
PROBLEM = 'The mean of 4 numbers is 26. 3 of them are 9, 26, 50. What is the missing number?'
LET = 'x = missing number'
EQUATION = '(9 + 26 + 50 + x)/4 = 26'
SOLVE = 'x/4 = 4.75 → x = 4.75 × 4 = 19'
ANSWER = '19'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The mean of {0} numbers is {1}. {2} of them are {3}, {4}, {5}. What is the missing number?'
NUMBERS = ['4', '26', '3', '9', '26', '50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

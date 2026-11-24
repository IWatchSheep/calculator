"""Algebra word problem 0950   [System of equations (3 variables)]

Problem : An apple, a banana, and a cherry cup cost $4.05 together. Two apples and a banana cost $3.40. An apple and two cherry cups cost $4.60. Find each price.
Let     : a, b, c = prices
Equation: a + b + c = 4.05;  2a + b = 3.4;  a + 2c = 4.6
Solve   : From eq 2: b = 3.4 − 2a; from eq 3: c = (4.6 − a)/2; substitute into eq 1 → a = 1.1, b = 1.2, c = 1.75
Answer  : apple $1.10, banana $1.20, cherry cup $1.75

Status  : ready: three_item_prices answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0950'
KEY = 'system_of_equations_3_variables/0950'
NAME = 'System of equations (3 variables) 0950'
CATEGORY = 'System of equations (3 variables)'
PROBLEM = 'An apple, a banana, and a cherry cup cost $4.05 together. Two apples and a banana cost $3.40. An apple and two cherry cups cost $4.60. Find each price.'
LET = 'a, b, c = prices'
EQUATION = 'a + b + c = 4.05;  2a + b = 3.4;  a + 2c = 4.6'
SOLVE = 'From eq 2: b = 3.4 − 2a; from eq 3: c = (4.6 − a)/2; substitute into eq 1 → a = 1.1, b = 1.2, c = 1.75'
ANSWER = 'apple $1.10, banana $1.20, cherry cup $1.75'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'three_item_prices'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An apple, a banana, and a cherry cup cost ${0} together. Two apples and a banana cost ${1}. An apple and two cherry cups cost ${2}. Find each price.'
NUMBERS = ['4.05', '3.40', '4.60']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

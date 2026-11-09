"""Algebra word problem 0952   [System of equations (3 variables)]

Problem : An apple, a banana, and a cherry cup cost $3.85 together. Two apples and a banana cost $3.05. A banana and two cherry cups cost $4.65. Find each price.
Let     : a, b, c = prices
Equation: a + b + c = 3.85;  2a + b = 3.05;  b + 2c = 4.65
Solve   : Subtract eq 1 from eq 2: a − c = -0.8; substitute into eq 3 → a = 0.6, b = 1.85, c = 1.4
Answer  : apple $0.60, banana $1.85, cherry cup $1.40

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0952'
KEY = 'system_of_equations_3_variables/0952'
NAME = 'System of equations (3 variables) 0952'
CATEGORY = 'System of equations (3 variables)'
PROBLEM = 'An apple, a banana, and a cherry cup cost $3.85 together. Two apples and a banana cost $3.05. A banana and two cherry cups cost $4.65. Find each price.'
LET = 'a, b, c = prices'
EQUATION = 'a + b + c = 3.85;  2a + b = 3.05;  b + 2c = 4.65'
SOLVE = 'Subtract eq 1 from eq 2: a − c = -0.8; substitute into eq 3 → a = 0.6, b = 1.85, c = 1.4'
ANSWER = 'apple $0.60, banana $1.85, cherry cup $1.40'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An apple, a banana, and a cherry cup cost ${0} together. Two apples and a banana cost ${1}. A banana and two cherry cups cost ${2}. Find each price.'
NUMBERS = ['3.85', '3.05', '4.65']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

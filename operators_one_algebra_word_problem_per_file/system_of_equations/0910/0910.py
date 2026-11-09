"""Algebra word problem 0910   [System of equations]

Problem : Two numbers x and y satisfy 4x + 5y = -41 and −2x − 3y = 25. Find x and y.
Let     : x, y = the numbers
Equation: 4x + 5y = -41;  −2x − 3y = 25
Solve   : Solve by elimination → x = 1, y = -9
Answer  : x = 1, y = -9

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0910'
KEY = 'system_of_equations/0910'
NAME = 'System of equations 0910'
CATEGORY = 'System of equations'
PROBLEM = 'Two numbers x and y satisfy 4x + 5y = -41 and −2x − 3y = 25. Find x and y.'
LET = 'x, y = the numbers'
EQUATION = '4x + 5y = -41;  −2x − 3y = 25'
SOLVE = 'Solve by elimination → x = 1, y = -9'
ANSWER = 'x = 1, y = -9'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two numbers x and y satisfy {0}x + {1}y = -{2} and −{3}x − {4}y = {5}. Find x and y.'
NUMBERS = ['4', '5', '41', '2', '3', '25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

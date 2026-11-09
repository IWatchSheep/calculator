"""Algebra word problem 0928   [System of equations]

Problem : Two numbers x and y satisfy −x + 3y = 3 and 5x − 2y = -41. Find x and y.
Let     : x, y = the numbers
Equation: −x + 3y = 3;  5x − 2y = -41
Solve   : Solve by elimination → x = -9, y = -2
Answer  : x = -9, y = -2

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0928'
KEY = 'system_of_equations/0928'
NAME = 'System of equations 0928'
CATEGORY = 'System of equations'
PROBLEM = 'Two numbers x and y satisfy −x + 3y = 3 and 5x − 2y = -41. Find x and y.'
LET = 'x, y = the numbers'
EQUATION = '−x + 3y = 3;  5x − 2y = -41'
SOLVE = 'Solve by elimination → x = -9, y = -2'
ANSWER = 'x = -9, y = -2'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two numbers x and y satisfy −x + {0}y = {1} and {2}x − {3}y = -{4}. Find x and y.'
NUMBERS = ['3', '3', '5', '2', '41']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

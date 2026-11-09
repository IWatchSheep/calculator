"""Algebra word problem 0927   [System of equations]

Problem : A farm packed 1026 eggs into 45 cartons, using cartons of 12 and cartons of 30. All cartons were full. How many of each?
Let     : x = cartons of 12, y = cartons of 30
Equation: x + y = 45;  12x + 30y = 1026
Solve   : Solve by elimination → x = 18, y = 27
Answer  : 18 of 12, 27 of 30

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0927'
KEY = 'system_of_equations/0927'
NAME = 'System of equations 0927'
CATEGORY = 'System of equations'
PROBLEM = 'A farm packed 1026 eggs into 45 cartons, using cartons of 12 and cartons of 30. All cartons were full. How many of each?'
LET = 'x = cartons of 12, y = cartons of 30'
EQUATION = 'x + y = 45;  12x + 30y = 1026'
SOLVE = 'Solve by elimination → x = 18, y = 27'
ANSWER = '18 of 12, 27 of 30'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A farm packed {0} eggs into {1} cartons, using cartons of {2} and cartons of {3}. All cartons were full. How many of each?'
NUMBERS = ['1026', '45', '12', '30']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

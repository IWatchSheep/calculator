"""Algebra word problem 0914   [System of equations]

Problem : A banquet hall seats 52 guests at 8 tables. Some tables seat 4 and the others seat 8. How many of each kind are there?
Let     : x = 4-seat tables, y = 8-seat tables
Equation: x + y = 8;  4x + 8y = 52
Solve   : Solve by elimination → x = 3, y = 5
Answer  : 3 tables of 4, 5 tables of 8

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0914'
KEY = 'system_of_equations/0914'
NAME = 'System of equations 0914'
CATEGORY = 'System of equations'
PROBLEM = 'A banquet hall seats 52 guests at 8 tables. Some tables seat 4 and the others seat 8. How many of each kind are there?'
LET = 'x = 4-seat tables, y = 8-seat tables'
EQUATION = 'x + y = 8;  4x + 8y = 52'
SOLVE = 'Solve by elimination → x = 3, y = 5'
ANSWER = '3 tables of 4, 5 tables of 8'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A banquet hall seats {0} guests at {1} tables. Some tables seat {2} and the others seat {3}. How many of each kind are there?'
NUMBERS = ['52', '8', '4', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

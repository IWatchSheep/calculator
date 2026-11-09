"""Algebra word problem 0940   [System of equations]

Problem : A banquet hall seats 50 guests at 19 tables. Some tables seat 2 and the others seat 4. How many of each kind are there?
Let     : x = 2-seat tables, y = 4-seat tables
Equation: x + y = 19;  2x + 4y = 50
Solve   : Solve by elimination → x = 13, y = 6
Answer  : 13 tables of 2, 6 tables of 4

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0940'
KEY = 'system_of_equations/0940'
NAME = 'System of equations 0940'
CATEGORY = 'System of equations'
PROBLEM = 'A banquet hall seats 50 guests at 19 tables. Some tables seat 2 and the others seat 4. How many of each kind are there?'
LET = 'x = 2-seat tables, y = 4-seat tables'
EQUATION = 'x + y = 19;  2x + 4y = 50'
SOLVE = 'Solve by elimination → x = 13, y = 6'
ANSWER = '13 tables of 2, 6 tables of 4'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A banquet hall seats {0} guests at {1} tables. Some tables seat {2} and the others seat {3}. How many of each kind are there?'
NUMBERS = ['50', '19', '2', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0934   [System of equations]

Problem : A camp rents 19 canoes for 88 campers, filling every seat. Some canoes hold 4 people and the rest hold 6. How many of each were rented?
Let     : x = 4-person, y = 6-person
Equation: x + y = 19;  4x + 6y = 88
Solve   : Solve by elimination → x = 13, y = 6
Answer  : 13 4-person and 6 6-person

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0934'
KEY = 'system_of_equations/0934'
NAME = 'System of equations 0934'
CATEGORY = 'System of equations'
PROBLEM = 'A camp rents 19 canoes for 88 campers, filling every seat. Some canoes hold 4 people and the rest hold 6. How many of each were rented?'
LET = 'x = 4-person, y = 6-person'
EQUATION = 'x + y = 19;  4x + 6y = 88'
SOLVE = 'Solve by elimination → x = 13, y = 6'
ANSWER = '13 4-person and 6 6-person'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A camp rents {0} canoes for {1} campers, filling every seat. Some canoes hold {2} people and the rest hold {3}. How many of each were rented?'
NUMBERS = ['19', '88', '4', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

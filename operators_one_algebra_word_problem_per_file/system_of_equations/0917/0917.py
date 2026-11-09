"""Algebra word problem 0917   [System of equations]

Problem : A camp rents 16 canoes for 38 campers, filling every seat. Some canoes hold 2 people and the rest hold 4. How many of each were rented?
Let     : x = 2-person, y = 4-person
Equation: x + y = 16;  2x + 4y = 38
Solve   : Solve by elimination → x = 13, y = 3
Answer  : 13 2-person and 3 4-person

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0917'
KEY = 'system_of_equations/0917'
NAME = 'System of equations 0917'
CATEGORY = 'System of equations'
PROBLEM = 'A camp rents 16 canoes for 38 campers, filling every seat. Some canoes hold 2 people and the rest hold 4. How many of each were rented?'
LET = 'x = 2-person, y = 4-person'
EQUATION = 'x + y = 16;  2x + 4y = 38'
SOLVE = 'Solve by elimination → x = 13, y = 3'
ANSWER = '13 2-person and 3 4-person'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A camp rents {0} canoes for {1} campers, filling every seat. Some canoes hold {2} people and the rest hold {3}. How many of each were rented?'
NUMBERS = ['16', '38', '2', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

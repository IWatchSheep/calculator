"""Algebra word problem 0951   [System of equations (3 variables)]

Problem : Three numbers add up to 21. The first plus the second is 10, and the second plus the third is 12. Find all three.
Let     : x, y, z = the numbers
Equation: x + y + z = 21;  x + y = 10;  y + z = 12
Solve   : z = 21 − 10 = 11; x = 21 − 12 = 9; y = 10 − 9 = 1 → x = 9, y = 1, z = 11
Answer  : 9, 1, 11

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0951'
KEY = 'system_of_equations_3_variables/0951'
NAME = 'System of equations (3 variables) 0951'
CATEGORY = 'System of equations (3 variables)'
PROBLEM = 'Three numbers add up to 21. The first plus the second is 10, and the second plus the third is 12. Find all three.'
LET = 'x, y, z = the numbers'
EQUATION = 'x + y + z = 21;  x + y = 10;  y + z = 12'
SOLVE = 'z = 21 − 10 = 11; x = 21 − 12 = 9; y = 10 − 9 = 1 → x = 9, y = 1, z = 11'
ANSWER = '9, 1, 11'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Three numbers add up to {0}. The first plus the second is {1}, and the second plus the third is {2}. Find all three.'
NUMBERS = ['21', '10', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

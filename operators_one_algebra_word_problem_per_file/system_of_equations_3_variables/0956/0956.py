"""Algebra word problem 0956   [System of equations (3 variables)]

Problem : Three numbers add up to 33. The first plus the second is 29, and the second plus the third is 20. Find all three.
Let     : x, y, z = the numbers
Equation: x + y + z = 33;  x + y = 29;  y + z = 20
Solve   : z = 33 − 29 = 4; x = 33 − 20 = 13; y = 29 − 13 = 16 → x = 13, y = 16, z = 4
Answer  : 13, 16, 4

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0956'
KEY = 'system_of_equations_3_variables/0956'
NAME = 'System of equations (3 variables) 0956'
CATEGORY = 'System of equations (3 variables)'
PROBLEM = 'Three numbers add up to 33. The first plus the second is 29, and the second plus the third is 20. Find all three.'
LET = 'x, y, z = the numbers'
EQUATION = 'x + y + z = 33;  x + y = 29;  y + z = 20'
SOLVE = 'z = 33 − 29 = 4; x = 33 − 20 = 13; y = 29 − 13 = 16 → x = 13, y = 16, z = 4'
ANSWER = '13, 16, 4'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Three numbers add up to {0}. The first plus the second is {1}, and the second plus the third is {2}. Find all three.'
NUMBERS = ['33', '29', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

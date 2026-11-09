"""Algebra word problem 0955   [System of equations (3 variables)]

Problem : Three numbers add up to 40. The first plus the second is 27, and the second plus the third is 24. Find all three.
Let     : x, y, z = the numbers
Equation: x + y + z = 40;  x + y = 27;  y + z = 24
Solve   : z = 40 − 27 = 13; x = 40 − 24 = 16; y = 27 − 16 = 11 → x = 16, y = 11, z = 13
Answer  : 16, 11, 13

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0955'
KEY = 'system_of_equations_3_variables/0955'
NAME = 'System of equations (3 variables) 0955'
CATEGORY = 'System of equations (3 variables)'
PROBLEM = 'Three numbers add up to 40. The first plus the second is 27, and the second plus the third is 24. Find all three.'
LET = 'x, y, z = the numbers'
EQUATION = 'x + y + z = 40;  x + y = 27;  y + z = 24'
SOLVE = 'z = 40 − 27 = 13; x = 40 − 24 = 16; y = 27 − 16 = 11 → x = 16, y = 11, z = 13'
ANSWER = '16, 11, 13'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Three numbers add up to {0}. The first plus the second is {1}, and the second plus the third is {2}. Find all three.'
NUMBERS = ['40', '27', '24']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0735   [Quadratic]

Problem : A polygon has 9 diagonals. Using D = n(n − 3)/2, how many sides does it have?
Let     : n = number of sides
Equation: n(n − 3)/2 = 9
Solve   : n² − 3n − 18 = 0 → n = 6 (the other root, -3, is rejected)
Answer  : 6 sides

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0735'
KEY = 'quadratic/0735'
NAME = 'Quadratic 0735'
CATEGORY = 'Quadratic'
PROBLEM = 'A polygon has 9 diagonals. Using D = n(n − 3)/2, how many sides does it have?'
LET = 'n = number of sides'
EQUATION = 'n(n − 3)/2 = 9'
SOLVE = 'n² − 3n − 18 = 0 → n = 6 (the other root, -3, is rejected)'
ANSWER = '6 sides'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A polygon has {0} diagonals. Using D = n(n − {1})/{2}, how many sides does it have?'
NUMBERS = ['9', '3', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

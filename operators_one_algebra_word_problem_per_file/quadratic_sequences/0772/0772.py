"""Algebra word problem 0772   [Quadratic (sequences)]

Problem : How many consecutive whole numbers, starting from 1, must be added to get a sum of 55? (Use 1 + 2 + … + n = n(n + 1)/2.)
Let     : n = how many numbers
Equation: n(n + 1)/2 = 55
Solve   : n² + n − 110 = 0 → n = 10 (the other root, -11, is rejected)
Answer  : 10 numbers (1 through 10)

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0772'
KEY = 'quadratic_sequences/0772'
NAME = 'Quadratic (sequences) 0772'
CATEGORY = 'Quadratic (sequences)'
PROBLEM = 'How many consecutive whole numbers, starting from 1, must be added to get a sum of 55? (Use 1 + 2 + … + n = n(n + 1)/2.)'
LET = 'n = how many numbers'
EQUATION = 'n(n + 1)/2 = 55'
SOLVE = 'n² + n − 110 = 0 → n = 10 (the other root, -11, is rejected)'
ANSWER = '10 numbers (1 through 10)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many consecutive whole numbers, starting from {0}, must be added to get a sum of {1}? (Use {2} + {3} + … + n = n(n + {4})/{5}.)'
NUMBERS = ['1', '55', '1', '2', '1', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

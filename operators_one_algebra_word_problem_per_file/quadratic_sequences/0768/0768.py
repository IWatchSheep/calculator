"""Algebra word problem 0768   [Quadratic (sequences)]

Problem : How many consecutive whole numbers, starting from 1, must be added to get a sum of 28? (Use 1 + 2 + … + n = n(n + 1)/2.)
Let     : n = how many numbers
Equation: n(n + 1)/2 = 28
Solve   : n² + n − 56 = 0 → n = 7 (the other root, -8, is rejected)
Answer  : 7 numbers (1 through 7)

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0768'
KEY = 'quadratic_sequences/0768'
NAME = 'Quadratic (sequences) 0768'
CATEGORY = 'Quadratic (sequences)'
PROBLEM = 'How many consecutive whole numbers, starting from 1, must be added to get a sum of 28? (Use 1 + 2 + … + n = n(n + 1)/2.)'
LET = 'n = how many numbers'
EQUATION = 'n(n + 1)/2 = 28'
SOLVE = 'n² + n − 56 = 0 → n = 7 (the other root, -8, is rejected)'
ANSWER = '7 numbers (1 through 7)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many consecutive whole numbers, starting from {0}, must be added to get a sum of {1}? (Use {2} + {3} + … + n = n(n + {4})/{5}.)'
NUMBERS = ['1', '28', '1', '2', '1', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

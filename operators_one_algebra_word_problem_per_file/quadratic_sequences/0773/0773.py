"""Algebra word problem 0773   [Quadratic (sequences)]

Problem : A stack of cans has 5 cans in the top row, and each row below has 1 more than the row above. The stack has 26 cans in total. How many rows are there?
Let     : n = number of rows
Equation: (n/2)(2(5) + (n − 1)(1)) = 26
Solve   : n² + 9n − 52 = 0 → n = 4 (the other root, -13, is rejected)
Answer  : 4 rows

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0773'
KEY = 'quadratic_sequences/0773'
NAME = 'Quadratic (sequences) 0773'
CATEGORY = 'Quadratic (sequences)'
PROBLEM = 'A stack of cans has 5 cans in the top row, and each row below has 1 more than the row above. The stack has 26 cans in total. How many rows are there?'
LET = 'n = number of rows'
EQUATION = '(n/2)(2(5) + (n − 1)(1)) = 26'
SOLVE = 'n² + 9n − 52 = 0 → n = 4 (the other root, -13, is rejected)'
ANSWER = '4 rows'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A stack of cans has {0} cans in the top row, and each row below has {1} more than the row above. The stack has {2} cans in total. How many rows are there?'
NUMBERS = ['5', '1', '26']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

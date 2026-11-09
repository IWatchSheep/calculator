"""Algebra word problem 0858   [Sequences]

Problem : A theater has 23 seats in the first row and each row has 4 more seats than the row before. Which row has 83 seats?
Let     : n = row number
Equation: 23 + (n − 1)(4) = 83
Solve   : 4n = 64 → n = 16
Answer  : Row 16

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0858'
KEY = 'sequences/0858'
NAME = 'Sequences 0858'
CATEGORY = 'Sequences'
PROBLEM = 'A theater has 23 seats in the first row and each row has 4 more seats than the row before. Which row has 83 seats?'
LET = 'n = row number'
EQUATION = '23 + (n − 1)(4) = 83'
SOLVE = '4n = 64 → n = 16'
ANSWER = 'Row 16'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A theater has {0} seats in the first row and each row has {1} more seats than the row before. Which row has {2} seats?'
NUMBERS = ['23', '4', '83']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

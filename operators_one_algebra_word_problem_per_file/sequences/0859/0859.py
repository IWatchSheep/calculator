"""Algebra word problem 0859   [Sequences]

Problem : A theater has 14 seats in the first row and each row has 2 more seats than the row before. Which row has 58 seats?
Let     : n = row number
Equation: 14 + (n − 1)(2) = 58
Solve   : 2n = 46 → n = 23
Answer  : Row 23

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0859'
KEY = 'sequences/0859'
NAME = 'Sequences 0859'
CATEGORY = 'Sequences'
PROBLEM = 'A theater has 14 seats in the first row and each row has 2 more seats than the row before. Which row has 58 seats?'
LET = 'n = row number'
EQUATION = '14 + (n − 1)(2) = 58'
SOLVE = '2n = 46 → n = 23'
ANSWER = 'Row 23'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A theater has {0} seats in the first row and each row has {1} more seats than the row before. Which row has {2} seats?'
NUMBERS = ['14', '2', '58']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

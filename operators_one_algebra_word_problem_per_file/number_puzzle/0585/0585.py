"""Algebra word problem 0585   [Number puzzle]

Problem : Grace has 9 more than 4 times as many stamps as Uma. Together they have 139 stamps. How many does each have?
Let     : x = Uma's stamps
Equation: x + (4x + 9) = 139
Solve   : 5x = 130 → x = 26
Answer  : Uma: 26, Grace: 113

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0585'
KEY = 'number_puzzle/0585'
NAME = 'Number puzzle 0585'
CATEGORY = 'Number puzzle'
PROBLEM = 'Grace has 9 more than 4 times as many stamps as Uma. Together they have 139 stamps. How many does each have?'
LET = "x = Uma's stamps"
EQUATION = 'x + (4x + 9) = 139'
SOLVE = '5x = 130 → x = 26'
ANSWER = 'Uma: 26, Grace: 113'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Grace has {0} more than {1} times as many stamps as Uma. Together they have {2} stamps. How many does each have?'
NUMBERS = ['9', '4', '139']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0611   [Number puzzle]

Problem : Maya has 5 more than 4 times as many stamps as Ben. Together they have 285 stamps. How many does each have?
Let     : x = Ben's stamps
Equation: x + (4x + 5) = 285
Solve   : 5x = 280 → x = 56
Answer  : Ben: 56, Maya: 229

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0611'
KEY = 'number_puzzle/0611'
NAME = 'Number puzzle 0611'
CATEGORY = 'Number puzzle'
PROBLEM = 'Maya has 5 more than 4 times as many stamps as Ben. Together they have 285 stamps. How many does each have?'
LET = "x = Ben's stamps"
EQUATION = 'x + (4x + 5) = 285'
SOLVE = '5x = 280 → x = 56'
ANSWER = 'Ben: 56, Maya: 229'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Maya has {0} more than {1} times as many stamps as Ben. Together they have {2} stamps. How many does each have?'
NUMBERS = ['5', '4', '285']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

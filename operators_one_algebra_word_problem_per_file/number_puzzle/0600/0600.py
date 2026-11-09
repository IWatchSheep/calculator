"""Algebra word problem 0600   [Number puzzle]

Problem : Isla has 5 more than 2 times as many stamps as Caleb. Together they have 26 stamps. How many does each have?
Let     : x = Caleb's stamps
Equation: x + (2x + 5) = 26
Solve   : 3x = 21 → x = 7
Answer  : Caleb: 7, Isla: 19

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0600'
KEY = 'number_puzzle/0600'
NAME = 'Number puzzle 0600'
CATEGORY = 'Number puzzle'
PROBLEM = 'Isla has 5 more than 2 times as many stamps as Caleb. Together they have 26 stamps. How many does each have?'
LET = "x = Caleb's stamps"
EQUATION = 'x + (2x + 5) = 26'
SOLVE = '3x = 21 → x = 7'
ANSWER = 'Caleb: 7, Isla: 19'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Isla has {0} more than {1} times as many stamps as Caleb. Together they have {2} stamps. How many does each have?'
NUMBERS = ['5', '2', '26']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

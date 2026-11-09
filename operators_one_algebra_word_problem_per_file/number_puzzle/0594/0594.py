"""Algebra word problem 0594   [Number puzzle]

Problem : Caleb has 12 more than 3 times as many stamps as Bea. Together they have 88 stamps. How many does each have?
Let     : x = Bea's stamps
Equation: x + (3x + 12) = 88
Solve   : 4x = 76 → x = 19
Answer  : Bea: 19, Caleb: 69

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0594'
KEY = 'number_puzzle/0594'
NAME = 'Number puzzle 0594'
CATEGORY = 'Number puzzle'
PROBLEM = 'Caleb has 12 more than 3 times as many stamps as Bea. Together they have 88 stamps. How many does each have?'
LET = "x = Bea's stamps"
EQUATION = 'x + (3x + 12) = 88'
SOLVE = '4x = 76 → x = 19'
ANSWER = 'Bea: 19, Caleb: 69'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Caleb has {0} more than {1} times as many stamps as Bea. Together they have {2} stamps. How many does each have?'
NUMBERS = ['12', '3', '88']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

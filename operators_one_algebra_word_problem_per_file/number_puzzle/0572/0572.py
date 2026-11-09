"""Algebra word problem 0572   [Number puzzle]

Problem : Tara has 3 more than 4 times as many stamps as Aiden. Together they have 38 stamps. How many does each have?
Let     : x = Aiden's stamps
Equation: x + (4x + 3) = 38
Solve   : 5x = 35 → x = 7
Answer  : Aiden: 7, Tara: 31

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0572'
KEY = 'number_puzzle/0572'
NAME = 'Number puzzle 0572'
CATEGORY = 'Number puzzle'
PROBLEM = 'Tara has 3 more than 4 times as many stamps as Aiden. Together they have 38 stamps. How many does each have?'
LET = "x = Aiden's stamps"
EQUATION = 'x + (4x + 3) = 38'
SOLVE = '5x = 35 → x = 7'
ANSWER = 'Aiden: 7, Tara: 31'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Tara has {0} more than {1} times as many stamps as Aiden. Together they have {2} stamps. How many does each have?'
NUMBERS = ['3', '4', '38']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

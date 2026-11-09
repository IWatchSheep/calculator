"""Algebra word problem 0597   [Number puzzle]

Problem : Ben has 3 times as much money as Dev. After Ben gives Dev $38, they have the same amount. How much did each have at first?
Let     : x = Dev's money
Equation: 3x − 38 = x + 38
Solve   : 2x = 76 → x = 38
Answer  : Dev $38, Ben $114

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0597'
KEY = 'number_puzzle/0597'
NAME = 'Number puzzle 0597'
CATEGORY = 'Number puzzle'
PROBLEM = 'Ben has 3 times as much money as Dev. After Ben gives Dev $38, they have the same amount. How much did each have at first?'
LET = "x = Dev's money"
EQUATION = '3x − 38 = x + 38'
SOLVE = '2x = 76 → x = 38'
ANSWER = 'Dev $38, Ben $114'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Ben has {0} times as much money as Dev. After Ben gives Dev ${1}, they have the same amount. How much did each have at first?'
NUMBERS = ['3', '38']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

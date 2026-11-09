"""Algebra word problem 0591   [Number puzzle]

Problem : Wren has 3 times as much money as Sam. After Wren gives Sam $15, they have the same amount. How much did each have at first?
Let     : x = Sam's money
Equation: 3x − 15 = x + 15
Solve   : 2x = 30 → x = 15
Answer  : Sam $15, Wren $45

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0591'
KEY = 'number_puzzle/0591'
NAME = 'Number puzzle 0591'
CATEGORY = 'Number puzzle'
PROBLEM = 'Wren has 3 times as much money as Sam. After Wren gives Sam $15, they have the same amount. How much did each have at first?'
LET = "x = Sam's money"
EQUATION = '3x − 15 = x + 15'
SOLVE = '2x = 30 → x = 15'
ANSWER = 'Sam $15, Wren $45'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Wren has {0} times as much money as Sam. After Wren gives Sam ${1}, they have the same amount. How much did each have at first?'
NUMBERS = ['3', '15']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

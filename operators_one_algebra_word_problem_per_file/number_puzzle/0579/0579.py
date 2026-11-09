"""Algebra word problem 0579   [Number puzzle]

Problem : Grace has 4 times as much money as Nia. After Grace gives Nia $42, they have the same amount. How much did each have at first?
Let     : x = Nia's money
Equation: 4x − 42 = x + 42
Solve   : 3x = 84 → x = 28
Answer  : Nia $28, Grace $112

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0579'
KEY = 'number_puzzle/0579'
NAME = 'Number puzzle 0579'
CATEGORY = 'Number puzzle'
PROBLEM = 'Grace has 4 times as much money as Nia. After Grace gives Nia $42, they have the same amount. How much did each have at first?'
LET = "x = Nia's money"
EQUATION = '4x − 42 = x + 42'
SOLVE = '3x = 84 → x = 28'
ANSWER = 'Nia $28, Grace $112'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Grace has {0} times as much money as Nia. After Grace gives Nia ${1}, they have the same amount. How much did each have at first?'
NUMBERS = ['4', '42']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

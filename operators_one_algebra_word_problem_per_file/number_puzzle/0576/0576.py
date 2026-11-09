"""Algebra word problem 0576   [Number puzzle]

Problem : Aiden has 3 times as much money as Fatima. After Aiden gives Fatima $43, they have the same amount. How much did each have at first?
Let     : x = Fatima's money
Equation: 3x − 43 = x + 43
Solve   : 2x = 86 → x = 43
Answer  : Fatima $43, Aiden $129

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0576'
KEY = 'number_puzzle/0576'
NAME = 'Number puzzle 0576'
CATEGORY = 'Number puzzle'
PROBLEM = 'Aiden has 3 times as much money as Fatima. After Aiden gives Fatima $43, they have the same amount. How much did each have at first?'
LET = "x = Fatima's money"
EQUATION = '3x − 43 = x + 43'
SOLVE = '2x = 86 → x = 43'
ANSWER = 'Fatima $43, Aiden $129'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Aiden has {0} times as much money as Fatima. After Aiden gives Fatima ${1}, they have the same amount. How much did each have at first?'
NUMBERS = ['3', '43']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

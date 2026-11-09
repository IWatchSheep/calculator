"""Algebra word problem 0651   [Percent]

Problem : After a 10% discount, a coffee maker costs $22.50. What was the original price?
Let     : p = original price
Equation: 0.9p = 22.5
Solve   : p = 22.5 ÷ 0.9 = 25
Answer  : $25.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0651'
KEY = 'percent/0651'
NAME = 'Percent 0651'
CATEGORY = 'Percent'
PROBLEM = 'After a 10% discount, a coffee maker costs $22.50. What was the original price?'
LET = 'p = original price'
EQUATION = '0.9p = 22.5'
SOLVE = 'p = 22.5 ÷ 0.9 = 25'
ANSWER = '$25.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'After a {0}% discount, a coffee maker costs ${1}. What was the original price?'
NUMBERS = ['10', '22.50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

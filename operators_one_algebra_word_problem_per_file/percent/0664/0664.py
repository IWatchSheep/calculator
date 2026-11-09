"""Algebra word problem 0664   [Percent]

Problem : 7 friends split a restaurant bill equally, including a 15% tip. Each paid $51.75. What was the bill before the tip?
Let     : b = bill before tip
Equation: 1.15b / 7 = 51.75
Solve   : (23/140)b = 51.75 → b = 315
Answer  : $315.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0664'
KEY = 'percent/0664'
NAME = 'Percent 0664'
CATEGORY = 'Percent'
PROBLEM = '7 friends split a restaurant bill equally, including a 15% tip. Each paid $51.75. What was the bill before the tip?'
LET = 'b = bill before tip'
EQUATION = '1.15b / 7 = 51.75'
SOLVE = '(23/140)b = 51.75 → b = 315'
ANSWER = '$315.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} friends split a restaurant bill equally, including a {1}% tip. Each paid ${2}. What was the bill before the tip?'
NUMBERS = ['7', '15', '51.75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

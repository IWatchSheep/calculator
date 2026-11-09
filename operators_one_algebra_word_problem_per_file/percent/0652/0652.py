"""Algebra word problem 0652   [Percent]

Problem : 9 friends split a restaurant bill equally, including a 20% tip. Each paid $94.80. What was the bill before the tip?
Let     : b = bill before tip
Equation: 1.2b / 9 = 94.8
Solve   : (2/15)b = 94.8 → b = 711
Answer  : $711.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0652'
KEY = 'percent/0652'
NAME = 'Percent 0652'
CATEGORY = 'Percent'
PROBLEM = '9 friends split a restaurant bill equally, including a 20% tip. Each paid $94.80. What was the bill before the tip?'
LET = 'b = bill before tip'
EQUATION = '1.2b / 9 = 94.8'
SOLVE = '(2/15)b = 94.8 → b = 711'
ANSWER = '$711.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} friends split a restaurant bill equally, including a {1}% tip. Each paid ${2}. What was the bill before the tip?'
NUMBERS = ['9', '20', '94.80']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0623   [Percent]

Problem : 9 friends split a restaurant bill equally, including a 25% tip. Each paid $175.00. What was the bill before the tip?
Let     : b = bill before tip
Equation: 1.25b / 9 = 175
Solve   : (5/36)b = 175 → b = 1260
Answer  : $1,260.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0623'
KEY = 'percent/0623'
NAME = 'Percent 0623'
CATEGORY = 'Percent'
PROBLEM = '9 friends split a restaurant bill equally, including a 25% tip. Each paid $175.00. What was the bill before the tip?'
LET = 'b = bill before tip'
EQUATION = '1.25b / 9 = 175'
SOLVE = '(5/36)b = 175 → b = 1260'
ANSWER = '$1,260.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} friends split a restaurant bill equally, including a {1}% tip. Each paid ${2}. What was the bill before the tip?'
NUMBERS = ['9', '25', '175.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

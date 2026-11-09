"""Algebra word problem 0653   [Percent]

Problem : A group paid $243.95 for lunch, which included a 25% tip. How much was the meal itself?
Let     : b = bill before tip
Equation: 1.25b = 243.95
Solve   : 1.25b = 243.95 → b = 195.16
Answer  : $195.16

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0653'
KEY = 'percent/0653'
NAME = 'Percent 0653'
CATEGORY = 'Percent'
PROBLEM = 'A group paid $243.95 for lunch, which included a 25% tip. How much was the meal itself?'
LET = 'b = bill before tip'
EQUATION = '1.25b = 243.95'
SOLVE = '1.25b = 243.95 → b = 195.16'
ANSWER = '$195.16'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A group paid ${0} for lunch, which included a {1}% tip. How much was the meal itself?'
NUMBERS = ['243.95', '25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

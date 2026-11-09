"""Algebra word problem 0675   [Percent]

Problem : After adding a 25% tip, a dinner bill came to $193.00. What was the bill before the tip?
Let     : b = bill before tip
Equation: 1.25b = 193
Solve   : 1.25b = 193 → b = 154.4
Answer  : $154.40

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0675'
KEY = 'percent/0675'
NAME = 'Percent 0675'
CATEGORY = 'Percent'
PROBLEM = 'After adding a 25% tip, a dinner bill came to $193.00. What was the bill before the tip?'
LET = 'b = bill before tip'
EQUATION = '1.25b = 193'
SOLVE = '1.25b = 193 → b = 154.4'
ANSWER = '$154.40'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'After adding a {0}% tip, a dinner bill came to ${1}. What was the bill before the tip?'
NUMBERS = ['25', '193.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

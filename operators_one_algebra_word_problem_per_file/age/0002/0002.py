"""Algebra word problem 0002   [Age]

Problem : Wes is 13 years older than Theo. The sum of their ages is 85. How old is each?
Let     : x = Theo's age
Equation: x + (x + 13) = 85
Solve   : 2x = 72 → x = 36
Answer  : Theo is 36, Wes is 49

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0002'
KEY = 'age/0002'
NAME = 'Age 0002'
CATEGORY = 'Age'
PROBLEM = 'Wes is 13 years older than Theo. The sum of their ages is 85. How old is each?'
LET = "x = Theo's age"
EQUATION = 'x + (x + 13) = 85'
SOLVE = '2x = 72 → x = 36'
ANSWER = 'Theo is 36, Wes is 49'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Wes is {0} years older than Theo. The sum of their ages is {1}. How old is each?'
NUMBERS = ['13', '85']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

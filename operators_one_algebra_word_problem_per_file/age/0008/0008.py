"""Algebra word problem 0008   [Age]

Problem : Emeka is 5 years older than Yara. The sum of their ages is 67. How old is each?
Let     : x = Yara's age
Equation: x + (x + 5) = 67
Solve   : 2x = 62 → x = 31
Answer  : Yara is 31, Emeka is 36

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0008'
KEY = 'age/0008'
NAME = 'Age 0008'
CATEGORY = 'Age'
PROBLEM = 'Emeka is 5 years older than Yara. The sum of their ages is 67. How old is each?'
LET = "x = Yara's age"
EQUATION = 'x + (x + 5) = 67'
SOLVE = '2x = 62 → x = 31'
ANSWER = 'Yara is 31, Emeka is 36'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Emeka is {0} years older than Yara. The sum of their ages is {1}. How old is each?'
NUMBERS = ['5', '67']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

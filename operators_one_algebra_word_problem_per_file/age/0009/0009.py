"""Algebra word problem 0009   [Age]

Problem : Maya is 30 years older than Yara. The sum of their ages is 40. How old is each?
Let     : x = Yara's age
Equation: x + (x + 30) = 40
Solve   : 2x = 10 → x = 5
Answer  : Yara is 5, Maya is 35

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0009'
KEY = 'age/0009'
NAME = 'Age 0009'
CATEGORY = 'Age'
PROBLEM = 'Maya is 30 years older than Yara. The sum of their ages is 40. How old is each?'
LET = "x = Yara's age"
EQUATION = 'x + (x + 30) = 40'
SOLVE = '2x = 10 → x = 5'
ANSWER = 'Yara is 5, Maya is 35'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Maya is {0} years older than Yara. The sum of their ages is {1}. How old is each?'
NUMBERS = ['30', '40']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

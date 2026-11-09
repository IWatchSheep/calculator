"""Algebra word problem 0595   [Number puzzle]

Problem : The second of three numbers is 3 times the first. The third is 5 more than the second. Their sum is 68. Find the numbers.
Let     : x = first number
Equation: x + 3x + (3x + 5) = 68
Solve   : 7x = 63 → x = 9
Answer  : 9, 27, 32

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0595'
KEY = 'number_puzzle/0595'
NAME = 'Number puzzle 0595'
CATEGORY = 'Number puzzle'
PROBLEM = 'The second of three numbers is 3 times the first. The third is 5 more than the second. Their sum is 68. Find the numbers.'
LET = 'x = first number'
EQUATION = 'x + 3x + (3x + 5) = 68'
SOLVE = '7x = 63 → x = 9'
ANSWER = '9, 27, 32'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The second of three numbers is {0} times the first. The third is {1} more than the second. Their sum is {2}. Find the numbers.'
NUMBERS = ['3', '5', '68']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

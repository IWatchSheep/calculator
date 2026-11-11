"""Algebra word problem 0823   [Rational equation]

Problem : A group shares a $42 rental equally. If 2 more people join, each pays $1.75 less. How many people are in the group originally?
Let     : n = original number of people
Equation: 42/n − 42/(n + 2) = 1.75
Solve   : Multiply out → quadratic in n → n = 6 (reject negative)
Answer  : 6 people

Status  : ready: archive_rational_equation_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0823'
KEY = 'rational_equation/0823'
NAME = 'Rational equation 0823'
CATEGORY = 'Rational equation'
PROBLEM = 'A group shares a $42 rental equally. If 2 more people join, each pays $1.75 less. How many people are in the group originally?'
LET = 'n = original number of people'
EQUATION = '42/n − 42/(n + 2) = 1.75'
SOLVE = 'Multiply out → quadratic in n → n = 6 (reject negative)'
ANSWER = '6 people'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_rational_equation_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A group shares a ${0} rental equally. If {1} more people join, each pays ${2} less. How many people are in the group originally?'
NUMBERS = ['42', '2', '1.75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

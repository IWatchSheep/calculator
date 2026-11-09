"""Algebra word problem 0840   [Rational equation]

Problem : A group shares a $156 rental equally. If 3 more people join, each pays $2.60 less. How many people are in the group originally?
Let     : n = original number of people
Equation: 156/n − 156/(n + 3) = 2.6
Solve   : Multiply out → quadratic in n → n = 12 (reject negative)
Answer  : 12 people

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0840'
KEY = 'rational_equation/0840'
NAME = 'Rational equation 0840'
CATEGORY = 'Rational equation'
PROBLEM = 'A group shares a $156 rental equally. If 3 more people join, each pays $2.60 less. How many people are in the group originally?'
LET = 'n = original number of people'
EQUATION = '156/n − 156/(n + 3) = 2.6'
SOLVE = 'Multiply out → quadratic in n → n = 12 (reject negative)'
ANSWER = '12 people'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A group shares a ${0} rental equally. If {1} more people join, each pays ${2} less. How many people are in the group originally?'
NUMBERS = ['156', '3', '2.60']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

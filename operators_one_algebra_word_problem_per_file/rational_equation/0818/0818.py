"""Algebra word problem 0818   [Rational equation]

Problem : A boat goes 52 km upstream in the same time it goes 132 km downstream. Its speed in still water is 23 km/h. What is the speed of the current?
Let     : c = current speed
Equation: 52/(23 − c) = 132/(23 + c)
Solve   : Cross-multiply → c = 10
Answer  : 10 km/h

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0818'
KEY = 'rational_equation/0818'
NAME = 'Rational equation 0818'
CATEGORY = 'Rational equation'
PROBLEM = 'A boat goes 52 km upstream in the same time it goes 132 km downstream. Its speed in still water is 23 km/h. What is the speed of the current?'
LET = 'c = current speed'
EQUATION = '52/(23 − c) = 132/(23 + c)'
SOLVE = 'Cross-multiply → c = 10'
ANSWER = '10 km/h'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A boat goes {0} km upstream in the same time it goes {1} km downstream. Its speed in still water is {2} km/h. What is the speed of the current?'
NUMBERS = ['52', '132', '23']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0843   [Rational equation]

Problem : A truck travels 265 miles in the same time a car travels 320 miles. The car is 11 mph faster. Find both speeds.
Let     : s = truck speed
Equation: 265/s = 320/(s + 11)
Solve   : Cross-multiply: 265(s + 11) = 320s → s = 53
Answer  : Truck 53 mph, car 64 mph

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0843'
KEY = 'rational_equation/0843'
NAME = 'Rational equation 0843'
CATEGORY = 'Rational equation'
PROBLEM = 'A truck travels 265 miles in the same time a car travels 320 miles. The car is 11 mph faster. Find both speeds.'
LET = 's = truck speed'
EQUATION = '265/s = 320/(s + 11)'
SOLVE = 'Cross-multiply: 265(s + 11) = 320s → s = 53'
ANSWER = 'Truck 53 mph, car 64 mph'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A truck travels {0} miles in the same time a car travels {1} miles. The car is {2} mph faster. Find both speeds.'
NUMBERS = ['265', '320', '11']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

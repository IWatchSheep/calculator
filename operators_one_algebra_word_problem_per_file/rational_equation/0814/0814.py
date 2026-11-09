"""Algebra word problem 0814   [Rational equation]

Problem : The denominator of a fraction is 2 more than the numerator. If 4 is added to both, the fraction becomes 7/8. Find the original fraction.
Let     : x = numerator
Equation: (x + 4)/(x + 6) = 7/8
Solve   : Cross-multiply and solve → x = 10
Answer  : 10/12

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0814'
KEY = 'rational_equation/0814'
NAME = 'Rational equation 0814'
CATEGORY = 'Rational equation'
PROBLEM = 'The denominator of a fraction is 2 more than the numerator. If 4 is added to both, the fraction becomes 7/8. Find the original fraction.'
LET = 'x = numerator'
EQUATION = '(x + 4)/(x + 6) = 7/8'
SOLVE = 'Cross-multiply and solve → x = 10'
ANSWER = '10/12'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The denominator of a fraction is {0} more than the numerator. If {1} is added to both, the fraction becomes {2}/{3}. Find the original fraction.'
NUMBERS = ['2', '4', '7', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

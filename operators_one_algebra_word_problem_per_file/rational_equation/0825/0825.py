"""Algebra word problem 0825   [Rational equation]

Problem : The denominator of a fraction is 2 more than the numerator. If 3 is added to both, the fraction becomes 5/6. Find the original fraction.
Let     : x = numerator
Equation: (x + 3)/(x + 5) = 5/6
Solve   : Cross-multiply and solve → x = 7
Answer  : 7/9

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0825'
KEY = 'rational_equation/0825'
NAME = 'Rational equation 0825'
CATEGORY = 'Rational equation'
PROBLEM = 'The denominator of a fraction is 2 more than the numerator. If 3 is added to both, the fraction becomes 5/6. Find the original fraction.'
LET = 'x = numerator'
EQUATION = '(x + 3)/(x + 5) = 5/6'
SOLVE = 'Cross-multiply and solve → x = 7'
ANSWER = '7/9'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The denominator of a fraction is {0} more than the numerator. If {1} is added to both, the fraction becomes {2}/{3}. Find the original fraction.'
NUMBERS = ['2', '3', '5', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

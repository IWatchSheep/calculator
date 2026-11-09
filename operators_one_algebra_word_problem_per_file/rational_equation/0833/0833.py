"""Algebra word problem 0833   [Rational equation]

Problem : The denominator of a fraction is 1 more than the numerator. If 4 is added to both, the fraction becomes 20/21. Find the original fraction.
Let     : x = numerator
Equation: (x + 4)/(x + 5) = 20/21
Solve   : Cross-multiply and solve → x = 16
Answer  : 16/17

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0833'
KEY = 'rational_equation/0833'
NAME = 'Rational equation 0833'
CATEGORY = 'Rational equation'
PROBLEM = 'The denominator of a fraction is 1 more than the numerator. If 4 is added to both, the fraction becomes 20/21. Find the original fraction.'
LET = 'x = numerator'
EQUATION = '(x + 4)/(x + 5) = 20/21'
SOLVE = 'Cross-multiply and solve → x = 16'
ANSWER = '16/17'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The denominator of a fraction is {0} more than the numerator. If {1} is added to both, the fraction becomes {2}/{3}. Find the original fraction.'
NUMBERS = ['1', '4', '20', '21']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

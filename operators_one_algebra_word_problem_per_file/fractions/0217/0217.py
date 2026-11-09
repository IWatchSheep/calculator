"""Algebra word problem 0217   [Fractions]

Problem : Sam read 1/5 of a book on Monday and 1/2 of the remaining pages on Tuesday. 52 pages are left. How many pages does the book have?
Let     : x = total pages
Equation: x × (4/5) × (1/2) = 52
Solve   : 0.4x = 52 → x = 130
Answer  : 130 pages

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0217'
KEY = 'fractions/0217'
NAME = 'Fractions 0217'
CATEGORY = 'Fractions'
PROBLEM = 'Sam read 1/5 of a book on Monday and 1/2 of the remaining pages on Tuesday. 52 pages are left. How many pages does the book have?'
LET = 'x = total pages'
EQUATION = 'x × (4/5) × (1/2) = 52'
SOLVE = '0.4x = 52 → x = 130'
ANSWER = '130 pages'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Sam read {0}/{1} of a book on Monday and {2}/{3} of the remaining pages on Tuesday. {4} pages are left. How many pages does the book have?'
NUMBERS = ['1', '5', '1', '2', '52']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

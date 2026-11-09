"""Algebra word problem 0213   [Fractions]

Problem : Sofia read 1/5 of a book on Monday and 1/4 of the remaining pages on Tuesday. 108 pages are left. How many pages does the book have?
Let     : x = total pages
Equation: x × (4/5) × (3/4) = 108
Solve   : 0.6x = 108 → x = 180
Answer  : 180 pages

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0213'
KEY = 'fractions/0213'
NAME = 'Fractions 0213'
CATEGORY = 'Fractions'
PROBLEM = 'Sofia read 1/5 of a book on Monday and 1/4 of the remaining pages on Tuesday. 108 pages are left. How many pages does the book have?'
LET = 'x = total pages'
EQUATION = 'x × (4/5) × (3/4) = 108'
SOLVE = '0.6x = 108 → x = 180'
ANSWER = '180 pages'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Sofia read {0}/{1} of a book on Monday and {2}/{3} of the remaining pages on Tuesday. {4} pages are left. How many pages does the book have?'
NUMBERS = ['1', '5', '1', '4', '108']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

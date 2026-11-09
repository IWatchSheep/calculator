"""Algebra word problem 0221   [Fractions]

Problem : Isla read 1/3 of a book on Monday and 1/2 of the remaining pages on Tuesday. 12 pages are left. How many pages does the book have?
Let     : x = total pages
Equation: x × (2/3) × (1/2) = 12
Solve   : x/3 = 12 → x = 12 × 3 = 36
Answer  : 36 pages

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0221'
KEY = 'fractions/0221'
NAME = 'Fractions 0221'
CATEGORY = 'Fractions'
PROBLEM = 'Isla read 1/3 of a book on Monday and 1/2 of the remaining pages on Tuesday. 12 pages are left. How many pages does the book have?'
LET = 'x = total pages'
EQUATION = 'x × (2/3) × (1/2) = 12'
SOLVE = 'x/3 = 12 → x = 12 × 3 = 36'
ANSWER = '36 pages'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Isla read {0}/{1} of a book on Monday and {2}/{3} of the remaining pages on Tuesday. {4} pages are left. How many pages does the book have?'
NUMBERS = ['1', '3', '1', '2', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0959   [Tickets]

Problem : Adult tickets to a movie screening cost $12 and child tickets cost $6. 167 tickets were sold for a total of $1404. How many of each were sold?
Let     : x = adult tickets; 167 − x = child tickets
Equation: 12x + 6(167 − x) = 1404
Solve   : 6x = 402 → x = 67
Answer  : 67 adult and 100 child tickets

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0959'
KEY = 'tickets/0959'
NAME = 'Tickets 0959'
CATEGORY = 'Tickets'
PROBLEM = 'Adult tickets to a movie screening cost $12 and child tickets cost $6. 167 tickets were sold for a total of $1404. How many of each were sold?'
LET = 'x = adult tickets; 167 − x = child tickets'
EQUATION = '12x + 6(167 − x) = 1404'
SOLVE = '6x = 402 → x = 67'
ANSWER = '67 adult and 100 child tickets'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Adult tickets to a movie screening cost ${0} and child tickets cost ${1}. {2} tickets were sold for a total of ${3}. How many of each were sold?'
NUMBERS = ['12', '6', '167', '1404']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

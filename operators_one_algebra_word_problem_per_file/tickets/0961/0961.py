"""Algebra word problem 0961   [Tickets]

Problem : Adult tickets to a movie screening cost $8 and child tickets cost $5. 252 tickets were sold for a total of $1398. How many of each were sold?
Let     : x = adult tickets; 252 − x = child tickets
Equation: 8x + 5(252 − x) = 1398
Solve   : 3x = 138 → x = 46
Answer  : 46 adult and 206 child tickets

Status  : ready: archive_tickets_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0961'
KEY = 'tickets/0961'
NAME = 'Tickets 0961'
CATEGORY = 'Tickets'
PROBLEM = 'Adult tickets to a movie screening cost $8 and child tickets cost $5. 252 tickets were sold for a total of $1398. How many of each were sold?'
LET = 'x = adult tickets; 252 − x = child tickets'
EQUATION = '8x + 5(252 − x) = 1398'
SOLVE = '3x = 138 → x = 46'
ANSWER = '46 adult and 206 child tickets'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_tickets_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Adult tickets to a movie screening cost ${0} and child tickets cost ${1}. {2} tickets were sold for a total of ${3}. How many of each were sold?'
NUMBERS = ['8', '5', '252', '1398']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

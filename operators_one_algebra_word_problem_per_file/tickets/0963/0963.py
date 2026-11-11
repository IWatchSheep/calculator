"""Algebra word problem 0963   [Tickets]

Problem : Adult tickets to a movie screening cost $8 and child tickets cost $7. 471 tickets were sold for a total of $3535. How many of each were sold?
Let     : x = adult tickets; 471 − x = child tickets
Equation: 8x + 7(471 − x) = 3535
Solve   : x = 238
Answer  : 238 adult and 233 child tickets

Status  : ready: archive_tickets_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0963'
KEY = 'tickets/0963'
NAME = 'Tickets 0963'
CATEGORY = 'Tickets'
PROBLEM = 'Adult tickets to a movie screening cost $8 and child tickets cost $7. 471 tickets were sold for a total of $3535. How many of each were sold?'
LET = 'x = adult tickets; 471 − x = child tickets'
EQUATION = '8x + 7(471 − x) = 3535'
SOLVE = 'x = 238'
ANSWER = '238 adult and 233 child tickets'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_tickets_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Adult tickets to a movie screening cost ${0} and child tickets cost ${1}. {2} tickets were sold for a total of ${3}. How many of each were sold?'
NUMBERS = ['8', '7', '471', '3535']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

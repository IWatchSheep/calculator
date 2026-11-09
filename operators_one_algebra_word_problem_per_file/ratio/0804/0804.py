"""Algebra word problem 0804   [Ratio]

Problem : An estate of $31,500.00 is split among three heirs. Xena gets 3 times as much as Dana, and Finn gets $9,000.00 more than Dana. How much does each receive?
Let     : x = Dana's share
Equation: 3x + x + (x + 9000) = 31500
Solve   : 5x = 22500 → x = 4500
Answer  : Xena $13,500.00, Dana $4,500.00, Finn $13,500.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0804'
KEY = 'ratio/0804'
NAME = 'Ratio 0804'
CATEGORY = 'Ratio'
PROBLEM = 'An estate of $31,500.00 is split among three heirs. Xena gets 3 times as much as Dana, and Finn gets $9,000.00 more than Dana. How much does each receive?'
LET = "x = Dana's share"
EQUATION = '3x + x + (x + 9000) = 31500'
SOLVE = '5x = 22500 → x = 4500'
ANSWER = 'Xena $13,500.00, Dana $4,500.00, Finn $13,500.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An estate of ${0} is split among three heirs. Xena gets {1} times as much as Dana, and Finn gets ${2} more than Dana. How much does each receive?'
NUMBERS = ['31500.00', '3', '9000.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

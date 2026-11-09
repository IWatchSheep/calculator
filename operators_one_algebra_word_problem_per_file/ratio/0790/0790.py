"""Algebra word problem 0790   [Ratio]

Problem : An estate of $92,000.00 is split among three heirs. Finn gets 3 times as much as Sam, and Ben gets $2,000.00 more than Sam. How much does each receive?
Let     : x = Sam's share
Equation: 3x + x + (x + 2000) = 92000
Solve   : 5x = 90000 → x = 18000
Answer  : Finn $54,000.00, Sam $18,000.00, Ben $20,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0790'
KEY = 'ratio/0790'
NAME = 'Ratio 0790'
CATEGORY = 'Ratio'
PROBLEM = 'An estate of $92,000.00 is split among three heirs. Finn gets 3 times as much as Sam, and Ben gets $2,000.00 more than Sam. How much does each receive?'
LET = "x = Sam's share"
EQUATION = '3x + x + (x + 2000) = 92000'
SOLVE = '5x = 90000 → x = 18000'
ANSWER = 'Finn $54,000.00, Sam $18,000.00, Ben $20,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An estate of ${0} is split among three heirs. Finn gets {1} times as much as Sam, and Ben gets ${2} more than Sam. How much does each receive?'
NUMBERS = ['92000.00', '3', '2000.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

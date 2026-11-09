"""Algebra word problem 0780   [Ratio]

Problem : An estate of $64,500.00 is split among three heirs. Wes gets 2 times as much as Nia, and Noah gets $6,500.00 more than Nia. How much does each receive?
Let     : x = Nia's share
Equation: 2x + x + (x + 6500) = 64500
Solve   : 4x = 58000 → x = 14500
Answer  : Wes $29,000.00, Nia $14,500.00, Noah $21,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0780'
KEY = 'ratio/0780'
NAME = 'Ratio 0780'
CATEGORY = 'Ratio'
PROBLEM = 'An estate of $64,500.00 is split among three heirs. Wes gets 2 times as much as Nia, and Noah gets $6,500.00 more than Nia. How much does each receive?'
LET = "x = Nia's share"
EQUATION = '2x + x + (x + 6500) = 64500'
SOLVE = '4x = 58000 → x = 14500'
ANSWER = 'Wes $29,000.00, Nia $14,500.00, Noah $21,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An estate of ${0} is split among three heirs. Wes gets {1} times as much as Nia, and Noah gets ${2} more than Nia. How much does each receive?'
NUMBERS = ['64500.00', '2', '6500.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0799   [Ratio]

Problem : An estate of $71,000.00 is split among three heirs. Jamal gets 3 times as much as Maya, and Noah gets $6,000.00 more than Maya. How much does each receive?
Let     : x = Maya's share
Equation: 3x + x + (x + 6000) = 71000
Solve   : 5x = 65000 → x = 13000
Answer  : Jamal $39,000.00, Maya $13,000.00, Noah $19,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0799'
KEY = 'ratio/0799'
NAME = 'Ratio 0799'
CATEGORY = 'Ratio'
PROBLEM = 'An estate of $71,000.00 is split among three heirs. Jamal gets 3 times as much as Maya, and Noah gets $6,000.00 more than Maya. How much does each receive?'
LET = "x = Maya's share"
EQUATION = '3x + x + (x + 6000) = 71000'
SOLVE = '5x = 65000 → x = 13000'
ANSWER = 'Jamal $39,000.00, Maya $13,000.00, Noah $19,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An estate of ${0} is split among three heirs. Jamal gets {1} times as much as Maya, and Noah gets ${2} more than Maya. How much does each receive?'
NUMBERS = ['71000.00', '3', '6000.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

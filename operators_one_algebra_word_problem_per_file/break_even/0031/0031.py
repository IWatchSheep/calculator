"""Algebra word problem 0031   [Break-even]

Problem : Job A pays $1000 a month plus 2% commission. Job B pays $490 a month plus 5% commission. At what monthly sales total do both pay the same?
Let     : s = monthly sales
Equation: 1000 + 0.02s = 490 + 0.05s
Solve   : 0.03s = 510 → s = 17000
Answer  : $17,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0031'
KEY = 'break_even/0031'
NAME = 'Break-even 0031'
CATEGORY = 'Break-even'
PROBLEM = 'Job A pays $1000 a month plus 2% commission. Job B pays $490 a month plus 5% commission. At what monthly sales total do both pay the same?'
LET = 's = monthly sales'
EQUATION = '1000 + 0.02s = 490 + 0.05s'
SOLVE = '0.03s = 510 → s = 17000'
ANSWER = '$17,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Job A pays ${0} a month plus {1}% commission. Job B pays ${2} a month plus {3}% commission. At what monthly sales total do both pay the same?'
NUMBERS = ['1000', '2', '490', '5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

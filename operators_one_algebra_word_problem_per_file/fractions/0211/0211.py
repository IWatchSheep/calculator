"""Algebra word problem 0211   [Fractions]

Problem : A puzzle: a man spent 1/6 of his life as a boy, 1/12 more as a youth, and 1/7 more before marrying. 5 years later a son was born, who lived 1/2 as long as his father. The father died 4 years after the son. How long did the father live?
Let     : x = father's age at death
Equation: x/6 + x/12 + x/7 + 5 + x/2 + 4 = x
Solve   : (3/28)x = 9 → x = 84
Answer  : 84 years

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0211'
KEY = 'fractions/0211'
NAME = 'Fractions 0211'
CATEGORY = 'Fractions'
PROBLEM = 'A puzzle: a man spent 1/6 of his life as a boy, 1/12 more as a youth, and 1/7 more before marrying. 5 years later a son was born, who lived 1/2 as long as his father. The father died 4 years after the son. How long did the father live?'
LET = "x = father's age at death"
EQUATION = 'x/6 + x/12 + x/7 + 5 + x/2 + 4 = x'
SOLVE = '(3/28)x = 9 → x = 84'
ANSWER = '84 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A puzzle: a man spent {0}/{1} of his life as a boy, {2}/{3} more as a youth, and {4}/{5} more before marrying. {6} years later a son was born, who lived {7}/{8} as long as his father. The father died {9} years after the son. How long did the father live?'
NUMBERS = ['1', '6', '1', '12', '1', '7', '5', '1', '2', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

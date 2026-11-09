"""Algebra word problem 0973   [Work rate]

Problem : An inlet pipe fills a tank in 4 hours. A drain empties it in 12 hours. If both are open, how long does it take to fill the empty tank?
Let     : t = hours
Equation: t/4 − t/12 = 1
Solve   : t(8)/48 = 1 → t = 6
Answer  : 6 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0973'
KEY = 'work_rate/0973'
NAME = 'Work rate 0973'
CATEGORY = 'Work rate'
PROBLEM = 'An inlet pipe fills a tank in 4 hours. A drain empties it in 12 hours. If both are open, how long does it take to fill the empty tank?'
LET = 't = hours'
EQUATION = 't/4 − t/12 = 1'
SOLVE = 't(8)/48 = 1 → t = 6'
ANSWER = '6 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An inlet pipe fills a tank in {0} hours. A drain empties it in {1} hours. If both are open, how long does it take to fill the empty tank?'
NUMBERS = ['4', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

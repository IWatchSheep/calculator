"""Algebra word problem 0982   [Work rate]

Problem : An inlet pipe fills a tank in 5 hours. A drain empties it in 10 hours. If both are open, how long does it take to fill the empty tank?
Let     : t = hours
Equation: t/5 − t/10 = 1
Solve   : t(5)/50 = 1 → t = 10
Answer  : 10 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0982'
KEY = 'work_rate/0982'
NAME = 'Work rate 0982'
CATEGORY = 'Work rate'
PROBLEM = 'An inlet pipe fills a tank in 5 hours. A drain empties it in 10 hours. If both are open, how long does it take to fill the empty tank?'
LET = 't = hours'
EQUATION = 't/5 − t/10 = 1'
SOLVE = 't(5)/50 = 1 → t = 10'
ANSWER = '10 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An inlet pipe fills a tank in {0} hours. A drain empties it in {1} hours. If both are open, how long does it take to fill the empty tank?'
NUMBERS = ['5', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

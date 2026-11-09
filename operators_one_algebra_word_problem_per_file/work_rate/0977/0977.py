"""Algebra word problem 0977   [Work rate]

Problem : Pipe A fills a pool in 3 hours, pipe B in 6 hours, and a drain empties it in 10 hours. With all three open, how long does it take to fill the pool?
Let     : t = hours
Equation: t/3 + t/6 − t/10 = 1
Solve   : Combine rates → t = 2.5
Answer  : 2.5 hours

Status  : ready: pipes_and_drain answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0977'
KEY = 'work_rate/0977'
NAME = 'Work rate 0977'
CATEGORY = 'Work rate'
PROBLEM = 'Pipe A fills a pool in 3 hours, pipe B in 6 hours, and a drain empties it in 10 hours. With all three open, how long does it take to fill the pool?'
LET = 't = hours'
EQUATION = 't/3 + t/6 − t/10 = 1'
SOLVE = 'Combine rates → t = 2.5'
ANSWER = '2.5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'pipes_and_drain'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pipe A fills a pool in {0} hours, pipe B in {1} hours, and a drain empties it in {2} hours. With all three open, how long does it take to fill the pool?'
NUMBERS = ['3', '6', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

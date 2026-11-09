"""Algebra word problem 0994   [Work rate]

Problem : Pipe A fills a pool in 4 hours, pipe B in 12 hours, and a drain empties it in 6 hours. With all three open, how long does it take to fill the pool?
Let     : t = hours
Equation: t/4 + t/12 − t/6 = 1
Solve   : Combine rates → t = 6
Answer  : 6 hours

Status  : ready: pipes_and_drain answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0994'
KEY = 'work_rate/0994'
NAME = 'Work rate 0994'
CATEGORY = 'Work rate'
PROBLEM = 'Pipe A fills a pool in 4 hours, pipe B in 12 hours, and a drain empties it in 6 hours. With all three open, how long does it take to fill the pool?'
LET = 't = hours'
EQUATION = 't/4 + t/12 − t/6 = 1'
SOLVE = 'Combine rates → t = 6'
ANSWER = '6 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'pipes_and_drain'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pipe A fills a pool in {0} hours, pipe B in {1} hours, and a drain empties it in {2} hours. With all three open, how long does it take to fill the pool?'
NUMBERS = ['4', '12', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

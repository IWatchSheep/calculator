"""Algebra word problem 1000   [Work rate]

Problem : Dev can do a job in 12 hours and Pablo can do it in 3 hours. Dev works alone for 1 hour, then Pablo joins. How much longer will it take to finish?
Let     : t = hours working together
Equation: 1/12 + t/12 + t/3 = 1
Solve   : Combine rates → t = 2.2
Answer  : 2.2 more hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '1000'
KEY = 'work_rate/1000'
NAME = 'Work rate 1000'
CATEGORY = 'Work rate'
PROBLEM = 'Dev can do a job in 12 hours and Pablo can do it in 3 hours. Dev works alone for 1 hour, then Pablo joins. How much longer will it take to finish?'
LET = 't = hours working together'
EQUATION = '1/12 + t/12 + t/3 = 1'
SOLVE = 'Combine rates → t = 2.2'
ANSWER = '2.2 more hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Dev can do a job in {0} hours and Pablo can do it in {1} hours. Dev works alone for {2} hour, then Pablo joins. How much longer will it take to finish?'
NUMBERS = ['12', '3', '1']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

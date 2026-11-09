"""Algebra word problem 0971   [Work rate]

Problem : Sam can do a job in 4 hours and Hana can do it in 8 hours. Sam works alone for 2 hours, then Hana joins. How much longer will it take to finish?
Let     : t = hours working together
Equation: 2/4 + t/4 + t/8 = 1
Solve   : Combine rates → t = 4/3
Answer  : 4/3 more hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0971'
KEY = 'work_rate/0971'
NAME = 'Work rate 0971'
CATEGORY = 'Work rate'
PROBLEM = 'Sam can do a job in 4 hours and Hana can do it in 8 hours. Sam works alone for 2 hours, then Hana joins. How much longer will it take to finish?'
LET = 't = hours working together'
EQUATION = '2/4 + t/4 + t/8 = 1'
SOLVE = 'Combine rates → t = 4/3'
ANSWER = '4/3 more hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Sam can do a job in {0} hours and Hana can do it in {1} hours. Sam works alone for {2} hours, then Hana joins. How much longer will it take to finish?'
NUMBERS = ['4', '8', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

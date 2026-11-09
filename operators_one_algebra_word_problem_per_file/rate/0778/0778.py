"""Algebra word problem 0778   [Rate]

Problem : A car travels 360 miles on 9 gallons of gas. At this rate, how many gallons are needed for 1000 miles?
Let     : x = gallons
Equation: 360/9 = 1000/x
Solve   : 40x = 1000 → x = 25
Answer  : 25 gallons

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0778'
KEY = 'rate/0778'
NAME = 'Rate 0778'
CATEGORY = 'Rate'
PROBLEM = 'A car travels 360 miles on 9 gallons of gas. At this rate, how many gallons are needed for 1000 miles?'
LET = 'x = gallons'
EQUATION = '360/9 = 1000/x'
SOLVE = '40x = 1000 → x = 25'
ANSWER = '25 gallons'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A car travels {0} miles on {1} gallons of gas. At this rate, how many gallons are needed for {2} miles?'
NUMBERS = ['360', '9', '1000']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

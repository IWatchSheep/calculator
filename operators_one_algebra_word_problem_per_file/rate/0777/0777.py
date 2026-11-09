"""Algebra word problem 0777   [Rate]

Problem : A car travels 475 miles on 19 gallons of gas. At this rate, how many gallons are needed for 300 miles?
Let     : x = gallons
Equation: 475/19 = 300/x
Solve   : 25x = 300 → x = 12
Answer  : 12 gallons

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0777'
KEY = 'rate/0777'
NAME = 'Rate 0777'
CATEGORY = 'Rate'
PROBLEM = 'A car travels 475 miles on 19 gallons of gas. At this rate, how many gallons are needed for 300 miles?'
LET = 'x = gallons'
EQUATION = '475/19 = 300/x'
SOLVE = '25x = 300 → x = 12'
ANSWER = '12 gallons'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A car travels {0} miles on {1} gallons of gas. At this rate, how many gallons are needed for {2} miles?'
NUMBERS = ['475', '19', '300']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

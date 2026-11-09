"""Algebra word problem 0776   [Rate]

Problem : A car travels 154 miles on 7 gallons of gas. At this rate, how many gallons are needed for 528 miles?
Let     : x = gallons
Equation: 154/7 = 528/x
Solve   : 22x = 528 → x = 24
Answer  : 24 gallons

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0776'
KEY = 'rate/0776'
NAME = 'Rate 0776'
CATEGORY = 'Rate'
PROBLEM = 'A car travels 154 miles on 7 gallons of gas. At this rate, how many gallons are needed for 528 miles?'
LET = 'x = gallons'
EQUATION = '154/7 = 528/x'
SOLVE = '22x = 528 → x = 24'
ANSWER = '24 gallons'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A car travels {0} miles on {1} gallons of gas. At this rate, how many gallons are needed for {2} miles?'
NUMBERS = ['154', '7', '528']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

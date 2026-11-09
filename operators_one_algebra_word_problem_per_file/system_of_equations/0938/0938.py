"""Algebra word problem 0938   [System of equations]

Problem : A cash drawer has 39 bills, all $20 and $50 bills, totaling $1080. How many of each?
Let     : x = $20 bills, y = $50 bills
Equation: x + y = 39;  20x + 50y = 1080
Solve   : Solve by elimination → x = 29, y = 10
Answer  : 29 $20 bills and 10 $50 bills

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0938'
KEY = 'system_of_equations/0938'
NAME = 'System of equations 0938'
CATEGORY = 'System of equations'
PROBLEM = 'A cash drawer has 39 bills, all $20 and $50 bills, totaling $1080. How many of each?'
LET = 'x = $20 bills, y = $50 bills'
EQUATION = 'x + y = 39;  20x + 50y = 1080'
SOLVE = 'Solve by elimination → x = 29, y = 10'
ANSWER = '29 $20 bills and 10 $50 bills'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A cash drawer has {0} bills, all ${1} and ${2} bills, totaling ${3}. How many of each?'
NUMBERS = ['39', '20', '50', '1080']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

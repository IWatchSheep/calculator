"""Algebra word problem 0913   [System of equations]

Problem : A cash drawer has 51 bills, all $5 and $20 bills, totaling $645. How many of each?
Let     : x = $5 bills, y = $20 bills
Equation: x + y = 51;  5x + 20y = 645
Solve   : Solve by elimination → x = 25, y = 26
Answer  : 25 $5 bills and 26 $20 bills

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0913'
KEY = 'system_of_equations/0913'
NAME = 'System of equations 0913'
CATEGORY = 'System of equations'
PROBLEM = 'A cash drawer has 51 bills, all $5 and $20 bills, totaling $645. How many of each?'
LET = 'x = $5 bills, y = $20 bills'
EQUATION = 'x + y = 51;  5x + 20y = 645'
SOLVE = 'Solve by elimination → x = 25, y = 26'
ANSWER = '25 $5 bills and 26 $20 bills'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A cash drawer has {0} bills, all ${1} and ${2} bills, totaling ${3}. How many of each?'
NUMBERS = ['51', '5', '20', '645']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

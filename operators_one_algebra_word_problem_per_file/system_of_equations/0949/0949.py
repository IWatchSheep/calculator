"""Algebra word problem 0949   [System of equations]

Problem : A concert sold 1162 tickets: lawn seats at $20 and reserved seats at $45. Ticket sales totaled $39,765. How many of each were sold?
Let     : x = lawn, y = reserved
Equation: x + y = 1162;  20x + 45y = 39765
Solve   : Solve by elimination → x = 501, y = 661
Answer  : 501 lawn, 661 reserved

Status  : ready: two_priced_items answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0949'
KEY = 'system_of_equations/0949'
NAME = 'System of equations 0949'
CATEGORY = 'System of equations'
PROBLEM = 'A concert sold 1162 tickets: lawn seats at $20 and reserved seats at $45. Ticket sales totaled $39,765. How many of each were sold?'
LET = 'x = lawn, y = reserved'
EQUATION = 'x + y = 1162;  20x + 45y = 39765'
SOLVE = 'Solve by elimination → x = 501, y = 661'
ANSWER = '501 lawn, 661 reserved'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_priced_items'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A concert sold {0} tickets: lawn seats at ${1} and reserved seats at ${2}. Ticket sales totaled ${3}. How many of each were sold?'
NUMBERS = ['1162', '20', '45', '39765']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

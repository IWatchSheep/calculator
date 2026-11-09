"""Algebra word problem 0918   [System of equations]

Problem : A concert sold 1035 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $41,510. How many of each were sold?
Let     : x = lawn, y = reserved
Equation: x + y = 1035;  30x + 50y = 41510
Solve   : Solve by elimination → x = 512, y = 523
Answer  : 512 lawn, 523 reserved

Status  : ready: two_priced_items answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0918'
KEY = 'system_of_equations/0918'
NAME = 'System of equations 0918'
CATEGORY = 'System of equations'
PROBLEM = 'A concert sold 1035 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $41,510. How many of each were sold?'
LET = 'x = lawn, y = reserved'
EQUATION = 'x + y = 1035;  30x + 50y = 41510'
SOLVE = 'Solve by elimination → x = 512, y = 523'
ANSWER = '512 lawn, 523 reserved'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_priced_items'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A concert sold {0} tickets: lawn seats at ${1} and reserved seats at ${2}. Ticket sales totaled ${3}. How many of each were sold?'
NUMBERS = ['1035', '30', '50', '41510']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

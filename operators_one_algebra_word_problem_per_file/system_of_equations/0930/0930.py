"""Algebra word problem 0930   [System of equations]

Problem : A concert sold 867 tickets: lawn seats at $15 and reserved seats at $35. Ticket sales totaled $16,505. How many of each were sold?
Let     : x = lawn, y = reserved
Equation: x + y = 867;  15x + 35y = 16505
Solve   : Solve by elimination → x = 692, y = 175
Answer  : 692 lawn, 175 reserved

Status  : ready: two_priced_items answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0930'
KEY = 'system_of_equations/0930'
NAME = 'System of equations 0930'
CATEGORY = 'System of equations'
PROBLEM = 'A concert sold 867 tickets: lawn seats at $15 and reserved seats at $35. Ticket sales totaled $16,505. How many of each were sold?'
LET = 'x = lawn, y = reserved'
EQUATION = 'x + y = 867;  15x + 35y = 16505'
SOLVE = 'Solve by elimination → x = 692, y = 175'
ANSWER = '692 lawn, 175 reserved'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_priced_items'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A concert sold {0} tickets: lawn seats at ${1} and reserved seats at ${2}. Ticket sales totaled ${3}. How many of each were sold?'
NUMBERS = ['867', '15', '35', '16505']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

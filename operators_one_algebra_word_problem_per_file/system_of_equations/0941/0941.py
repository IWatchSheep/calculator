"""Algebra word problem 0941   [System of equations]

Problem : Omar bought 39 stamps, some at 50¢ and some at 75¢, for $23.00. How many of each?
Let     : x = 50¢ stamps, y = 75¢ stamps
Equation: x + y = 39;  50x + 75y = 2300
Solve   : Solve by elimination → x = 25, y = 14
Answer  : 25 at 50¢, 14 at 75¢

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0941'
KEY = 'system_of_equations/0941'
NAME = 'System of equations 0941'
CATEGORY = 'System of equations'
PROBLEM = 'Omar bought 39 stamps, some at 50¢ and some at 75¢, for $23.00. How many of each?'
LET = 'x = 50¢ stamps, y = 75¢ stamps'
EQUATION = 'x + y = 39;  50x + 75y = 2300'
SOLVE = 'Solve by elimination → x = 25, y = 14'
ANSWER = '25 at 50¢, 14 at 75¢'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Omar bought {0} stamps, some at {1}¢ and some at {2}¢, for ${3}. How many of each?'
NUMBERS = ['39', '50', '75', '23.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

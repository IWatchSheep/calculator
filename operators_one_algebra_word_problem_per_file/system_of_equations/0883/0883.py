"""Algebra word problem 0883   [System of equations]

Problem : Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65. How many of each?
Let     : x = 55¢ stamps, y = 70¢ stamps
Equation: x + y = 30;  55x + 70y = 1965
Solve   : Solve by elimination → x = 9, y = 21
Answer  : 9 at 55¢, 21 at 70¢

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0883'
KEY = 'system_of_equations/0883'
NAME = 'System of equations 0883'
CATEGORY = 'System of equations'
PROBLEM = 'Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65. How many of each?'
LET = 'x = 55¢ stamps, y = 70¢ stamps'
EQUATION = 'x + y = 30;  55x + 70y = 1965'
SOLVE = 'Solve by elimination → x = 9, y = 21'
ANSWER = '9 at 55¢, 21 at 70¢'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Noah bought {0} stamps, some at {1}¢ and some at {2}¢, for ${3}. How many of each?'
NUMBERS = ['30', '55', '70', '19.65']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

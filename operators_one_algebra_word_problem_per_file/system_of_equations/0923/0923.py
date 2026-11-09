"""Algebra word problem 0923   [System of equations]

Problem : Kofi bought 36 stamps, some at 55¢ and some at 70¢, for $21.30. How many of each?
Let     : x = 55¢ stamps, y = 70¢ stamps
Equation: x + y = 36;  55x + 70y = 2130
Solve   : Solve by elimination → x = 26, y = 10
Answer  : 26 at 55¢, 10 at 70¢

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0923'
KEY = 'system_of_equations/0923'
NAME = 'System of equations 0923'
CATEGORY = 'System of equations'
PROBLEM = 'Kofi bought 36 stamps, some at 55¢ and some at 70¢, for $21.30. How many of each?'
LET = 'x = 55¢ stamps, y = 70¢ stamps'
EQUATION = 'x + y = 36;  55x + 70y = 2130'
SOLVE = 'Solve by elimination → x = 26, y = 10'
ANSWER = '26 at 55¢, 10 at 70¢'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Kofi bought {0} stamps, some at {1}¢ and some at {2}¢, for ${3}. How many of each?'
NUMBERS = ['36', '55', '70', '21.30']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

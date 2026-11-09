"""Algebra word problem 0901   [System of equations]

Problem : Zane bought 24 stamps, some at 44¢ and some at 63¢, for $12.27. How many of each?
Let     : x = 44¢ stamps, y = 63¢ stamps
Equation: x + y = 24;  44x + 63y = 1227
Solve   : Solve by elimination → x = 15, y = 9
Answer  : 15 at 44¢, 9 at 63¢

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0901'
KEY = 'system_of_equations/0901'
NAME = 'System of equations 0901'
CATEGORY = 'System of equations'
PROBLEM = 'Zane bought 24 stamps, some at 44¢ and some at 63¢, for $12.27. How many of each?'
LET = 'x = 44¢ stamps, y = 63¢ stamps'
EQUATION = 'x + y = 24;  44x + 63y = 1227'
SOLVE = 'Solve by elimination → x = 15, y = 9'
ANSWER = '15 at 44¢, 9 at 63¢'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Zane bought {0} stamps, some at {1}¢ and some at {2}¢, for ${3}. How many of each?'
NUMBERS = ['24', '44', '63', '12.27']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

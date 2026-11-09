"""Algebra word problem 0153   [Distance (toward each other)]

Problem : Two trains start 115 miles apart and travel toward each other at 75 mph and 40 mph. When will they meet?
Let     : t = hours
Equation: 75t + 40t = 115
Solve   : 115t = 115 → t = 1
Answer  : 1 hour

Status  : ready: toward_each_other answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0153'
KEY = 'distance_toward_each_other/0153'
NAME = 'Distance (toward each other) 0153'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Two trains start 115 miles apart and travel toward each other at 75 mph and 40 mph. When will they meet?'
LET = 't = hours'
EQUATION = '75t + 40t = 115'
SOLVE = '115t = 115 → t = 1'
ANSWER = '1 hour'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'toward_each_other'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two trains start {0} miles apart and travel toward each other at {1} mph and {2} mph. When will they meet?'
NUMBERS = ['115', '75', '40']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

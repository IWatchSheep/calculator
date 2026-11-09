"""Algebra word problem 0150   [Distance (toward each other)]

Problem : Two trains start 142 miles apart and travel toward each other at 38 mph and 33 mph. When will they meet?
Let     : t = hours
Equation: 38t + 33t = 142
Solve   : 71t = 142 → t = 2
Answer  : 2 hours

Status  : ready: toward_each_other answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0150'
KEY = 'distance_toward_each_other/0150'
NAME = 'Distance (toward each other) 0150'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Two trains start 142 miles apart and travel toward each other at 38 mph and 33 mph. When will they meet?'
LET = 't = hours'
EQUATION = '38t + 33t = 142'
SOLVE = '71t = 142 → t = 2'
ANSWER = '2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'toward_each_other'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two trains start {0} miles apart and travel toward each other at {1} mph and {2} mph. When will they meet?'
NUMBERS = ['142', '38', '33']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

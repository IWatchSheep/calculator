"""Algebra word problem 0152   [Distance (toward each other)]

Problem : Emeka and Quinn live 362 miles apart. Emeka drives toward Quinn at 58 mph. 2 hours later, Quinn starts driving toward Emeka at 65 mph. How long after Quinn leaves do they meet?
Let     : t = hours Quinn drives
Equation: 58(t + 2) + 65t = 362
Solve   : 123t = 246 → t = 2
Answer  : 2 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0152'
KEY = 'distance_toward_each_other/0152'
NAME = 'Distance (toward each other) 0152'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Emeka and Quinn live 362 miles apart. Emeka drives toward Quinn at 58 mph. 2 hours later, Quinn starts driving toward Emeka at 65 mph. How long after Quinn leaves do they meet?'
LET = 't = hours Quinn drives'
EQUATION = '58(t + 2) + 65t = 362'
SOLVE = '123t = 246 → t = 2'
ANSWER = '2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Emeka and Quinn live {0} miles apart. Emeka drives toward Quinn at {1} mph. {2} hours later, Quinn starts driving toward Emeka at {3} mph. How long after Quinn leaves do they meet?'
NUMBERS = ['362', '58', '2', '65']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

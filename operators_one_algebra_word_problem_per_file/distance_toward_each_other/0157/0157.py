"""Algebra word problem 0157   [Distance (toward each other)]

Problem : Victor and Aiden live 327 miles apart. Victor drives toward Aiden at 63 mph. 1 hour later, Aiden starts driving toward Victor at 69 mph. How long after Aiden leaves do they meet?
Let     : t = hours Aiden drives
Equation: 63(t + 1) + 69t = 327
Solve   : 132t = 264 → t = 2
Answer  : 2 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0157'
KEY = 'distance_toward_each_other/0157'
NAME = 'Distance (toward each other) 0157'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Victor and Aiden live 327 miles apart. Victor drives toward Aiden at 63 mph. 1 hour later, Aiden starts driving toward Victor at 69 mph. How long after Aiden leaves do they meet?'
LET = 't = hours Aiden drives'
EQUATION = '63(t + 1) + 69t = 327'
SOLVE = '132t = 264 → t = 2'
ANSWER = '2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Victor and Aiden live {0} miles apart. Victor drives toward Aiden at {1} mph. {2} hour later, Aiden starts driving toward Victor at {3} mph. How long after Aiden leaves do they meet?'
NUMBERS = ['327', '63', '1', '69']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

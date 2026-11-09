"""Algebra word problem 0156   [Distance (toward each other)]

Problem : Carla and Zane live 370 miles apart. Carla drives toward Zane at 58 mph. 1 hour later, Zane starts driving toward Carla at 46 mph. How long after Zane leaves do they meet?
Let     : t = hours Zane drives
Equation: 58(t + 1) + 46t = 370
Solve   : 104t = 312 → t = 3
Answer  : 3 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0156'
KEY = 'distance_toward_each_other/0156'
NAME = 'Distance (toward each other) 0156'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Carla and Zane live 370 miles apart. Carla drives toward Zane at 58 mph. 1 hour later, Zane starts driving toward Carla at 46 mph. How long after Zane leaves do they meet?'
LET = 't = hours Zane drives'
EQUATION = '58(t + 1) + 46t = 370'
SOLVE = '104t = 312 → t = 3'
ANSWER = '3 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Carla and Zane live {0} miles apart. Carla drives toward Zane at {1} mph. {2} hour later, Zane starts driving toward Carla at {3} mph. How long after Zane leaves do they meet?'
NUMBERS = ['370', '58', '1', '46']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

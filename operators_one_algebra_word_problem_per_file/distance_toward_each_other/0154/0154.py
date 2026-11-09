"""Algebra word problem 0154   [Distance (toward each other)]

Problem : Yusuf and Theo live 618 miles apart. Yusuf drives toward Theo at 59 mph. 2 hours later, Theo starts driving toward Yusuf at 66 mph. How long after Theo leaves do they meet?
Let     : t = hours Theo drives
Equation: 59(t + 2) + 66t = 618
Solve   : 125t = 500 → t = 4
Answer  : 4 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0154'
KEY = 'distance_toward_each_other/0154'
NAME = 'Distance (toward each other) 0154'
CATEGORY = 'Distance (toward each other)'
PROBLEM = 'Yusuf and Theo live 618 miles apart. Yusuf drives toward Theo at 59 mph. 2 hours later, Theo starts driving toward Yusuf at 66 mph. How long after Theo leaves do they meet?'
LET = 't = hours Theo drives'
EQUATION = '59(t + 2) + 66t = 618'
SOLVE = '125t = 500 → t = 4'
ANSWER = '4 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Yusuf and Theo live {0} miles apart. Yusuf drives toward Theo at {1} mph. {2} hours later, Theo starts driving toward Yusuf at {3} mph. How long after Theo leaves do they meet?'
NUMBERS = ['618', '59', '2', '66']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

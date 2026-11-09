"""Algebra word problem 0984   [Work rate]

Problem : A new machine works 3 times as fast as an old one. Together they finish an order in 2.5 hours. How long would the old machine take alone?
Let     : x = old machine's time
Equation: 2.5/x + 2.5/(x/3) = 1
Solve   : Multiply through by x → x = 10
Answer  : 10 hours (new machine: 10/3 hours)

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0984'
KEY = 'work_rate/0984'
NAME = 'Work rate 0984'
CATEGORY = 'Work rate'
PROBLEM = 'A new machine works 3 times as fast as an old one. Together they finish an order in 2.5 hours. How long would the old machine take alone?'
LET = "x = old machine's time"
EQUATION = '2.5/x + 2.5/(x/3) = 1'
SOLVE = 'Multiply through by x → x = 10'
ANSWER = '10 hours (new machine: 10/3 hours)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A new machine works {0} times as fast as an old one. Together they finish an order in {1} hours. How long would the old machine take alone?'
NUMBERS = ['3', '2.5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

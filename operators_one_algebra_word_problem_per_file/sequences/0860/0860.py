"""Algebra word problem 0860   [Sequences]

Problem : A savings jar holds $15 in week 1 and grows by $6 each week. In which week does it hold $63?
Let     : n = week number
Equation: 15 + (n − 1)(6) = 63
Solve   : 6n = 54 → n = 9
Answer  : Week 9

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0860'
KEY = 'sequences/0860'
NAME = 'Sequences 0860'
CATEGORY = 'Sequences'
PROBLEM = 'A savings jar holds $15 in week 1 and grows by $6 each week. In which week does it hold $63?'
LET = 'n = week number'
EQUATION = '15 + (n − 1)(6) = 63'
SOLVE = '6n = 54 → n = 9'
ANSWER = 'Week 9'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A savings jar holds ${0} in week {1} and grows by ${2} each week. In which week does it hold ${3}?'
NUMBERS = ['15', '1', '6', '63']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

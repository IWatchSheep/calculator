"""Algebra word problem 0107   [Direct variation]

Problem : A spring stretches 7.5 cm under a 15 N force. Stretch varies directly with force. How far will it stretch under 40 N?
Let     : x = stretch
Equation: 7.5/15 = x/40
Solve   : x/40 = 0.5 → x = 0.5 × 40 = 20
Answer  : 20 cm

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0107'
KEY = 'direct_variation/0107'
NAME = 'Direct variation 0107'
CATEGORY = 'Direct variation'
PROBLEM = 'A spring stretches 7.5 cm under a 15 N force. Stretch varies directly with force. How far will it stretch under 40 N?'
LET = 'x = stretch'
EQUATION = '7.5/15 = x/40'
SOLVE = 'x/40 = 0.5 → x = 0.5 × 40 = 20'
ANSWER = '20 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A spring stretches {0} cm under a {1} N force. Stretch varies directly with force. How far will it stretch under {2} N?'
NUMBERS = ['7.5', '15', '40']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0363   [Inequality]

Problem : Hana has $157 to spend. There is a $25 entry fee, and T-shirts cost $12.00 each. What is the most T-shirts that can be bought?
Let     : n = number bought
Equation: 25 + 12n ≤ 157
Solve   : n ≤ 11 → n = 11 (largest whole number that works)
Answer  : 11 T-shirts

Status  : ready: most_you_can_buy answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0363'
KEY = 'inequality/0363'
NAME = 'Inequality 0363'
CATEGORY = 'Inequality'
PROBLEM = 'Hana has $157 to spend. There is a $25 entry fee, and T-shirts cost $12.00 each. What is the most T-shirts that can be bought?'
LET = 'n = number bought'
EQUATION = '25 + 12n ≤ 157'
SOLVE = 'n ≤ 11 → n = 11 (largest whole number that works)'
ANSWER = '11 T-shirts'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'most_you_can_buy'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Hana has ${0} to spend. There is a ${1} entry fee, and T-shirts cost ${2} each. What is the most T-shirts that can be bought?'
NUMBERS = ['157', '25', '12.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0388   [Inequality]

Problem : Wes has $138 to spend. There is a $8 entry fee, and bags of mulch cost $12.00 each. What is the most bags of mulch that can be bought?
Let     : n = number bought
Equation: 8 + 12n ≤ 138
Solve   : n ≤ 65/6 → n = 10 (largest whole number that works)
Answer  : 10 bags of mulch

Status  : ready: most_you_can_buy answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0388'
KEY = 'inequality/0388'
NAME = 'Inequality 0388'
CATEGORY = 'Inequality'
PROBLEM = 'Wes has $138 to spend. There is a $8 entry fee, and bags of mulch cost $12.00 each. What is the most bags of mulch that can be bought?'
LET = 'n = number bought'
EQUATION = '8 + 12n ≤ 138'
SOLVE = 'n ≤ 65/6 → n = 10 (largest whole number that works)'
ANSWER = '10 bags of mulch'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'most_you_can_buy'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Wes has ${0} to spend. There is a ${1} entry fee, and bags of mulch cost ${2} each. What is the most bags of mulch that can be bought?'
NUMBERS = ['138', '8', '12.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

"""Algebra word problem 0044   [Break-even]

Problem : Car rental A costs $45.00 plus $0.05 per mile. Plan B costs $41.00 plus $0.10 per mile. For how many miles do they cost the same?
Let     : x = number of miles
Equation: 45 + 0.05x = 41 + 0.1x
Solve   : 0.05x = 4 → x = 80
Answer  : 80 miles

Status  : ready: archive_break_even_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0044'
KEY = 'break_even/0044'
NAME = 'Break-even 0044'
CATEGORY = 'Break-even'
PROBLEM = 'Car rental A costs $45.00 plus $0.05 per mile. Plan B costs $41.00 plus $0.10 per mile. For how many miles do they cost the same?'
LET = 'x = number of miles'
EQUATION = '45 + 0.05x = 41 + 0.1x'
SOLVE = '0.05x = 4 → x = 80'
ANSWER = '80 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_break_even_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Car rental A costs ${0} plus ${1} per mile. Plan B costs ${2} plus ${3} per mile. For how many miles do they cost the same?'
NUMBERS = ['45.00', '0.05', '41.00', '0.10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

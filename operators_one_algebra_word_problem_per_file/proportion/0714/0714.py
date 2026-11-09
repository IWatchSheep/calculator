"""Algebra word problem 0714   [Proportion]

Problem : A lawn needs 3 kg of fertilizer per 25 m². How much is needed for 450 m²?
Let     : x = kg needed
Equation: 3/25 = x/450
Solve   : x/450 = 0.12 → x = 0.12 × 450 = 54
Answer  : 54 kg

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0714'
KEY = 'proportion/0714'
NAME = 'Proportion 0714'
CATEGORY = 'Proportion'
PROBLEM = 'A lawn needs 3 kg of fertilizer per 25 m². How much is needed for 450 m²?'
LET = 'x = kg needed'
EQUATION = '3/25 = x/450'
SOLVE = 'x/450 = 0.12 → x = 0.12 × 450 = 54'
ANSWER = '54 kg'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A lawn needs {0} kg of fertilizer per {1} m². How much is needed for {2} m²?'
NUMBERS = ['3', '25', '450']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

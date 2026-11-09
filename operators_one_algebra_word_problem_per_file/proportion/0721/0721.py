"""Algebra word problem 0721   [Proportion]

Problem : A lawn needs 3 kg of fertilizer per 50 m². How much is needed for 1400 m²?
Let     : x = kg needed
Equation: 3/50 = x/1400
Solve   : x/1400 = 0.06 → x = 0.06 × 1400 = 84
Answer  : 84 kg

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0721'
KEY = 'proportion/0721'
NAME = 'Proportion 0721'
CATEGORY = 'Proportion'
PROBLEM = 'A lawn needs 3 kg of fertilizer per 50 m². How much is needed for 1400 m²?'
LET = 'x = kg needed'
EQUATION = '3/50 = x/1400'
SOLVE = 'x/1400 = 0.06 → x = 0.06 × 1400 = 84'
ANSWER = '84 kg'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A lawn needs {0} kg of fertilizer per {1} m². How much is needed for {2} m²?'
NUMBERS = ['3', '50', '1400']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

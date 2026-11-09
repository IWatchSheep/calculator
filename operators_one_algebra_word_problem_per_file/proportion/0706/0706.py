"""Algebra word problem 0706   [Proportion]

Problem : A lawn needs 5 kg of fertilizer per 20 m². How much is needed for 120 m²?
Let     : x = kg needed
Equation: 5/20 = x/120
Solve   : x/120 = 0.25 → x = 0.25 × 120 = 30
Answer  : 30 kg

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0706'
KEY = 'proportion/0706'
NAME = 'Proportion 0706'
CATEGORY = 'Proportion'
PROBLEM = 'A lawn needs 5 kg of fertilizer per 20 m². How much is needed for 120 m²?'
LET = 'x = kg needed'
EQUATION = '5/20 = x/120'
SOLVE = 'x/120 = 0.25 → x = 0.25 × 120 = 30'
ANSWER = '30 kg'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A lawn needs {0} kg of fertilizer per {1} m². How much is needed for {2} m²?'
NUMBERS = ['5', '20', '120']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

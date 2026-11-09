"""Algebra word problem 0809   [Ratio]

Problem : The ratio of Gus's marbles to Kira's is 6:5. After Gus gives Kira 16 marbles, the ratio is 4:7. How many did each have at first?
Let     : k = scale factor
Equation: (6k − 16)/(5k + 16) = 4/7
Solve   : Multiply both sides by the denominator and collect terms → k = 8
Answer  : Gus 48, Kira 40

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0809'
KEY = 'ratio/0809'
NAME = 'Ratio 0809'
CATEGORY = 'Ratio'
PROBLEM = "The ratio of Gus's marbles to Kira's is 6:5. After Gus gives Kira 16 marbles, the ratio is 4:7. How many did each have at first?"
LET = 'k = scale factor'
EQUATION = '(6k − 16)/(5k + 16) = 4/7'
SOLVE = 'Multiply both sides by the denominator and collect terms → k = 8'
ANSWER = 'Gus 48, Kira 40'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "The ratio of Gus's marbles to Kira's is {0}:{1}. After Gus gives Kira {2} marbles, the ratio is {3}:{4}. How many did each have at first?"
NUMBERS = ['6', '5', '16', '4', '7']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

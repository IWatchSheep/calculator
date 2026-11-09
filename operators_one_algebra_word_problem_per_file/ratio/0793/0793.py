"""Algebra word problem 0793   [Ratio]

Problem : The ratio of Ben's marbles to Carla's is 3:5. After Ben gives Carla 16 marbles, the ratio is 1:7. How many did each have at first?
Let     : k = scale factor
Equation: (3k − 16)/(5k + 16) = 1/7
Solve   : Multiply both sides by the denominator and collect terms → k = 8
Answer  : Ben 24, Carla 40

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0793'
KEY = 'ratio/0793'
NAME = 'Ratio 0793'
CATEGORY = 'Ratio'
PROBLEM = "The ratio of Ben's marbles to Carla's is 3:5. After Ben gives Carla 16 marbles, the ratio is 1:7. How many did each have at first?"
LET = 'k = scale factor'
EQUATION = '(3k − 16)/(5k + 16) = 1/7'
SOLVE = 'Multiply both sides by the denominator and collect terms → k = 8'
ANSWER = 'Ben 24, Carla 40'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "The ratio of Ben's marbles to Carla's is {0}:{1}. After Ben gives Carla {2} marbles, the ratio is {3}:{4}. How many did each have at first?"
NUMBERS = ['3', '5', '16', '1', '7']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

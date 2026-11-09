"""Algebra word problem 0782   [Ratio]

Problem : The ratio of Yusuf's marbles to Dev's is 3:5. After Yusuf gives Dev 12 marbles, the ratio is 1:7. How many did each have at first?
Let     : k = scale factor
Equation: (3k − 12)/(5k + 12) = 1/7
Solve   : Multiply both sides by the denominator and collect terms → k = 6
Answer  : Yusuf 18, Dev 30

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0782'
KEY = 'ratio/0782'
NAME = 'Ratio 0782'
CATEGORY = 'Ratio'
PROBLEM = "The ratio of Yusuf's marbles to Dev's is 3:5. After Yusuf gives Dev 12 marbles, the ratio is 1:7. How many did each have at first?"
LET = 'k = scale factor'
EQUATION = '(3k − 12)/(5k + 12) = 1/7'
SOLVE = 'Multiply both sides by the denominator and collect terms → k = 6'
ANSWER = 'Yusuf 18, Dev 30'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "The ratio of Yusuf's marbles to Dev's is {0}:{1}. After Yusuf gives Dev {2} marbles, the ratio is {3}:{4}. How many did each have at first?"
NUMBERS = ['3', '5', '12', '1', '7']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

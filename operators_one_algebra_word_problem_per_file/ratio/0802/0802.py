"""Algebra word problem 0802   [Ratio]

Problem : The ratio of Yusuf's marbles to Zane's is 5:6. After Yusuf gives Zane 18 marbles, the ratio is 2:9. How many did each have at first?
Let     : k = scale factor
Equation: (5k − 18)/(6k + 18) = 2/9
Solve   : Multiply both sides by the denominator and collect terms → k = 6
Answer  : Yusuf 30, Zane 36

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0802'
KEY = 'ratio/0802'
NAME = 'Ratio 0802'
CATEGORY = 'Ratio'
PROBLEM = "The ratio of Yusuf's marbles to Zane's is 5:6. After Yusuf gives Zane 18 marbles, the ratio is 2:9. How many did each have at first?"
LET = 'k = scale factor'
EQUATION = '(5k − 18)/(6k + 18) = 2/9'
SOLVE = 'Multiply both sides by the denominator and collect terms → k = 6'
ANSWER = 'Yusuf 30, Zane 36'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "The ratio of Yusuf's marbles to Zane's is {0}:{1}. After Yusuf gives Zane {2} marbles, the ratio is {3}:{4}. How many did each have at first?"
NUMBERS = ['5', '6', '18', '2', '9']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

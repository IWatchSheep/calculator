"""Algebra word problem 0787   [Ratio]

Problem : The ratio of Hana's marbles to Maya's is 1:1. After Hana gives Maya 23 marbles, the ratio is 1:3. How many did each have at first?
Let     : k = scale factor
Equation: (k − 23)/(k + 23) = 1/3
Solve   : Multiply both sides by the denominator and collect terms → k = 46
Answer  : Hana 46, Maya 46

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0787'
KEY = 'ratio/0787'
NAME = 'Ratio 0787'
CATEGORY = 'Ratio'
PROBLEM = "The ratio of Hana's marbles to Maya's is 1:1. After Hana gives Maya 23 marbles, the ratio is 1:3. How many did each have at first?"
LET = 'k = scale factor'
EQUATION = '(k − 23)/(k + 23) = 1/3'
SOLVE = 'Multiply both sides by the denominator and collect terms → k = 46'
ANSWER = 'Hana 46, Maya 46'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "The ratio of Hana's marbles to Maya's is {0}:{1}. After Hana gives Maya {2} marbles, the ratio is {3}:{4}. How many did each have at first?"
NUMBERS = ['1', '1', '23', '1', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

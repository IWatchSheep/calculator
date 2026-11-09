"""Algebra word problem 0779   [Ratio]

Problem : The ratio of boys to girls in a class is 3:8. After 4 more girls join, the ratio becomes 1:3. How many students were there originally?
Let     : k = scale factor (boys = 3k, girls = 8k)
Equation: 3k/(8k + 4) = 1/3
Solve   : Multiply both sides by the denominator and collect terms → k = 4
Answer  : 44 students (12 boys, 32 girls)

Status  : ready: class_ratio_after_join answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0779'
KEY = 'ratio/0779'
NAME = 'Ratio 0779'
CATEGORY = 'Ratio'
PROBLEM = 'The ratio of boys to girls in a class is 3:8. After 4 more girls join, the ratio becomes 1:3. How many students were there originally?'
LET = 'k = scale factor (boys = 3k, girls = 8k)'
EQUATION = '3k/(8k + 4) = 1/3'
SOLVE = 'Multiply both sides by the denominator and collect terms → k = 4'
ANSWER = '44 students (12 boys, 32 girls)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'class_ratio_after_join'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The ratio of boys to girls in a class is {0}:{1}. After {2} more girls join, the ratio becomes {3}:{4}. How many students were there originally?'
NUMBERS = ['3', '8', '4', '1', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

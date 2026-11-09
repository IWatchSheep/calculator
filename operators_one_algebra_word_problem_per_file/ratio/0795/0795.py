"""Algebra word problem 0795   [Ratio]

Problem : The ratio of boys to girls in a class is 6:8. After 7 more girls join, the ratio becomes 2:3. How many students were there originally?
Let     : k = scale factor (boys = 6k, girls = 8k)
Equation: 6k/(8k + 7) = 2/3
Solve   : Multiply both sides by the denominator and collect terms → k = 7
Answer  : 98 students (42 boys, 56 girls)

Status  : ready: class_ratio_after_join answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0795'
KEY = 'ratio/0795'
NAME = 'Ratio 0795'
CATEGORY = 'Ratio'
PROBLEM = 'The ratio of boys to girls in a class is 6:8. After 7 more girls join, the ratio becomes 2:3. How many students were there originally?'
LET = 'k = scale factor (boys = 6k, girls = 8k)'
EQUATION = '6k/(8k + 7) = 2/3'
SOLVE = 'Multiply both sides by the denominator and collect terms → k = 7'
ANSWER = '98 students (42 boys, 56 girls)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'class_ratio_after_join'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The ratio of boys to girls in a class is {0}:{1}. After {2} more girls join, the ratio becomes {3}:{4}. How many students were there originally?'
NUMBERS = ['6', '8', '7', '2', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

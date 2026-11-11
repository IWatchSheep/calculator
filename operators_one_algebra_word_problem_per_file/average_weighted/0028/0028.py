"""Algebra word problem 0028   [Average (weighted)]

Problem : A course grade is 70% coursework and 30% final exam. Lena has a coursework average of 87. What final exam score gives an overall grade of 81?
Let     : f = final exam score
Equation: 0.7(87) + 0.3f = 81
Solve   : 0.3f = 20.1 → f = 67
Answer  : 67

Status  : ready: course_grade_final_exam answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0028'
KEY = 'average_weighted/0028'
NAME = 'Average (weighted) 0028'
CATEGORY = 'Average (weighted)'
PROBLEM = 'A course grade is 70% coursework and 30% final exam. Lena has a coursework average of 87. What final exam score gives an overall grade of 81?'
LET = 'f = final exam score'
EQUATION = '0.7(87) + 0.3f = 81'
SOLVE = '0.3f = 20.1 → f = 67'
ANSWER = '67'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'course_grade_final_exam'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A course grade is {0}% coursework and {1}% final exam. Lena has a coursework average of {2}. What final exam score gives an overall grade of {3}?'
NUMBERS = ['70', '30', '87', '81']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)

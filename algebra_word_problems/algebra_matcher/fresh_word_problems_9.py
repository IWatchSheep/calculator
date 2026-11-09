"""Ninth fresh set for word_solver.py: two-purchase wordings written AFTER the family was finished, run once, untuned.
Each item: (problem, the two prices increasing) or None = must decline."""
from fractions import Fraction

FRESH = [
    ("A pen and a notebook cost $4.50. Three pens and two notebooks cost $11.00. What is the price of each?", [2, Fraction(5, 2)]),
    ("Two sodas and one hot dog cost $9.50. One soda and two hot dogs cost $11.50. Find the price of one of each.", [Fraction(5, 2), Fraction(9, 2)]),
    ("3 adult passes and 2 student passes cost $62. 1 adult pass and 4 student passes cost $54. Find the price of one of each.", [10, 14]),
    ("A bagel and a coffee cost $5.00. Two bagels and a coffee cost $7.25. How much does each cost?", [Fraction(9, 4), Fraction(11, 4)]),
    ("A pen and a notebook cost $4.50. Two such pens and three notebooks cost $11.00. Find the price of each.", None),
    ("Two pens and a pad cost $5.00. Four pens and two pads cost $10.00. Find the price of each.", None),
    ("A ticket and a snack cost $12. Two tickets and a snack cost $20. I paid with $50. Find the price of each.", None),
    ("Three apples and two pears cost $4.20. Find the price of each.", None),
]

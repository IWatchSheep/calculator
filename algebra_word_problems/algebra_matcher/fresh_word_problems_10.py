"""Tenth fresh set for word_solver.py: two-purchase wordings written AFTER the plural fix ("passes" = "pass") and the
"each / apiece / per after a price" rule, run once, untuned.  Each item: (problem, prices increasing) or None = decline."""
from fractions import Fraction

FRESH = [
    ("2 boxes and 1 jar cost $9. 1 box and 3 jars cost $13. Find the price of one of each.", [Fraction(14, 5), Fraction(17, 5)]),
    ("A sandwich and a juice cost $7. Two sandwiches and three juices cost $17.50. Find the price of each.", [Fraction(7, 2), Fraction(7, 2)]),
    ("Two ties and a belt cost $50. A tie and two belts cost $55. Find the price of one of each.", [15, 20]),
    ("A cherry pie and a lemon pie cost $15. Two cherry pies and a lemon pie cost $26. Find the price of each.", [4, 11]),
    ("3 hats and 2 caps cost $40 together. 1 hat and 4 caps cost $35. Find the price of one of each.", [Fraction(13, 2), 9]),
    ("A pen and a pad cost $3 each. Two pens and a pad cost $5. Find the price of each.", None),
    ("2 apples and 3 pears cost $5 apiece. 4 apples and 1 pear cost $6. Find the price of one of each.", None),
]

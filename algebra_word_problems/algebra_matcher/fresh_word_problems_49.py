"""Forty-ninth fresh set for word_solver.py: neighbours of the batch-45 families (percent spent with money or fuel left, a price minus a coupon, complementary and supplementary angles),
written AFTER the families were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

FRESH = [
    ("Omar spent 60% of an allowance on games and had $48 left. How much was the allowance?", [Fraction(120)]),
    ("After burning 40% of the fuel in a tank, 90 liters remain. How much fuel was there at first?", [Fraction(150)]),
    ("Lena spent 100% of a paycheck on rent and had $50 left. How much was the paycheck?", None),
    ("Lena spent 20% of a paycheck on rent and had $0 left. How much was the paycheck?", None),
    ("Lena spent 20% of a paycheck on rent and $50 on food and had $300 left. How much was the paycheck?", None),
    ("After using 30% of the fuel in a tank, 70 liters remain. How much did the tank hold?", None),
    ("Plants cost $4.50 each. With a $5 coupon, Tara paid $40.00. How many plants were bought?", [Fraction(10)]),
    ("Magazines cost $3 each. With a $2 coupon, Sol paid $20.00. How many magazines were bought?", None),
    ("Sandwiches cost $6 each. With a $10 coupon, Ana paid $8.00. How many sandwiches were bought?", None),
    ("Sandwiches cost $6 each. With a $10 coupon, Ana paid $38.00. How many sandwiches were bought?", [Fraction(8)]),
    ("Two angles are supplementary. One angle is 10 more than 3 times the other. Find both angles.", [Fraction(85, 2), Fraction(275, 2)]),
    ("Two angles are complementary. One angle is 40 less than 2 times the other. Find both angles.", [Fraction(130, 3), Fraction(140, 3)]),
    # (first written as a required decline by mistake: 190/3 and 80/3 are both positive and add to 90, so the answer is right)
    ("Two angles are complementary. One angle is 100 less than 2 times the other. Find both angles.", [Fraction(80, 3), Fraction(190, 3)]),
    ("Two angles are complementary. One angle is 12 less than 5 times the other. Find the larger angle.", None),
    ("Two angles are complementary. One angle is 12 less than 5 times the other and the bigger is 3 more than that. Find both angles.", None),
]

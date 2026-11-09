"""Fifteenth fresh set for word_solver.py: wordings for the three families added with the 'or' fix (still_water_current, ratio_split,
three_numbers), written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

FRESH = [
    ("A kayaker paddles 18 km downstream in 2 hours and 10 km upstream in 2 hours. How fast is the current?", [2]),
    ("A motorboat goes 45 miles with the current in 3 hours and 20 miles against the current in 2 hours. What is the speed of the boat in still water?", [Fraction(25, 2)]),
    ("A boat goes 20 km upstream in 2 hours and 30 km downstream in 2 hours. What is the speed of the boat in still water?", [Fraction(25, 2)]),
    ("Sand is mixed with cement in the ratio 3:1. How much cement is needed for 24 kg of sand?", [8]),
    ("The ratio of flour to sugar is 5:2. If I use 20 cups of flour, how many cups of sugar do I need?", [8]),
    ("Red and blue paint are mixed in the ratio 2:3. How much blue is needed for 10 litres of red?", [15]),
    ("The sum of three numbers is 60. The first two add to 35 and the second and third add to 40. Find the numbers.", [15, 20, 25]),
    ("Three numbers add up to 45. The first and last add to 30 and the last two add to 25. What are the numbers?", [10, 15, 20]),
    ("A boat goes 20 km downstream in 2 hours and 20 km upstream in 2 hours. How fast is the current?", None),
    ("A rower goes 12 km downstream in 2 hours and 18 km upstream in 2 hours. What is the speed in still water?", None),
    ("Water is mixed into concentrate in the ratio 5:1. How much of each is needed for 30 litres of water?", None),
    ("Sand is mixed with cement in the ratio 3:1. How much cement is needed for 24 kg of sand in total?", None),
    ("The sum of three numbers is 30. The first two add to 18 and the last two add to 20. What is the largest?", None),
    ("The sum of three numbers is 30. The first two add to 18 and the last two add to 20, and one is twice another.", None),
    ("You have $60. You can buy tickets at $12 or snacks at $4 each. How many snacks can you afford?", None),
]

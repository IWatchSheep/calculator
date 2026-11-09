"""Twenty-fourth fresh set for word_solver.py: wordings for the unit-of-the-question fix and the three families added together (line_from_two_points,
election_margin, wind_same_time), written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("For a cab ride, 3 miles cost $27 and 8 miles cost $52. The cost is C = m·x + b. How many miles cost $82?", [14]),
    ("A plumber charges for time: 2 hours cost $95 and 6 hours cost $215. The cost is linear. How many hours cost $335?", [10]),
    ("In a race between two people, the winner received 62% of the votes and won by 2,400 votes. How many votes were cast?", [10000]),
    ("The winner took 55% of the vote and won by 1,200 votes. How many votes were cast?", [12000]),
    ("A plane flies 900 miles with a 30 mph tailwind in the same time it flies 780 miles into that wind. What is its speed in still air?", [420]),
    ("A jet flies 2,100 km with a 50 km/h tailwind in the same time it flies 1,800 km into the same wind as a headwind. What is the jet's speed in still air?", [650]),
    ("For a cab ride, 3 miles cost $27 and 8 miles cost $52 and 5 miles cost $40. The cost is linear. How many miles cost $82?", None),
    ("The winner got 58% of the votes and won by 3,393 votes. How many votes were cast?", None),
    ("A plane flies 780 miles with a 30 mph tailwind in the same time it flies 900 miles into that wind. What is its speed in still air?", None),
    ("A plane flies 900 miles with a 30 mph tailwind in the same time it flies 780 miles into that wind. What is the wind speed?", None),
    ("A gym plan costs $40 a month and includes 10 hours of court time. Each extra hour costs $6. The bill was $76. How many days were used?", None),
]

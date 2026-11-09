"""Twenty-third fresh set for word_solver.py: wordings for the unit fix and the three families added together (two_priced_items, plan_with_included,
most_that_fits), written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

FRESH = [
    ("A market sold 20 lb of two coffees, one at $4/lb and one at $9/lb, for $120. How many lb of each?", [8, 12]),
    ("A theater sold 300 tickets: balcony seats at $20 and floor seats at $35. Ticket sales totaled $7,500. How many of each?", [100, 200]),
    ("A school play sold 150 tickets: adult tickets at $12 and student tickets at $7. Sales came to $1,380. How many of each?", [66, 84]),
    ("A gym plan costs $40 a month and includes 10 hours of court time. Each extra hour costs $6. The bill was $76. How many hours were used?", [16]),
    ("A cloud plan costs $20 a month and includes 100 GB. Every additional GB costs $2. The total came to $60. How many GB were stored?", [120]),
    ("A freight lift holds at most 2,000 kg. A 80 kg operator is loading 45 kg crates. How many crates can be carried with the operator?", [42]),
    ("A truck can carry up to 900 lb. A 150 lb driver sits in front and 40 lb sacks are loaded. How many sacks can the truck take?", [18]),
    ("A market sold 20 oz of two coffees, one at $4/lb and one at $9/lb, for $120. How many lb of each?", None),
    ("A theater sold 300 tickets: balcony seats at $20, floor seats at $35 and box seats at $60. Ticket sales totaled $7,500. How many of each?", None),
    ("A theater sold 300 tickets: balcony seats at $20 and floor seats at $35. Ticket sales totaled $7,501. How many of each?", None),
    ("A gym plan costs $40 a month and includes 10 hours of court time. Each extra hour costs $6. The bill was $40. How many hours were used?", None),
    ("A lift holds at most 500 lb. A 520 lb worker is loading 20 lb boxes. How many boxes can go up with the worker?", None),
    ("A lift holds at most 500 lb. A 100 lb worker is loading 20 lb boxes. How many boxes can go up in two trips?", None),
]

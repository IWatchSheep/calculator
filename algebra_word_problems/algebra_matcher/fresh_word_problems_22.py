"""Twenty-second fresh set for word_solver.py: wordings for the families added together (two teas / two coffees at two prices, two rates on one pile,
the least number sold for a profit), written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A bakery sold 40 lb of two flours, one at $2/lb and one at $3/lb, for $95. How many lb of each?", [15, 25]),
    ("A shop sold 50 kg of two coffees, one at $8/kg and one at $10/kg, for $424. How many kg of each?", [12, 38]),
    ("A farm sold 60 kg of two fruits, one at $2/kg and one at $5/kg, for $210. How many kg of each?", [30, 30]),
    ("Two printers print 40 and 60 pages per minute. Working together, how long will they take to print 1,500 pages?", [15]),
    ("Two pumps move 25 and 15 gallons per hour. Working together, how many hours will they take to move 200 gallons?", [5]),
    ("A club dinner costs $450 to host. Plates are $15. How many plates must be sold for a profit of at least $600?", [70]),
    ("A fair costs $1,200 to organize. Wristbands sell for $7 each. How many wristbands must be sold for a profit of at least $900?", [300]),
    ("Two pumps move 25 and 15 gallons per hour. Working together, how many minutes will they take to move 200 gallons?", None),
    ("Two pumps move 25 and 15 gallons per hour. Working together, how many gallons do they move in one hour?", None),
    ("A club dinner costs $450 to host. Plates are $15. How many plates must be sold for a profit of at most $600?", None),
    ("A club dinner costs $450 to host. Plates are $15. How many plates must be sold for a profit of at least $600 if 5 are free?", None),
]

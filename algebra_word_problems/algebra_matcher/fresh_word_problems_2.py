"""Second fresh set for word_solver.py: written AFTER the three cue changes (service charge, how far, machine) and run
once without tuning.  Same format as fresh_word_problems.py: (problem, answers increasing) or None = must decline.
The first fresh set (fresh_word_problems.py) is now a development set."""
from fractions import Fraction

FRESH = [
    # ---- percent change (incl. "service charge")
    ("A hotel bill with a 10% service charge came to $418. What was the bill before the service charge?", [380]),
    ("A meal cost $345 including a 15% service charge. What was the price before the service charge?", [300]),
    ("After a 25% markup, a bike is priced at $250. What was the wholesale cost?", [200]),
    ("After a 30% discount, a chair costs $140. What was the original price?", [200]),
    ("Her salary rose 4% to $62,400. What was her salary before the raise?", [60000]),
    ("A laptop is on sale for $720 after 10% off. What was the price before the sale?", [800]),
    ("A shirt costs $60 after a 20% discount. What is the discount in dollars?", None),
    ("A bill of $90 includes a $10 service charge. What was it before the service charge?", None),
    # ---- proportion (incl. "how far" and "machine")
    ("A cyclist rides 36 km in 3 hours. At that rate, how far will they ride in 8 hours?", [96]),
    ("A bus covers 210 miles in 6 hours. How far does it go in 9 hours?", [315]),
    ("A bakery machine makes 150 rolls in 5 hours. How many rolls does it make in 12 hours?", [360]),
    ("A press stamps 90 plates in 15 minutes. How many plates does it stamp in 40 minutes?", [240]),
    ("A printer prints 48 pages in 3 minutes. How many pages will it print in 10 minutes?", [160]),
    ("If 4 apples cost $3, how much do 14 apples cost?", [Fraction(21, 2)]),
    ("A garden hose uses 30 litres in 4 minutes. How many litres does it use in 10 minutes?", [75]),
    ("A recipe uses 3 eggs for 12 muffins. How many eggs for 20 muffins?", [5]),
    ("A car goes 50 mph for 2 hours. How far does it go?", None),
    ("If 8 workers paint a house in 6 days, how many days for 12 workers?", None),
    # ---- sum and difference, consecutive, work together
    ("The sum of two numbers is 64 and their difference is 10. Find the numbers.", [27, 37]),
    ("Two numbers add up to 100 and one is 24 bigger than the other. Find them.", [38, 62]),
    ("Three consecutive even integers add up to 108. What are they?", [34, 36, 38]),
    ("The sum of 4 consecutive integers is 94. What are they?", [22, 23, 24, 25]),
    ("The sum of two consecutive integers is 35. What are the integers?", [17, 18]),
    ("Ann can wash a car in 20 minutes and Bea can wash it in 30 minutes. How long will they take working together?", [12]),
    ("One hose fills a tub in 12 minutes and another hose fills it in 6 minutes. How long does it take with both hoses running?", [4]),
    ("Two taps fill a tank, one in 6 hours and the other in 12 hours. How long does the other tap need alone?", None),
    ("A 40 cm stick is cut into two pieces. One piece is 4 times the other. How long is each piece?", None),
]

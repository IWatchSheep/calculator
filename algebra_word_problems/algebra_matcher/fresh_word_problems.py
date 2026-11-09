"""Fresh wordings for word_solver.py, written (with hand-calculated answers) after the solver was finished and
run once without tuning.  Each item: (problem, answers).  answers = list of the numbers asked for, in increasing order;
None means "this is not a plain problem of the five families: the solver must decline"."""
from fractions import Fraction

FRESH = [
    # ---- sum and difference
    ("The sum of two numbers is 90 and their difference is 14. Find the numbers.", [38, 52]),
    ("Two numbers add up to 71 and one of them is 9 larger than the other. What are they?", [31, 40]),
    ("A 120 cm rope is cut into two pieces. One piece is 30 cm longer than the other. How long are the pieces?", [45, 75]),
    ("Dev is 6 years older than Mia. The sum of their ages is 40. How old is each?", [17, 23]),
    ("The sum of two numbers is 30 and their product is 200. Find the numbers.", None),
    ("The sum of two numbers is 21 and one is twice the other. Find the numbers.", None),
    # ---- consecutive integers
    ("The sum of 3 consecutive integers is 60. Find them.", [19, 20, 21]),
    ("Five consecutive integers sum to 105. What are they?", [19, 20, 21, 22, 23]),
    ("Three odd integers in a row total 87. What are they?", [27, 29, 31]),
    ("The sum of 2 consecutive even integers is 90. What are they?", [44, 46]),
    ("The product of two consecutive integers is 56. Find them.", [7, 8]),   # was a required decline until the consecutive_product family
    ("The sum of 3 consecutive integers is 61. Find them.", None),
    # ---- two workers together
    ("Ann can paint a room in 6 hours and Bob can paint it in 3 hours. Working together, how long will they take?", [2]),
    ("Pipe A fills a pool in 10 hours and pipe B fills it in 15 hours. How long does it take if both are open?", [6]),
    ("Two machines finish an order in 8 hours and 12 hours respectively. How long will it take them together?", [Fraction(24, 5)]),
    ("Tara and Joe together mow a lawn in 4 hours. Tara alone takes 6 hours. How long would Joe take alone?", None),
    ("A tap fills a tank in 5 hours but a leak empties it in 8 hours. How long to fill it with both going?", None),
    # ---- a price after a percent change
    ("After a 20% discount, a jacket costs $64. What was the original price?", [80]),
    ("A phone costs $330 after a 10% price increase. What was the price before the increase?", [300]),
    ("The bill including a 12% service charge was $224. What was the bill before the charge?", [200]),
    ("Prices fell 15% and a coat now costs $170. What was it before?", [200]),
    ("Her rent went up 8% to $1,350. What was the old rent?", [1250]),
    ("A shirt costs $40 and is 25% off. What is the sale price?", None),
    ("A shirt is 25% off, saving $10. What was the original price?", None),
    ("A jacket is 20% off. It costs $64 now. What does it cost after another 10% off?", None),
    # ---- direct proportion
    ("If 5 pens cost $12.50, how much do 12 pens cost?", [30]),
    ("A machine makes 240 bolts in 8 hours. How many bolts does it make in 20 hours?", [600]),
    ("A train travels 150 km in 2 hours. At that rate, how far does it go in 5 hours?", [375]),
    ("A recipe needs 2 cups of flour for 12 cookies. How many cookies can I make with 5 cups?", [30]),
    ("A 3 kg bag of rice costs $9. How much does an 8 kg bag cost?", [24]),
    ("If 6 workers build a wall in 12 days, how long would 9 workers take?", None),
    ("A car goes 60 mph for 3 hours then 40 mph for 2 hours. How far does it go in all?", None),
    ("Tickets cost $8 each. How much do 5 tickets cost?", None),
]

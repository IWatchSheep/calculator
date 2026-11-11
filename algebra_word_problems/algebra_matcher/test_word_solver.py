"""Tests for word_solver.py.   Run:  python test_word_solver.py

1. Phrasings for each of the five families, and problems it must decline.
2. Ground truth: every one of the 1,000 generated problems either gets None or the stored answer (a wrong answer fails).
3. The 100 hand-written matcher problems: every claim must be in the table of hand-calculated answers below.
4. 33 fresh wordings (fresh_word_problems.py), written after the solver was finished and run once, untuned.
"""
import os
import re
import sys
import unittest
from fractions import Fraction

import number_puzzle as NP
import word_solver as WS
from test_number_puzzle import load_problems

# Answers worked out by hand for the hand-written matcher problems the solver claims.
HAND_ANSWERS = {
    "What percent of 80 is 20?": [25],
    "Find two numbers that add to 50 if one is 8 bigger than the other.": [21, 29],
    "Add up three integers in a row and you get 138. Which integers?": [45, 46, 47],
    "Shoes are 30% off and now cost $56. What did they cost before the sale?": [80],
    "My pay went up 4% and I now make $52,000. What was I making before?": [50000],
    "With 8% sales tax my receipt says $54. What was the price before tax?": [50],
    "After a 15% tip the lunch came to $46. How much was lunch before tip?": [40],
    "A recipe for 4 people needs 300 g of pasta. How much pasta for 10 people?": [750],
    "A store buys a lamp and adds 40% to sell it for $70. What did the store pay?": [50],
    "Four odd numbers in a row sum to 96. List them.": [21, 23, 25, 27],
    "One printer finishes a job in 4 hours and another in 12 hours. Running both, how long does the job take?": [3],
    "Tom paints a fence alone in 6 hours, Sue in 3. If they team up, how long does it take?": [2],
    "A TV is marked down 25% to $450. What was the original price?": [600],
    "Rent went up 5% to $1,260 a month. What was the old rent?": [1200],
    "If 3 kg of apples cost $7.50, how much do 8 kg cost?": [20],
    "I put some money in an account at 3% and the rest at 5%, $10,000 total. I earned $420 in interest in a year. How much was at 5%?": [4000, 6000],
    "$8,000 was invested, some at 6% and some at 4%. The total yearly interest was $400. How much was invested at 6%?": [4000, 4000],
    "An apple and a pear cost $1.30. Two apples and three pears cost $3.40. Find the price of each.": [Fraction(1, 2), Fraction(4, 5)],
    "Coffee worth $6 a pound is mixed with coffee worth $10 a pound to make 40 lb worth $7 a pound. How much of each?": [10, 30],
    "I have $200 and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same?": [15],
    "My test marks are 70, 85 and 90. What do I need on the fourth test to average 85?": [95],
    "On a farm there are some hens and some sheep. Altogether I count 30 heads and 84 feet. How many sheep?": [12, 18],
    "How many sides does a polygon have if its inside angles total 1440 degrees?": [10],
    "Two cars leave the same spot heading in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 km apart?": [3],
    "Two even numbers that come one after another multiply to 168. What are they?": [12, 14],
    "Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. When do they meet?": [2],
    "The product of two consecutive odd numbers is 143. Find them.": [11, 13],
    "You have $45. A movie costs $9 per ticket. What is the greatest number of tickets you can buy?": [5],
    "Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of water?": [6],
    "The sum of three numbers is 30. The first two add to 18 and the last two add to 20. What are the numbers?": [8, 10, 12],
    "Rowing with the current I cover 24 km in 2 h, but against it only 12 km in 2 h. What's my rowing speed in still water?": [9],
    "A bacteria colony doubles every 3 hours. Starting at 500 cells, when will there be 8000?": [12],
    "A radioactive sample halves every 5 years. When does 160 g become 20 g?": [15],
    "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph along the same road. When does the car catch the cyclist?": [1],
    "An investment of bacteria... a yeast culture triples every 2 hours, starting at 10 cells. When does it reach 810?": [8],
    "Town X has 50,000 people and gains 1,000 a year; Town Y has 80,000 and loses 500 a year. When are they equal?": [20],
    "Using d = rt, how long does a 210 km trip take at 70 km/h?": [3],
    "You need 20 litres of 30% acid. You have 10% and 50% acid. How much of the 10% do you use?": [10, 10],
    "How many ounces of a 20% sugar syrup must be combined with 50% syrup to get 30 oz of 40% syrup?": [10, 20],
}


def answers(problem):
    r = WS.solve(problem)
    return None if r is None else sorted(Fraction(v) for v in r.values)


def values(*xs):
    return sorted(Fraction(x) for x in xs)


class SourceHygiene(unittest.TestCase):
    def test_no_control_characters_in_the_source(self):
        # "\\b" written inside a normal string becomes a backspace: that once disabled a check in word_solver.py
        here = os.path.dirname(os.path.abspath(__file__))
        for name in ("word_solver.py", "number_puzzle.py"):
            with open(os.path.join(here, name), encoding="utf-8") as f:
                text = f.read()
            bad = [i for i, c in enumerate(text) if ord(c) < 32 and c not in "\n\r\t"]
            self.assertEqual(bad, [], name + " contains control characters")


class Families(unittest.TestCase):
    def test_sum_difference(self):
        self.assertEqual(answers("The sum of two numbers is 235 and their difference is 103. Find the numbers."), values(66, 169))
        self.assertEqual(answers("Two numbers add up to 71 and one of them is 9 larger than the other. What are they?"), values(31, 40))
        self.assertEqual(answers("A 93 cm board is cut into two pieces. One piece is 25 cm longer than the other. How long is each piece?"), values(34, 59))
        self.assertEqual(answers("Kofi is 2 years older than Priya. The sum of their ages is 38. How old is each?"), values(18, 20))
        self.assertIsNone(answers("The sum of two numbers is 30 and their product is 200. Find the numbers."))
        self.assertIsNone(answers("The sum of two numbers is 20 and their difference is 30. Find the numbers."))   # a negative number

    def test_consecutive(self):
        self.assertEqual(answers("The sum of 3 consecutive even integers is 84. What are the integers?"), values(26, 28, 30))
        self.assertEqual(answers("Three odd integers in a row total 87. What are they?"), values(27, 29, 31))
        self.assertIsNone(answers("The sum of 3 consecutive integers is 61. Find them."))            # no whole answer
        self.assertIsNone(answers("The sum of 3 consecutive odd integers is 60. Find them."))          # parity does not fit
        # a product of two consecutive integers was a required decline here until the consecutive_product family; it is now answered (7 and 8)
        self.assertEqual(answers("The product of two consecutive integers is 56. Find them."), values(7, 8))

    def test_work_together(self):
        self.assertEqual(answers("Elena can clean the house in 4 hours. Vera can do it in 6 hours. How long will it take them working together?"), values(Fraction(12, 5)))
        # "alone" describes the separate times; the question asks for the time together
        self.assertEqual(answers("Tom paints a fence alone in 6 hours, Sue in 3. If they team up, how long does it take?"), values(2))
        self.assertIsNone(answers("Tara and Joe together mow a lawn in 4 hours. Tara alone takes 6 hours. How long would Joe take alone?"))
        # the combined time is already in the setup, so the question's "together" must not make it a separate worker
        self.assertIsNone(answers("Tara and Joe together mow a lawn in 4 hours. Tara alone takes 6 hours. How long do they take working together?"))
        self.assertIsNone(answers("Working together, Ann and Bob finish a job in 4 hours. Ann takes 6 hours alone. How long will it take them working together?"))
        self.assertIsNone(answers("Working together they take 5 hours. How long do they take together?"))
        self.assertIsNone(answers("Working together, two gardeners weed a park in 6 hours. One alone would need 10 hours. How long would the other need alone?"))
        self.assertIsNone(answers("A tap fills a tank in 5 hours but a leak empties it in 8 hours. How long to fill it with both going?"))
        # spelled multipliers of the workers or their rates (found by Grok); "Two machines ..." as the shape of the problem stays
        self.assertIsNone(answers("Ann can wash a car in 20 minutes and Bea can wash it in 30 minutes. How long will two such pairs take working together?"))
        self.assertIsNone(answers("Tom paints a fence alone in 6 hours, Sue in 3. If two teams like them team up, how long does it take?"))
        self.assertIsNone(answers("Ann can wash a car in 20 minutes and Bea can wash it in 30 minutes. How long will both pairs take working together?"))
        # the bare word "both" must keep working
        self.assertEqual(answers("One printer finishes a job in 4 hours and another in 12 hours. Running both, how long does the job take?"), values(3))
        self.assertEqual(answers("Two machines finish an order in 8 hours and 12 hours respectively. How long will it take them together?"), values(Fraction(24, 5)))
        # regression: found by this test file, the stem "empt" must also catch "empties", "leaks" and "plug"
        self.assertIsNone(answers("A tap fills a bath in 10 minutes but the plug leaks and empties it in 30 minutes. With both going, how long to fill it?"))

    def test_partner_alone_from_together(self):
        cases = [
            ("Working together, Hiro and Nia can finish a job in 3 hours. Hiro alone takes 4 hours. How long would Nia take alone?", 12),
            ("Working together, Rhea and Emeka can finish a job in 4 hours. Rhea alone takes 12 hours. How long would Emeka take alone?", 6),
            ("Working together, Omar and Fatima can finish a job in 3 hours. Omar alone takes 12 hours. How long would Fatima take alone?", 4),
            ("Working together, Noah and Victor can finish a job in 6 hours. Noah alone takes 12 hours. How long would Victor take alone?", 12),
            ("Working together, Gus and Sam can finish a job in 3 hours. Gus alone takes 6 hours. How long would Sam take alone?", 6),
        ]
        for sentence, expected in cases:
            self.assertEqual(answers(sentence), values(expected), sentence)
        self.assertIsNone(answers("Working together, Hiro and Nia can finish a job in 3 hours. Nia alone takes 4 hours. How long would Hiro take alone?"))
        self.assertIsNone(answers("Working together, Hiro and Nia can finish a job in 3 hours. Hiro alone takes 4 hours. How long do they take working together?"))
        self.assertIsNone(WS.work_together("Working together, Hiro and Nia can finish a job in 3 hours. Hiro alone takes 4 hours. How long would Nia take alone?"))

    def test_course_grade_final_exam(self):
        cases = [
            ("A course grade is 75% coursework and 25% final exam. Elena has a coursework average of 96. What final exam score gives an overall grade of 86?", 56),
            ("A course grade is 60% coursework and 40% final exam. Rhea has a coursework average of 80. What final exam score gives an overall grade of 88?", 100),
            ("A course grade is 70% coursework and 30% final exam. Lena has a coursework average of 87. What final exam score gives an overall grade of 81?", 67),
            ("A course grade is 60% coursework and 40% final exam. Ivan has a coursework average of 97. What final exam score gives an overall grade of 85?", 67),
            ("A course grade is 60% coursework and 40% final exam. Gus has a coursework average of 79. What final exam score gives an overall grade of 85?", 94),
        ]
        for sentence, expected in cases:
            self.assertEqual(answers(sentence), values(expected), sentence)
        self.assertIsNone(answers("A course grade is 75% coursework and 20% final exam. Elena has a coursework average of 96. What final exam score gives an overall grade of 86?"))
        self.assertIsNone(answers("A course grade is 75% coursework and 25% final exam. Elena has a coursework average of 96. What coursework average gives an overall grade of 86?"))

    def test_round_trip_lake_distance(self):
        cases = [
            ("Aiden drove to a lake at 30 mph and returned on the same road at 20 mph. The round trip took 5 hours. How far is the lake?", 60),
            ("Bea drove to a lake at 60 mph and returned on the same road at 30 mph. The round trip took 10 hours. How far is the lake?", 200),
            ("Kofi drove to a lake at 40 mph and returned on the same road at 20 mph. The round trip took 6 hours. How far is the lake?", 80),
            ("Isla drove to a lake at 45 mph and returned on the same road at 30 mph. The round trip took 2 hours. How far is the lake?", 36),
            ("Tara drove to a lake at 45 mph and returned on the same road at 36 mph. The round trip took 8 hours. How far is the lake?", 160),
        ]
        for sentence, expected in cases:
            self.assertEqual(answers(sentence), values(expected), sentence)
        self.assertIsNone(answers("Aiden drove to a lake at 30 mph and returned on the same road at 20 mph. The round trip took 5 hours. How long was the drive?"))
        self.assertIsNone(answers("Aiden drove to a lake at 30 mph. The round trip took 5 hours. How far is the lake?"))

    def test_three_painters_together(self):
        cases = [
            ("Gus, Rosa, and Bea can each paint a room alone in 12, 30, and 3 hours. How long will it take all three together?", Fraction(20, 9)),
            ("Aiden, Lena, and Yara can each paint a room alone in 8, 30, and 20 hours. How long will it take all three together?", Fraction(24, 5)),
            ("Quinn, Jamal, and Sam can each paint a room alone in 24, 20, and 30 hours. How long will it take all three together?", Fraction(8)),
            ("Grace, Uma, and Omar can each paint a room alone in 10, 30, and 24 hours. How long will it take all three together?", Fraction(40, 7)),
            ("Sofia, Grace, and Sam can each paint a room alone in 24, 15, and 10 hours. How long will it take all three together?", Fraction(24, 5)),
        ]
        for sentence, expected in cases:
            self.assertEqual(answers(sentence), values(expected), sentence)
        self.assertIsNone(answers("Gus and Rosa can each paint a room alone in 12 and 30 hours. How long will it take all three together?"))
        self.assertIsNone(answers("Gus, Rosa, and Bea can each paint a room alone in 12, 30, and 3 hours. How long would Gus take alone?"))

    def test_seesaw_balance_distance(self):
        cases = [
            ("On a seesaw, weight \u00d7 distance from the pivot must be equal on both sides. Jade (69 kg) sits 3 m from the pivot. How far from the pivot must Theo (36 kg) sit to balance?", Fraction(23, 4)),
            ("On a seesaw, weight \u00d7 distance from the pivot must be equal on both sides. Yara (36 kg) sits 6 m from the pivot. How far from the pivot must Priya (54 kg) sit to balance?", Fraction(4)),
            ("On a seesaw, weight \u00d7 distance from the pivot must be equal on both sides. Sofia (66 kg) sits 6 m from the pivot. How far from the pivot must Mateo (22 kg) sit to balance?", Fraction(18)),
            ("On a seesaw, weight \u00d7 distance from the pivot must be equal on both sides. Ivan (35 kg) sits 1 m from the pivot. How far from the pivot must Pablo (70 kg) sit to balance?", Fraction(1, 2)),
            ("On a seesaw, weight \u00d7 distance from the pivot must be equal on both sides. Sam (30 kg) sits 3 m from the pivot. How far from the pivot must Sofia (72 kg) sit to balance?", Fraction(5, 4)),
        ]
        for sentence, expected in cases:
            self.assertEqual(answers(sentence), values(expected), sentence)
        self.assertIsNone(answers("On a seesaw, weight \u00d7 distance from the pivot must be equal on both sides. Jade (69 kg) sits 3 m from the pivot. How far from the pivot must Jade (36 kg) sit to balance?"))
        self.assertIsNone(answers("On a seesaw, weight \u00d7 distance from the pivot must be equal on both sides. Jade (69 kg) sits 3 m from the pivot. How heavy is Theo?"))

    def test_percent_change(self):
        self.assertEqual(answers("After a 5% raise, Vera's salary is $32,550.00. What was the salary before the raise?"), values(31000))
        self.assertEqual(answers("A TV is marked down 25% to $450. What was the original price?"), values(600))
        self.assertEqual(answers("A store marks up a rug by 100% and sells it for $240.00. What did the store pay for it?"), values(120))
        # the question asks for the AFTER value, or the known amount is a saving: never answer
        self.assertIsNone(answers("A shirt costs $40 and is 25% off. What is the sale price?"))
        self.assertIsNone(answers("A shirt is 25% off, saving $10. What was the original price?"))
        # a number written as a word multiplies the thing asked about ("two coats"): decline (found by Grok)
        self.assertIsNone(answers("After a 15% discount, two coats cost $170. What was the original price of one?"))
        self.assertIsNone(answers("Prices fell 15% and a coat now costs $170. What did two coats cost before?"))
        # counts hidden in words: "both coats", "a pair of phones", "a couple of coats" (found by Grok)
        self.assertIsNone(answers("After a 15% discount, both coats cost $170. What was the original price of one?"))
        self.assertIsNone(answers("Prices rose 20% and a pair of phones now costs $360. What did one cost before?"))
        self.assertIsNone(answers("Prices rose 20% and a couple of phones now cost $360. What did one cost before?"))
        # "service charge" (two words) is a rise; the bare word "charge" is not
        self.assertEqual(answers("The bill including a 12% service charge was $224. What was the bill before the charge?"), values(200))
        self.assertIsNone(answers("A bill of $90 includes a $10 service charge. What was it before the service charge?"))
        self.assertIsNone(answers("After a 20% discount and a 5% tax, a TV costs $400. What was the original price?"))

    def test_proportion(self):
        self.assertEqual(answers("If 5 pens cost $12.50, how much do 12 pens cost?"), values(30))
        self.assertEqual(answers("A car travels 480 miles on 15 gallons of gas. At this rate, how many gallons are needed for 736 miles?"), values(Fraction(736, 32)))
        # "how far" is a question word; "machine" is a noun, not a reason to decline (workers still are)
        self.assertEqual(answers("A train travels 150 km in 2 hours. At that rate, how far does it go in 5 hours?"), values(375))
        self.assertEqual(answers("A machine makes 240 bolts in 8 hours. How many bolts does it make in 20 hours?"), values(600))
        self.assertIsNone(answers("A car goes 60 mph for 3 hours then 40 mph for 2 hours. How far does it go in all?"))
        # cue verbs added in batch 3 (covers, stamps, prints)
        self.assertEqual(answers("A bus covers 210 miles in 6 hours. How far does it go in 9 hours?"), values(315))
        self.assertEqual(answers("A press stamps 90 plates in 15 minutes. How many plates does it stamp in 40 minutes?"), values(240))
        self.assertEqual(answers("A printer prints 48 pages in 3 minutes. How many pages will it print in 10 minutes?"), values(160))
        # a number written as a word has no role: "two printers" doubles the answer, so decline (found by fresh set 3)
        self.assertIsNone(answers("If a printer prints 48 pages in 3 minutes, how many pages will two printers print in 10 minutes?"))
        self.assertIsNone(answers("A copier prints 75 sheets in 5 minutes. How many sheets will it print in 12 minutes if it runs twice as fast?"))
        self.assertIsNone(answers("If 6 workers build a wall in 12 days, how long would 9 workers take?"))
        self.assertIsNone(answers("Sam earns $20/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $950. How many overtime hours were worked?"))
        # two typists on one pile of words was a required decline here until the two_rates_one_pile family; it is now answered (16 minutes)
        self.assertEqual(answers("Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1440 words?"), values(16))

    def test_price_blend(self):
        # the percent mixture with prices: p1*x + p2*(T - x) = blend*T
        self.assertEqual(answers("How many pounds of coffee at $6 per pound must be mixed with coffee at $10 per pound to make 40 lb worth $7 per pound?"), values(10, 30))
        self.assertEqual(answers("Coffee worth $6 a pound is mixed with coffee worth $10 a pound to make 40 lb worth $7 a pound. How many pounds of each?"), values(10, 30))
        self.assertEqual(answers("40 lb of a blend of nuts selling for $7/lb is made from nuts costing $6/lb and $10/lb. How many pounds of each are used?"), values(10, 30))
        # the source prices in the other order give the same two amounts
        self.assertEqual(answers("How many pounds of coffee at $10 per pound must be mixed with coffee at $6 per pound to make 40 lb worth $7 per pound?"), values(10, 30))
        # exact amounts, equation in the reading
        r = WS.solve("How many pounds of tea at $4 a pound and tea at $9 a pound should be combined to make 10 lb of a blend worth $5 a pound?")
        self.assertEqual(r.values, [Fraction(8), Fraction(2)])
        r = WS.solve("How many pounds of tea at $3 a pound and tea at $8 a pound should be combined to make 10 lb of a blend worth $4 a pound?")
        self.assertEqual(r.values, [Fraction(8), Fraction(2)])
        r = WS.solve("How many pounds of tea at $4 a pound and tea at $9 a pound should be combined to make 10 lb of a blend worth $6 a pound?")
        self.assertIn("4x + 9(10 - x) = 6(10)", r.reading)
        self.assertIn("6 lb at $4 and 4 lb at $9", r.reading)
        # other shapes decline: adding to a known amount (a different equation), a price outside the two, a spelled count, a percent,
        # a price that is not per pound, a missing question, three kinds
        self.assertIsNone(answers("How many pounds of $6 a pound coffee must be added to 10 lb of $10 a pound coffee to make a blend worth $7 a pound?"))
        self.assertIsNone(answers("How many pounds of coffee at $6 per pound must be mixed with coffee at $10 per pound to make 40 lb worth $12 per pound?"))
        self.assertIsNone(answers("How many pounds of coffee at $6 per pound must be mixed with coffee at $10 per pound to make 40 lb worth $6 per pound?"))
        self.assertIsNone(answers("How many pounds of coffee at $6 per pound must be mixed with coffee at $10 per pound to make three 40 lb batches worth $7 per pound?"))
        self.assertIsNone(answers("How many pounds of coffee at $6 per pound must be mixed with coffee at $10 per pound to make 40 lb worth $7 per pound, with 5% waste?"))
        self.assertIsNone(answers("Coffee at $6 a pound and coffee at $10 a pound are mixed to make 40 lb worth $7 a pound."))
        self.assertIsNone(answers("How many pounds of coffee at $6 a pound and $10 a pound make 40 lb worth $7 a bag?"))

    def test_price_with_for_each(self):
        # "$5 for each" and "$5 a piece" are the price of ONE item, like "$5 each" (found by Grok)
        self.assertIsNone(answers("2 apples and 3 pears cost $5 for each. 4 apples and 1 pear cost $6. Find the price of one of each."))
        self.assertIsNone(answers("2 apples and 3 pears cost $5 a piece. 4 apples and 1 pear cost $6. Find the price of one of each."))
        # "Find the price of one of each" stays answered: "each" there does not follow a price
        self.assertEqual(answers("An apple and a pear cost $1.30. Two apples and three pears cost $3.40. Find the price of one of each."), values(Fraction(1, 2), Fraction(4, 5)))

    def test_two_solution_mix(self):
        self.assertEqual(answers("How many liters of a 25% juice drink must be mixed with a 50% juice drink to make 100 liters of a 39% juice drink?"), values(44, 56))
        self.assertEqual(answers("One alloy is 10% silver and another is 50% silver. How many kilograms of each are needed to make 20 kg of an alloy that is 16% silver?"), values(3, 17))
        self.assertEqual(answers("You need 20 litres of 30% acid. You have 10% and 50% acid. How much of the 10% do you use?"), values(10, 10))
        self.assertEqual(answers("How many ounces of a 20% sugar syrup must be combined with 50% syrup to get 30 oz of 40% syrup?"), values(10, 20))
        # other mixing shapes: water, pure, evaporate, drain, replace, price per pound, adding to an existing amount
        self.assertIsNone(answers("How much pure water should I pour into 8 litres of 40% bleach solution to make it 25%?"))
        self.assertIsNone(answers("How many liters of water must be added to 10 liters of a 40% solution to make it 25%?"))
        self.assertIsNone(answers("How many liters of a 20% solution must be added to 10 liters of a 50% solution to make a 40% solution?"))
        # (a price-per-pound blend was a decline here until the price_blend family: it is not a percent mixture, see test_price_blend)
        self.assertIsNone(answers("A 12-litre bucket of 60% paint thinner is diluted with water down to 40%. How much water is added?"))
        # a spelled count of three or more ("three batches") is a number with no role (the word boundary was once stored as a backspace)
        self.assertIsNone(answers("How many liters of a 20% acid and a 50% acid are needed to make 20 liters of 30% acid if I mix three batches?"))
        # the reading shows exact amounts, never a rounded decimal
        r = WS.solve("How many liters of a 20% acid solution must be mixed with a 50% acid solution to make 20 liters of a 30% acid solution?")
        self.assertEqual(r.values, [Fraction(20, 1) * 2 / 3, Fraction(20, 1) / 3])
        self.assertIn("40/3 liters of the 20%", r.reading)
        self.assertIn("20/3 liters of the 50%", r.reading)
        self.assertNotIn("13.3333", r.reading)
        # the target is not between the two sources, the percents are not all there, or a ratio is given
        self.assertIsNone(answers("How many liters of a 10% solution and a 30% solution make 10 liters of a 40% solution?"))
        self.assertIsNone(answers("Mixing 5 liters of a 20% solution with 5 liters of a 40% solution gives what percent?"))
        self.assertIsNone(answers("A 30% solution and a 60% solution make 12 liters of 50% solution, with three times as much of the stronger one. How much of each?"))

    def test_two_rate_interest(self):
        self.assertEqual(answers("Emeka invests $24,000.00, part at 3% and the rest at 5% simple annual interest. After one year the total interest is $920.00. How much was invested at each rate?"), values(10000, 14000))
        self.assertEqual(answers("I put some money in an account at 3% and the rest at 5%, $10,000 total. I earned $420 in interest in a year. How much was at 5%?"), values(4000, 6000))
        self.assertEqual(answers("$8,000 was invested, some at 6% and some at 4%. The total yearly interest was $400. How much was invested at 6%?"), values(4000, 4000))
        # other interest shapes: time, equal interest, an extra amount, compound, commission, one amount at one rate only
        self.assertIsNone(answers("How many years will it take $24,500.00 to earn $11,025.00 in simple interest at 5% per year?"))
        self.assertIsNone(answers("$25,000.00 is split between two accounts paying 10% and 6% simple interest. Both accounts earn the same interest in a year. How much is in each?"))
        self.assertIsNone(answers("Tara has $12,000.00 invested at 3%. How much more must be invested at 8% so that the total earns 7% overall?"))
        self.assertIsNone(answers("Ben invests $9,000, part at 4% and the rest at 6%, compounded monthly. The interest after a year is $450. How much at each rate?"))
        self.assertIsNone(answers("A salesperson gets $500 a week plus 5% of sales. Last week they got $1,100. What were their sales?"))
        self.assertIsNone(answers("A bank pays 3% on $4,000 and 5% on another amount. The total interest is $380. How much is the other amount?"))
        # a cue for a real split can also match another sentence (found by Grok): "two such investments", and "part / the rest" of a YEAR
        self.assertIsNone(answers("Lea invests $10,000, part at 3% and the rest at 5%. Two such investments earn $420 in interest in one year. How much is in each?"))
        self.assertIsNone(answers("I invest $10,000 at 4% for part of the year and the rest of the year at 6%. The interest was $500. How much was at each rate?"))
        # the interest is not between the two possible extremes: no split can give it
        self.assertIsNone(answers("Leo invests $10,000, part at 3% and the rest at 5%. After one year the interest is $900. How much was invested at each rate?"))

    def test_two_purchases(self):
        # the counts are the roles, including counts written as words
        self.assertEqual(answers("An apple and a pear cost $1.30. Two apples and three pears cost $3.40. Find the price of each."), values(Fraction(1, 2), Fraction(4, 5)))
        self.assertEqual(answers("Three pens and one notebook cost $6.50. One pen and two notebooks cost $5.25. Find the price of each."), values(Fraction(31, 20), Fraction(37, 20)))
        self.assertEqual(answers("4 apples and 2 oranges cost $5.00. 6 apples and 1 oranges cost $6.50. Find the price of one of each."), values(1, Fraction(1, 2)))
        # the second purchase names the items the other way round
        self.assertEqual(answers("2 apples and 1 pear cost $2.00. 1 pear and 3 apples cost $2.70. Find the price of each."), values(Fraction(3, 5), Fraction(7, 10)))
        r = WS.solve("An apple and a pear cost $1.30. Two apples and three pears cost $3.40. Find the price of each.")
        self.assertIn("1x + 1y = 1.3", r.reading)
        self.assertIn("2x + 3y = 3.4", r.reading)
        # a price followed by "each" is the price of ONE item, not the total of the purchase (found by Grok)
        self.assertIsNone(answers("2 apples and 3 pears cost $5 each. 4 apples and 1 pear cost $6. Find the price of one of each."))
        self.assertIsNone(answers("2 apples and 3 pears cost $5 apiece. 4 apples and 1 pear cost $6. Find the price of one of each."))
        self.assertIsNone(answers("2 apples and 3 pears cost $5 per piece. 4 apples and 1 pear cost $6. Find the price of one of each."))
        # plural forms: "passes" and "pass" are the same item, and the reading keeps the words as written
        self.assertEqual(answers("3 adult passes and 2 student passes cost $62. 1 adult pass and 4 student passes cost $54. Find the price of one of each."), values(10, 14))
        r = WS.solve("5 burgers and 1 fries cost $55.30. 4 burgers and 2 fries cost $54.50. Find the price of one of each.")
        self.assertIn("'fries'", r.reading)
        self.assertNotIn("frie'", r.reading)
        self.assertEqual(WS._singular("passes"), WS._singular("pass"))
        self.assertEqual(WS._singular("sandwiches"), WS._singular("sandwich"))
        # "two such" is not a count of items; a count with no role, three items, one statement, other items, dependent equations
        self.assertIsNone(answers("An apple and a pear cost $1.30. Two such apples and three pears cost $3.40. Find the price of each."))
        self.assertIsNone(answers("An apple and a pear cost $1.30. Twice as many apples and three pears cost $3.40. Find the price of each."))
        self.assertIsNone(answers("An apple and a pear cost $1.30. Two apples and three pears cost $3.40. I have $10. Find the price of each."))
        self.assertIsNone(answers("Three apples and two pears cost $4.20. Find the price of each."))
        self.assertIsNone(answers("One apple and one pear cost $1.30. Two plums and three pears cost $3.40. Find the price of each."))
        self.assertIsNone(answers("Two pens and a pad cost $5.00. Four pens and two pads cost $10.00. Find the price of each."))
        self.assertIsNone(answers("An apple and a pear cost $1.30. Two apples and three pears cost $0.50. Find the price of each."))
        # a different system: coins / heads and legs / a total count are not two purchases
        self.assertIsNone(answers("Pens cost 50 cents and pencils 20 cents. I bought 18 items for $5.70. How many pens?"))

    def test_every_number_needs_a_role(self):
        # one extra number the patterns do not use -> decline, whatever the rest says
        self.assertIsNone(answers("The sum of two numbers is 90 and their difference is 14. Find the numbers between 1 and 100."))
        self.assertIsNone(answers("After a 20% discount, a jacket costs $64. What was the original price? It was on sale for 3 days."))


class GroundTruth(unittest.TestCase):
    @staticmethod
    def numbers_of(text, problem=None):
        if re.search(r"\$[\d,.]+ each", text):                                   # two prices: compare the dollars
            return sorted(Fraction(x.replace(",", "")) for x in re.findall(r"\$([\d,]+(?:\.\d+)?)", text))
        if re.search(r"\$[\d,.]+ at \d+(?:\.\d+)?%", text):                # an interest answer: compare the dollars, not the rates
            return sorted(Fraction(x.replace(",", "")) for x in re.findall(r"\$([\d,]+(?:\.\d+)?)", text))
        if re.search(r"^\d+ (?:weeks|months|days) \(each will have", text):      # a savings answer: compare the time, not the amount each has
            return [Fraction(re.match(r"\d+", text).group())]
        if re.search(r"\d\s?(?:lb|kg) at \$", text):                           # a price-blend answer: compare the weights, not the prices
            return sorted(Fraction(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s?(?:lb|kg)\b", text))
        if len(re.findall(r"(\d+(?:\.\d+)?)\s+(?:[a-z]+\s+)?at\s+[$\d]", text)) == 2:         # "9 at 55c, 21 at 70c" / "31 hours at $16, 30 hours at $22": compare the counts, not the prices
            return sorted(Fraction(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s+(?:[a-z]+\s+)?at\s+[$\d]", text))
        am = re.match(r"x = (-?\d+(?:\.\d+)?); each angle is (\d+(?:\.\d+)?)", text)
        if am:                                                        # "x = 38; each angle is 80 degrees": compare what the QUESTION asked for
            ask = (problem or "").lower()
            if re.search(r"\bfind x and the angle\b", ask):
                return sorted([Fraction(am.group(1)), Fraction(am.group(2))])                  # "Find x and the angle": both numbers
            if re.search(r"\bfind x\b", ask):
                return [Fraction(am.group(1))]                                                 # "Find x": x alone
            return [Fraction(am.group(2))]                                                     # "Find the angle" (or no problem text): the angle alone
        if re.search(r"\d\s?(?:L|kg) of", text):                       # a mixture answer: compare the amounts, not the percents
            return sorted(Fraction(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s?(?:L|kg)\b", text))
        text = re.sub(r"\([^)]*\)", "", text)
        text = re.sub(r"(?<=\d),(?=\d{3})", "", text)
        return sorted(Fraction(x) for x in re.findall(r"-?\d+(?:\.\d+)?(?:/\d+)?", text))

    def test_never_wrong_on_generated_problems(self):
        problems = load_problems()
        if not problems:
            self.skipTest("algebra_word_problems.txt not found")
        claimed, wrong, fam = 0, [], {}
        for p in problems:
            r = WS.solve(p["problem"])
            if r is None:
                continue
            claimed += 1
            fam[r.family] = fam.get(r.family, 0) + 1
            got, want = sorted(Fraction(v) for v in r.values), self.numbers_of(p["answer"], p["problem"])
            if not (len(got) == len(want) and all(abs(a - b) <= Fraction(1, 200) for a, b in zip(got, want))):
                wrong.append((r.family, p["problem"], [float(v) for v in got], p["answer"]))
        print("\n  generated problems: %d, claimed %d %s, wrong %d" % (len(problems), claimed, dict(sorted(fam.items())), len(wrong)))
        for w in wrong[:8]:
            print("   WRONG", w)
        self.assertEqual(wrong, [])
        self.assertGreater(claimed, 50)


class HandSets(unittest.TestCase):
    def test_claims_match_the_hand_calculated_answers(self):
        import algebra_matcher as AM
        claimed = 0
        for text, _ok in AM.HAND_TEST + AM.FRESH_TEST:
            if NP.solve(text) is not None:
                continue                                            # the number-puzzle reader answers these
            got = answers(text)
            if got is None:
                continue
            claimed += 1
            self.assertIn(text, HAND_ANSWERS, "claimed a problem with no hand-calculated answer: " + text)
            self.assertEqual(got, values(*HAND_ANSWERS[text]), text)
        print("\n  hand-written problems claimed by the family solver: %d (all match the hand-calculated answers)" % claimed)
        self.assertEqual(claimed, len(HAND_ANSWERS))


def score(table):
    """(solved, declined, required declines, wrong-or-unexpected) for a table of (problem, answers-or-None)."""
    solved = declined = required = 0
    for text, want in table:
        got = answers(text)
        if want is None:
            assert got is None, "should decline: " + text
            required += 1
        elif got is None:
            declined += 1
        else:
            assert got == values(*want), text
            solved += 1
    return solved, declined, required


class DevelopmentWordings(unittest.TestCase):
    """The first 33 fresh wordings.  They found the three cue gaps that were then fixed, so they are now a
    development set: every one with an answer must be solved and every required decline must still decline."""

    def test_development(self):
        from fresh_word_problems import FRESH
        solved, declined, required = score(FRESH)
        print("  development wordings (first fresh set): %d solved, %d declined, %d required declines correct" % (solved, declined, required))
        self.assertEqual((solved, declined, required), (22, 0, 11))      # 21/0/12 before consecutive_product answered the product-of-integers item


class DevelopmentWordingsLater(unittest.TestCase):
    """Fresh sets 2 and 3 became development sets when they led to changes (cue verbs; the spelled-number rule)."""

    def test_second_and_third_sets(self):
        from fresh_word_problems_2 import FRESH as F2
        from fresh_word_problems_3 import FRESH as F3
        self.assertEqual(score(F2), (22, 0, 5))      # it scored 18 solved / 3 declined before the cue verbs were added; "A car goes 50 mph for 2 hours" became an answer (100) with distance_speed_time
        self.assertEqual(score(F3), (9, 1, 5))       # it had 1 WRONG answer (two printers) before the spelled-number rule


class FreshWordings(unittest.TestCase):
    """8 wordings written AFTER the spelled-number rules for percent_change and work_together and run once, untuned
    (fresh_word_problems_5.py): 4 with an answer, 4 that must be declined.  A wrong answer is a failure."""

    def test_fresh(self):
        from fresh_word_problems_5 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (fifth set): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 0, 4))

    def test_mixture_sets(self):
        """Sets 6 and 7 were written after the two-solution mixture family and run once, untuned.  Set 6's declines
        repeat sentences in the unit tests (so only its 4 answers are an independent check); set 7 is fully independent."""
        from fresh_word_problems_6 import FRESH as F6
        from fresh_word_problems_7 import FRESH as F7
        s6, s7 = score(F6), score(F7)
        print("  fresh wordings (sixth set, mixtures): %d of 5 solved, %d of 5 required declines correct, 0 wrong" % (s6[0], s6[2]))
        print("  fresh wordings (seventh set, mixtures): %d of 2 solved, %d of 3 required declines correct, 0 wrong" % (s7[0], s7[2]))
        # its pounds-of-coffee-at-$6-and-$10 item was a required decline (not a percent mixture) and is now the price_blend answer 10 and 30
        self.assertEqual(s6, (5, 0, 5))
        self.assertEqual(s7, (2, 0, 3))

    def test_interest_set(self):
        """Set 8: two-rate interest wordings written after the family and run once, untuned.  One answer is declined
        because "splits" is not one of the split cue words; one of its declines repeats a sentence from the unit tests."""
        from fresh_word_problems_8 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (eighth set, interest): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 1, 4))

    def test_two_purchase_set(self):
        """Set 9 was written after the two-purchase family and run once, untuned: 3 solved, 1 declined ("adult passes /
        adult pass": the plural stripping made "passe" and "pas").  After the plural fix it is a development set and all 4 solve.
        Set 10 was written after the plural fix and the "each / apiece / per" rule and run once, untuned."""
        from fresh_word_problems_9 import FRESH as F9
        from fresh_word_problems_10 import FRESH as F10
        self.assertEqual(score(F9), (4, 0, 4))
        solved, declined, required = score(F10)
        print("  fresh wordings (tenth set, two purchases): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 0, 2))

    def test_price_blend_set(self):
        """Set 11: price-per-pound blend wordings written after the family and run once, untuned.  One answer is declined
        (a safe miss: "A 40 lb blend worth ... is made from ..." has no 'make / get / need' before the amount)."""
        from fresh_word_problems_11 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (eleventh set, price blends): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 1, 3))

    def test_savings_equal(self):
        self.assertEqual(answers("I have $200 and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same?"), values(15))
        self.assertEqual(answers("Elena has $160 saved and adds $20 each week. Ben has $360 saved and adds $10 each week. After how many weeks will they have the same amount?"), values(20))
        r = WS.solve("I have $200 and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same?")
        self.assertIn("200 + 15w = 350 + 5w", r.reading)
        self.assertIn("15 weeks (each will have $425)", r.reading)
        # one saver, equal rates, a negative or zero or fractional time, a question for an amount of money
        self.assertIsNone(answers("I have $200 and save $15 a week. When will I have $350?"))
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $350 and saves $15 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $100 and save $10 a week. My sister has $400 and saves $20 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $200 and saves $5 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $350 and saves $4 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $350 and saves $5 a week. How much will each have when we have the same?"))
        # a spelled number, "each / for each / apiece" after a starting amount, and the words that change the equation decline
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same? Assume two weeks of holiday."))
        self.assertIsNone(answers("I have $200 each and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $200 for each and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $200 apiece and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $200 and save $15 a week for part of the year. My sister has $350 and saves $5 a week. When will we have the same?"))
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $350 and saves $5 a week. Such savings! When will we have the same?"))
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $350 and saves $5 a week, but only half of the time. When will we have the same?"))

    def test_average_needed(self):
        self.assertEqual(answers("My test marks are 70, 85 and 90. What do I need on the fourth test to average 85?"), values(95))
        self.assertEqual(answers("Ava scored 87, 71, 73, 89, 97 on 5 tests. What score is needed on the next test to average 86?"), values(99))
        self.assertEqual(answers("Ava scored 70, 85 and 90 on three tests. What score does she need on the next test to average 85?"), values(95))
        r = WS.solve("My test marks are 70, 85 and 90. What do I need on the fourth test to average 85?")
        self.assertIn("(70 + 85 + 90 + x) / 4 = 85", r.reading)
        # a fraction stays exact: 4 * 85.5 - 245 = 97
        self.assertEqual(answers("My test marks are 70, 85 and 90. What do I need on the fourth test to average 85.5?"), values(97))
        self.assertEqual(answers("My test marks are 70, 85 and 91. What do I need on the fourth test to average 85.5?"), values(96))
        r = WS.solve("My test marks are 70, 85 and 91. What do I need on the fourth test to average 85.5?")
        self.assertIn("x = 96", r.reading)
        # a stated count or ordinal that does not match the scores, a spelled number that changes the answer
        self.assertIsNone(answers("My test marks are 70, 85 and 90 on 4 tests. What do I need on the next test to average 85?"))
        self.assertIsNone(answers("Ava scored 70, 85 and 90 on four tests. What score does she need on the next test to average 85?"))
        self.assertIsNone(answers("Ava scored 70, 85 and 90 on two tests. What score does she need on the next test to average 85?"))
        self.assertIsNone(answers("My test marks are 70, 85 and 90. What do I need on the fifth test to average 85?"))
        self.assertIsNone(answers("Ava scored 70, 85 and 90, and the last test is worth twice as much. What score does she need on the next test to average 85?"))
        # weighted averages, "drop the lowest", at least, a score no test can reach, a single score, a stated total, part of the year
        self.assertIsNone(answers("Ava scored 70, 85 and 90. What does she need on the next test to average 85 if the lowest is dropped?"))
        self.assertIsNone(answers("Ava scored 70, 85 and 90 and the final is worth 40%. What does she need on the final to average 85?"))
        self.assertIsNone(answers("Ava scored 70, 85 and 90. What does she need on the next test to average 85 at least?"))
        self.assertIsNone(answers("Ava scored 70 and 90. What does she need on the next test to average 100?"))
        self.assertIsNone(answers("Ava scored 70 on a test. What does she need on the next test to average 85?"))
        self.assertIsNone(answers("Ava scored 70, 85 and 90 for part of the year. What does she need on the next test to average 85?"))
        self.assertIsNone(answers("My average is 80 on 3 tests. My test marks are 70, 85 and 90. What do I need on the next test to average 85?"))

    def test_heads_and_feet(self):
        self.assertEqual(answers("30 heads and 84 feet. Hens and sheep. How many sheep?"), values(12, 18))
        self.assertEqual(answers("A farm has chickens and pigs. There are 48 heads and 138 legs. How many of each are there?"), values(21, 27))
        r = WS.solve("A farm has hens and sheep. There are 30 heads and 84 feet. How many of each are there?")
        self.assertEqual(r.values, [Fraction(18), Fraction(12)])
        self.assertIn("h + s = 30 and 2h + 4s = 84", r.reading)
        self.assertIn("h = 18 and s = 12", r.reading)
        # a third animal, people, insects, vehicles, a count that is not whole or not positive, a question that asks for legs
        self.assertIsNone(answers("A farm has hens, sheep and goats. There are 30 heads and 84 feet. How many sheep are there?"))
        self.assertIsNone(answers("A farm has hens and spiders. There are 30 heads and 84 legs. How many hens are there?"))
        self.assertIsNone(answers("A farm has farmers and sheep. There are 30 heads and 84 legs. How many sheep are there?"))
        self.assertIsNone(answers("A farm has bicycles and cars. There are 30 heads and 84 wheels. How many cars are there?"))
        self.assertIsNone(answers("A farm has hens and sheep. There are 30 heads and 85 legs. How many sheep are there?"))
        self.assertIsNone(answers("A farm has hens and sheep. There are 30 heads and 60 legs. How many sheep are there?"))
        self.assertIsNone(answers("A farm has hens and sheep. There are 30 heads and 84 legs. How many legs do the hens have?"))
        self.assertIsNone(answers("A farm has two kinds of animals, hens and sheep. There are 30 heads and 84 legs. How many sheep are there?"))
        self.assertIsNone(answers("A farm has hens and sheep. There are 30 heads and 84 legs, such that sheep are 4-legged. How many of each are there?"))
        self.assertIsNone(answers("A farm has hens and sheep. There are 30 heads and 84 legs for part of the year. How many of each are there?"))

    def test_three_families_set(self):
        """Set 12: wordings for savings_equal, average_needed and heads_and_feet, written after all three were finished and run once, untuned.
        Two answers are declined (safe misses): "brings my average up to 75" and "counting heads gives 20 and counting feet gives 56"."""
        from fresh_word_problems_12 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twelfth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 2, 7))

    def test_no_control_characters_in_the_python_files(self):
        """A backspace once got into a regular expression ("\\b" stored as a control character): every .py file here must be clean."""
        import glob
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        for path in glob.glob(os.path.join(here, "*.py")):
            with open(path, "rb") as f:
                data = f.read()
            bad = sorted({b for b in data if b < 32 and b not in (9, 10, 13)})
            self.assertEqual(bad, [], os.path.basename(path))

    def test_two_fixes_now_and_how_many_animals(self):
        # "as much as she has now" is the other saver's amount TODAY (200 + 15w = 350), not the time they are equal
        self.assertIsNone(answers("I have $200 and save $15 a week. My sister has $350 and saves $5 a week. When will I have as much as she has now?"))
        # "how many animals" is the number of heads: the question must name one of the two animals, or say "each"
        self.assertIsNone(answers("There are hens and sheep. 30 heads and 84 feet. How many animals are there?"))
        self.assertEqual(answers("There are hens and sheep. 30 heads and 84 feet. How many sheep?"), values(12, 18))
        self.assertEqual(answers("A yard has 25 heads and 70 legs among its geese and horses. How many horses are there?"), values(10, 15))
        self.assertEqual(answers("There are hens and sheep. 30 heads and 84 feet. How many of each are there?"), values(12, 18))

    def test_opposite_directions(self):
        self.assertEqual(answers("Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 km apart?"), values(3))
        self.assertEqual(answers("Omar and Lena leave the same town at the same time, driving in opposite directions at 30 mph and 36 mph. After how many hours will they be 165 miles apart?"), values(Fraction(5, 2)))
        r = WS.solve("Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 km apart?")
        self.assertIn("(50 + 70)t = 360", r.reading)
        r = WS.solve("Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. When are they 100 km apart?")
        self.assertEqual(r.values, [Fraction(5, 6)])                  # an exact fraction, never 0.8333
        self.assertIn("5/6 hours", r.reading)
        # the same direction, a head start, a question for a speed or a distance, mixed units, a third car, a spelled number that is not the count
        for text in ("Two cars leave the same spot in the same direction, one at 50 km/h and one at 70 km/h. When are they 360 km apart?",
                     "Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. How fast is the first if they are 360 km apart after 3 hours?",
                     "Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. One leaves an hour later. When are they 360 km apart?",
                     "Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 km apart, with a head start of 20 km?",
                     "Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. How far apart are they after 3 hours?",
                     "Three cars leave the same spot in opposite directions at 50 km/h and 70 km/h. When are they 360 km apart?",
                     "Two cars leave the same spot in opposite directions, one at 50 mph and one at 70 km/h. When are they 360 km apart?",
                     "Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 miles apart?",
                     "Two cars leave the same spot in opposite directions, twice at 50 km/h and one at 70 km/h. When are they 360 km apart?",
                     "Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 km apart for part of the year?",
                     "Two cars leave the same spot in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 km apart, such as half the time?"):
            self.assertIsNone(answers(text), text)

    def test_catch_up(self):
        self.assertEqual(answers("A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph. How long until the fast one catches it?"), values(4))
        self.assertEqual(answers("Caleb leaves at 39 mph. 2 hours later, Aiden follows the same route at 63 mph. How long after Aiden leaves will Aiden catch up?"), values(Fraction(13, 4)))
        self.assertEqual(answers("A slow train leaves at 40 mph. Three hours later a fast train follows at 60 mph. How long until the fast one catches it?"), values(6))
        r = WS.solve("A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph. How long until the fast one catches it?")
        self.assertIn("40(t + 2) = 60t", r.reading)
        self.assertIn("t = 4 hours", r.reading)
        r = WS.solve("Caleb leaves at 39 mph. 2 hours later, Aiden follows the same route at 63 mph. How long after Aiden leaves will Aiden catch up?")
        self.assertIn("13/4 hours", r.reading)                          # exact, not 3.25 rounded
        # the answer is the FOLLOWER's time: "after the slow train leaves" is a different question and declines; so does a distance
        self.assertEqual(answers("A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph. How many hours after the fast train leaves does the fast one catch it?"), values(4))
        for text in ("A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph. How many hours after the slow train leaves does the fast one catch it?",
                     "A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph. How far from the station does the fast one catch it?",
                     # the follower is not faster
                     "A slow train leaves at 60 mph. Two hours later a fast train follows at 40 mph. How long until the fast one catches it?",
                     "A slow train leaves at 40 mph. Two hours later a fast train follows at 40 mph. How long until the fast one catches it?",
                     # no head start, a spelled number that is not the head start, a stop, part of the way
                     "A slow train leaves at 40 mph. A fast train follows at 60 mph. How long until the fast one catches it?",
                     "A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph. How long until the fast one catches it? Half the time it stops.",
                     "A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph for part of the way. How long until the fast one catches it?",
                     "A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph and twice that speed after noon. How long until the fast one catches it?"):
            self.assertIsNone(answers(text), text)

    def test_polygon_angle_sum(self):
        self.assertEqual(answers("How many sides does a polygon have if its inside angles total 1440 degrees?"), values(10))
        self.assertEqual(answers("The interior angles of a polygon add up to 720°. How many sides does it have?"), values(6))
        r = WS.solve("The interior angles of a polygon add up to 720°. How many sides does it have?")
        self.assertIn("(n - 2) * 180 = 720", r.reading)
        self.assertIn("n = 6 sides", r.reading)
        # a regular polygon's one angle, an exterior angle, a sum that is not a multiple of 180, a result that is not above 2 sides, diagonals
        # (a regular polygon's one interior angle is a wording the word archive proved: polygon_angle_sum still declines it, archive_geometry_polygons_* answers it)
        regular = "Each interior angle of a regular polygon measures 150°. How many sides does the polygon have?"
        self.assertIsNone(WS.polygon_angle_sum(regular))
        self.assertEqual(answers(regular), values(12))
        exterior = "Each exterior angle of a regular polygon is 30°. How many sides does it have?"          # also a proven wording: 360 / n = 30
        self.assertIsNone(WS.polygon_angle_sum(exterior))
        self.assertEqual(answers(exterior), values(12))
        for text in ("The exterior angles of a polygon add up to 360°. How many sides does it have?",
                     "The interior angles of a polygon add up to 1450°. How many sides does it have?",
                     "The interior angles of a polygon add up to 0°. How many sides does it have?",
                     "The interior angles of a polygon add up to 90°. How many sides does it have?",
                     "The interior angles of a regular polygon add up to 1440°. How many sides does it have?",
                     "The interior angles of a polygon add up to 1440°. How many diagonals does it have?",
                     "The interior angles of a polygon add up to two thousand degrees. How many sides does it have?",
                     "The interior angles of a polygon add up to 1440° for part of the year. How many sides does it have?"):
            self.assertIsNone(answers(text), text)

    def test_distance_geometry_set(self):
        """Set 13: wordings for opposite_directions, catch_up and polygon_angle_sum, written after all three were finished and run once, untuned.
        One answer is declined (a safe miss): "until she is caught" has no 'catch / catches / overtake' word."""
        from fresh_word_problems_13 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirteenth set, distance and geometry): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 1, 9))

    def test_catch_up_the_later_vehicle_must_be_faster(self):
        # the 40 mph train is the one that leaves LATER and it is the slower one: it never catches the 60 mph train
        self.assertIsNone(answers("A train leaves at 40 mph. Two hours later it follows a 60 mph train that left earlier. How long until it catches up?"))
        self.assertIsNone(answers("A train leaves at 40 mph. Two hours later it follows the train that left at 60 mph. How long until it catches up?"))
        self.assertIsNone(answers("A train leaves at 40 mph. Two hours later it follows a 60 mph train. How long until it catches up?"))
        # the usual orders still answer
        self.assertEqual(answers("A slow train leaves at 40 mph. Two hours later a fast train follows at 60 mph. How long until the fast one catches it?"), values(4))
        self.assertEqual(answers("Sam leaves at 30 km/h. One hour later Ravi chases him at 45 km/h. How long until Ravi catches Sam?"), values(2))
        self.assertEqual(answers("Caleb leaves at 39 mph. 2 hours later, Aiden follows the same route at 63 mph. How long after Aiden leaves will Aiden catch up?"), values(Fraction(13, 4)))
        # a pronoun as the follower cannot say who leaves later: decline
        self.assertIsNone(answers("She leaves at 40 mph. Two hours later he follows at 60 mph. How long until he catches her?"))

    def test_toward_each_other(self):
        self.assertEqual(answers("Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. When do they meet?"), values(2))
        self.assertEqual(answers("Two trains start 142 miles apart and travel toward each other at 38 mph and 33 mph. When will they meet?"), values(2))
        self.assertEqual(answers("Two cyclists are 198 km apart and ride toward each other at 64 km/h and 35 km/h. How long until they meet?"), values(2))
        r = WS.solve("Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. When do they meet?")
        self.assertIn("(4 + 5)t = 18", r.reading)
        r = WS.solve("Two hikers start 10 km apart and walk toward each other at 4 km/h and 8 km/h. When do they meet?")
        self.assertEqual(r.values, [Fraction(5, 6)])
        self.assertIn("5/6 hours", r.reading)
        # a head start, a question for a distance, away from, mixed units, a third hiker, a spelled number that is not the count, a speed question
        for text in ("Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. How far from the start do they meet?",
                     "Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. One leaves an hour later. When do they meet?",
                     "Two hikers start 18 km apart and walk away from each other at 4 km/h and 5 km/h. When do they meet?",
                     "Two hikers start 18 km apart and walk toward each other at 4 mph and 5 km/h. When do they meet?",
                     "Two hikers start 18 km apart and walk toward each other at 4 km/h and twice that. When do they meet?",
                     "Three hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. When do they meet?",
                     "Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. How fast is each?",
                     "Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h for part of the day. When do they meet?",
                     "Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h, such as on half the days. When do they meet?"):
            self.assertIsNone(answers(text), text)
        # opposite directions still declines "toward" and "meet", and this family declines "opposite"
        self.assertIsNone(answers("Two hikers start 18 km apart and walk in opposite directions toward the same hill at 4 km/h and 5 km/h. When do they meet?"))

    def test_consecutive_product(self):
        self.assertEqual(answers("Two even numbers that come one after another multiply to 168. What are they?"), values(12, 14))
        self.assertEqual(answers("The product of two consecutive positive integers is 12. Find the integers."), values(3, 4))
        self.assertEqual(answers("The product of two consecutive odd numbers is 143. Find them."), values(11, 13))
        r = WS.solve("Two even numbers that come one after another multiply to 168. What are they?")
        self.assertIn("x(x + 2) = 168", r.reading)
        self.assertIn("-14 and -12 also multiplies to 168", r.reading)      # the negative pair is named, not hidden
        r = WS.solve("The product of two consecutive positive integers is 12. Find the integers.")
        self.assertNotIn("also multiplies", r.reading)                       # "positive" was said
        # not two whole numbers, the wrong kind, a sum, a negative pair, a third number, a decimal
        for text in ("Two even numbers that come one after another multiply to 170. What are they?",
                     "Two odd numbers that come one after another multiply to 168. What are they?",
                     "Two even numbers that come one after another multiply to 165. What are they?",
                     "Two numbers that come one after another multiply to 168. What are they?",
                     "The product of two consecutive integers is 100. Find the integers.",
                     "Two even numbers that come one after another multiply to 168. What is their sum?",
                     "Two even numbers that come one after another add to 168. What are they?",
                     "The sum of two consecutive even integers is 50 and their product is 624. Find the integers.",
                     "Two negative even numbers that come one after another multiply to 168. What are they?",
                     "Three even numbers that come one after another multiply to 168. What are they?",
                     "Two even numbers that come one after another multiply to 16.5. What are they?",
                     "Two even numbers that come one after another multiply to 168, such that one is large. What are they?"):
            self.assertIsNone(answers(text), text)

    def test_most_you_can_buy(self):
        self.assertEqual(answers("You have $45. A movie costs $9 per ticket. What is the greatest number of tickets you can buy?"), values(5))
        self.assertEqual(answers("You can spend no more than $60. Tickets cost $4 each and there is a $12 entry fee. What is the greatest number of tickets?"), values(12))
        self.assertEqual(answers("Hana has $157 to spend. There is a $25 entry fee, and T-shirts cost $12.00 each. What is the most T-shirts that can be bought?"), values(11))
        self.assertEqual(answers("You have $50. A movie costs $9 per ticket. How many tickets can you buy?"), values(5))
        r = WS.solve("You can spend no more than $60. Tickets cost $4 each and there is a $12 entry fee. What is the greatest number of tickets?")
        self.assertIn("4n + 12 <= 60", r.reading)
        self.assertIn("one more would cost $64, over $60", r.reading)      # one more ticket goes over the money
        # money left over, a discount, a total that is "each", too little money, the fee alone is too much, the least, part of the year,
        # a second per-item price, a spelled number, a percent
        for text in ("You have $45. A movie costs $9 per ticket. How much money is left after buying the most tickets?",
                     "You have $45. A movie costs $9 per ticket. What is the greatest number of tickets you can buy if there is a discount?",
                     "You have $45 each. A movie costs $9 per ticket. What is the greatest number of tickets you can buy?",
                     "You have $5. A movie costs $9 per ticket. What is the greatest number of tickets you can buy?",
                     "You have $45. A movie costs $9 per ticket and a $50 entry fee. What is the greatest number of tickets you can buy?",
                     "You have $45. A movie costs $9 per ticket. What is the least number of tickets you can buy?",
                     "You have $45 for part of the year. A movie costs $9 per ticket. What is the greatest number of tickets you can buy?",
                     "You have $45. A movie costs $9 per ticket and $3 for each snack. What is the greatest number of tickets you can buy?",
                     "You have $45. A movie costs $9 per ticket. What is the greatest number of tickets for two people?",
                     "You have $45. Tickets cost $9 each with a 10% discount for groups. What is the greatest number of tickets you can buy?"):
            self.assertIsNone(answers(text), text)

    def test_buy_consecutive_toward_set(self):
        """Set 14: wordings for toward_each_other, consecutive_product and most_you_can_buy, written after all three were finished and run once,
        untuned.  One answer is declined (a safe miss): "follow each other" is not one of the 'next to one another' phrases."""
        from fresh_word_problems_14 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (fourteenth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (8, 1, 7))

    def test_or_is_a_choice_not_a_fee(self):
        # "entry tickets at $12 OR snacks at $4": the snacks alone are 15 (4n <= 60); the $12 is not a fee that must be paid
        self.assertIsNone(answers("You have $60. You can buy entry tickets at $12 or snacks at $4 each. What is the greatest number of snacks you can buy?"))
        self.assertIsNone(answers("You have $60. You can buy tickets at $12 or snacks at $4 each. How many snacks can you afford?"))
        # "and there is a $12 entry fee" is a fee, and still answers
        self.assertEqual(answers("You can spend no more than $60. Tickets cost $4 each and there is a $12 entry fee. What is the greatest number of tickets?"), values(12))

    def test_still_water_current(self):
        self.assertEqual(answers("Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours. What is my rowing speed in still water?"), values(9))
        self.assertEqual(answers("Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours. How fast is the current?"), values(3))
        self.assertEqual(answers("A boat travels 34 km downstream in 2 hours and 35 km upstream in 5 hours. Find the speed of the boat in still water and the speed of the current."), values(5, 12))
        r = WS.solve("Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours. What is my rowing speed in still water?")
        self.assertEqual(r.values, [Fraction(9)])                       # only the one the question asks for
        self.assertIn("downstream speed = 12, upstream speed = 6", r.reading)
        self.assertIn("still water b = 9", r.reading)
        r = WS.solve("A boat goes 20 km upstream in 2 hours and 30 km downstream in 2 hours. What is the speed of the boat in still water?")
        self.assertEqual(r.values, [Fraction(25, 2)])                   # an exact fraction, and either order of the two legs
        self.assertIn("b = 25/2", r.reading)
        # equal speeds (no current), an upstream trip that is faster, mixed units, the speed against the current, a time, a spelled number
        for text in ("Rowing with the current I cover 24 km in 2 hours, but against it only 24 km in 2 hours. What is my rowing speed in still water?",
                     "Rowing with the current I cover 12 km in 2 hours, but against it 24 km in 2 hours. What is my rowing speed in still water?",
                     "Rowing with the current I cover 24 km in 2 hours, but against it only 12 miles in 2 hours. What is my rowing speed in still water?",
                     "Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours. What is my rowing speed against the current?",
                     "Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours. How long does the trip take?",
                     "Rowing with the current I cover 24 km in two hours, but against it only 12 km in 2 hours. What is my rowing speed in still water?",
                     "Rowing with the current I cover 24 km in 2 hours, and with the current again 12 km in 2 hours. What is my rowing speed in still water?",
                     "Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours. What is my rowing speed in still water, half the time?",
                     "Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours for part of the year. What is my rowing speed in still water?"):
            self.assertIsNone(answers(text), text)

    def test_ratio_split(self):
        self.assertEqual(answers("Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of water?"), values(6))
        self.assertEqual(answers("Water is mixed into concentrate in the ratio 5:1. How much water for 6 litres of concentrate?"), values(30))
        self.assertEqual(answers("A shade of green uses blue and yellow paint in the ratio 3:4. If 6 L of blue is used, how much yellow is needed?"), values(8))
        self.assertEqual(answers("The ratio of sand to cement is 3:1. If I use 24 kg of sand, how much cement do I need?"), values(8))
        r = WS.solve("Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of water?")
        self.assertIn("water : concentrate = 5 : 1", r.reading)
        r = WS.solve("A shade of green uses blue and yellow paint in the ratio 3:5. If 6 L of blue is used, how much yellow is needed?")
        self.assertEqual(r.values, [Fraction(10)])
        r = WS.solve("A shade of green uses blue and yellow paint in the ratio 4:3. If 6 L of blue is used, how much yellow is needed?")
        self.assertEqual(r.values, [Fraction(9, 2)])                    # exact, never 4.5 rounded
        self.assertIn("9/2 l", r.reading)
        # a ratio that is not two whole numbers, a question that does not name the missing substance, a total, a different substance, spelled numbers
        for text in ("Water is mixed into concentrate in the ratio 2.5:1. How much concentrate for 30 litres of water?",
                     "Water is mixed into concentrate in the ratio 5:0. How much concentrate for 30 litres of water?",
                     "Water is mixed into concentrate in the ratio 5:1. How much is needed for 30 litres of water?",
                     "Water is mixed into concentrate in the ratio 5:1. How much of each for 30 litres of water?",
                     "Water is mixed into concentrate in the ratio 5:1. How much water for 30 litres of water?",
                     "Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of oil?",
                     "Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of water in total?",
                     "Water is mixed into concentrate in the ratio 5:1 and then twice as much. How much concentrate for 30 litres of water?",
                     "Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of water if two bottles are used?",
                     "Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of water for part of the year?"):
            self.assertIsNone(answers(text), text)

    def test_three_numbers(self):
        self.assertEqual(answers("The sum of three numbers is 30. The first two add to 18 and the last two add to 20."), values(8, 10, 12))
        self.assertEqual(answers("The sum of three numbers is 30. The first two add to 18 and the last two add to 20. Find the numbers."), values(8, 10, 12))
        self.assertEqual(answers("The sum of three numbers is 30. The first and third add to 22 and the last two add to 20. What are the numbers?"), values(8, 10, 12))
        r = WS.solve("The sum of three numbers is 30. The first two add to 18 and the last two add to 20.")
        self.assertEqual(r.values, [Fraction(10), Fraction(8), Fraction(12)])           # in order: first, second, third
        self.assertIn("x + y + z = 30, x + y = 18, y + z = 20", r.reading)
        self.assertIn("x = 10, y = 8, z = 12", r.reading)
        r = WS.solve("The sum of three numbers is 31. The first two add to 18 and the last two add to 20.")
        self.assertEqual(r.values, [Fraction(11), Fraction(7), Fraction(13)])
        # a fourth number, a product, a question for something else, only one pair, the same pair twice, a spelled number
        for text in ("The sum of three numbers is 30. The first two add to 18 and the last two add to 20 and their product is 960.",
                     "The sum of three numbers is 30. The first two add to 18, the last two add to 20 and the first is 10.",
                     "The sum of three numbers is 30. The first two add to 18 and the last two add to 20. What is their product?",
                     "The sum of three numbers is 30. The first two add to 18 and the last two add to 20. What is the largest?",
                     "The sum of three numbers is 30. The first two add to 18. Find the numbers.",
                     "The sum of three numbers is 30. The first two add to 18 and the first two add to 18. Find the numbers.",
                     "The sum of four numbers is 30. The first two add to 18 and the last two add to 20.",
                     "The sum of three numbers is 30. The first two add to 18 and the last two add to 20, and one is twice another.",
                     "The sum of three numbers is 30. The first two add to 18 and the last two add to 20 for part of the year. Find the numbers."):
            self.assertIsNone(answers(text), text)

    def test_no_name_is_defined_twice_in_the_solver(self):
        """The 'still water' family once reused the names _UP and _DOWN that percent_change already used, and every percent problem was
        silently declined (22 generated claims became 0).  No module-level name may be assigned twice in word_solver.py."""
        import collections
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "word_solver.py"), encoding="utf-8") as f:
            text = f.read()
        names = re.findall(r"^([A-Za-z_]\w*)\s*=", text, flags=re.M) + re.findall(r"^def ([A-Za-z_]\w*)\(", text, flags=re.M)
        twice = sorted(n for n, c in collections.Counter(names).items() if c > 1)
        self.assertEqual(twice, [])

    def test_boat_ratio_numbers_set(self):
        """Set 15: wordings for still_water_current, ratio_split and three_numbers, written after all three were finished and run once, untuned.
        One answer is declined (a safe miss): "goes 45 miles with the current in 3 hours" has words between the distance and "in 3 hours"."""
        from fresh_word_problems_15 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (fifteenth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (7, 1, 7))

    def test_hour_abbreviation_h(self):
        # a lone "h" after the time is hours; "2 hours" and "2 hr" stay answered; "h" never matches inside another word
        self.assertEqual(answers("Rowing with the current I cover 24 km in 2 h, but against it only 12 km in 2 h. What's my rowing speed in still water?"), values(9))
        self.assertEqual(answers("Rowing with the current I cover 24 km in 2 hours, but against it only 12 km in 2 hours. What is my rowing speed in still water?"), values(9))
        self.assertEqual(answers("Rowing with the current I cover 24 km in 2 hr, but against it only 12 km in 2 hr. What is my rowing speed in still water?"), values(9))
        self.assertEqual(answers("Rowing with the current I cover 24 km in 2h, but against it only 12 km in 2h. What is my rowing speed in still water?"), values(9))
        self.assertIsNone(answers("Rowing with the current I cover 24 km in 2 hat, but against it only 12 km in 2 h. What is my rowing speed in still water?"))
        self.assertIsNone(answers("Rowing with the current I cover 24 km in 2 hm, but against it only 12 km in 2 h. What is my rowing speed in still water?"))
        self.assertIsNone(answers("Rowing with the current I cover 24 km in 2 min, but against it only 12 km in 2 h. What is my rowing speed in still water?"))

    def test_catch_up_clock(self):
        self.assertEqual(answers("A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph. When does the car catch the cyclist?"), values(1))
        self.assertEqual(answers("A cyclist leaves at 1 pm going 12 mph. A car leaves the same place at 4 pm going 36 mph. When does the car catch the cyclist?"), values(Fraction(3, 2)))
        # the order of the two sentences does not matter: the later departure is the follower
        self.assertEqual(answers("A car leaves the same place at 2 pm going 36 mph. A cyclist leaves at noon going 12 mph. When does the car catch the cyclist?"), values(1))
        r = WS.solve("A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph. When does the car catch the cyclist?")
        self.assertIn("12(t + 2) = 36t", r.reading)
        self.assertIn("t = 1 hour (3 hours after noon)", r.reading)
        r = WS.solve("A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 30 mph. When does the car catch the cyclist?")
        self.assertEqual(r.values, [Fraction(4, 3)])                    # 24 / 18, exact
        self.assertIn("4/3 hours", r.reading)
        # the later vehicle is not faster (slower or equal), the question names the earlier vehicle, minutes, half past, am, the same time,
        # a question for a distance or with only "it", a stop, part of the way
        for text in ("A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 6 mph. When does the car catch the cyclist?",
                     "A cyclist leaves at noon going 36 mph. A car leaves the same place at 2 pm going 12 mph. When does the car catch the cyclist?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 12 mph. When does the car catch the cyclist?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph. When does the cyclist catch the car?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2:30 pm going 36 mph. When does the car catch the cyclist?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at half past two going 36 mph. When does the car catch the cyclist?",
                     "A cyclist leaves at 9 am going 12 mph. A car leaves the same place at noon going 36 mph. When does the car catch the cyclist?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at noon going 36 mph. When does the car catch the cyclist?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph. How far from the start does the car catch the cyclist?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph. When does it catch up?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph and stops for lunch. When does the car catch the cyclist?",
                     "A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph for part of the way. When does the car catch the cyclist?"):
            self.assertIsNone(answers(text), text)

    def test_periodic_growth(self):
        self.assertEqual(answers("A yeast culture triples every 2 hours, starting at 10 cells. When does it reach 810?"), values(8))
        self.assertEqual(answers("A bacteria colony doubles every 3 hours. Starting at 500 cells, when will there be 8000?"), values(12))
        self.assertEqual(answers("A radioactive sample halves every 5 years. When does 160 g become 20 g?"), values(15))
        self.assertEqual(answers("Doubles every 3 hours from 500 to 8000. How long?"), values(12))
        self.assertEqual(answers("A bacteria culture starts with 1000 cells and doubles every 20 minutes. When will it reach 4,000 cells?"), values(40))
        self.assertEqual(answers("A substance has a half-life of 2 years. How long until 200 g decays to 25 g?"), values(6))
        self.assertEqual(answers("A culture doubles every two hours, starting at 10 cells. When does it reach 160?"), values(8))      # a spelled period is a count the equation uses
        r = WS.solve("A yeast culture triples every 2 hours, starting at 10 cells. When does it reach 810?")
        self.assertIn("810 / 10 = 81 = 3^4", r.reading)
        self.assertIn("4 periods of 2 hours: t = 8 hours", r.reading)
        r = WS.solve("A culture doubles every 1.5 hours, starting at 10 cells. When does it reach 80?")
        self.assertEqual(r.values, [Fraction(9, 2)])                    # an exact fraction: 3 periods of 3/2
        self.assertIn("9/2 hours", r.reading)
        # a ratio that is not an exact power, the wrong direction, a different unit asked, two kinds, a question for an amount, a spelled other number
        for text in ("A yeast culture triples every 2 hours, starting at 10 cells. When does it reach 800?",
                     "A yeast culture triples every 2 hours, starting at 10 cells. When does it reach 10?",
                     "A yeast culture triples every 2 hours, starting at 10 cells. When does it reach 5?",
                     "A culture doubles every 3 hours, starting at 10 cells. When does it reach 100?",
                     "Halves every 5 years from 20 g to 160 g. How long?",
                     "A yeast culture triples every 2 hours, starting at 10 cells. When does it reach 810 cells, in minutes?",
                     "A culture triples every 2 hours and doubles every 3 hours. When does it reach 810 from 10?",
                     "A yeast culture triples every 2 hours, starting at 10 cells. How many cells after 8 hours?",
                     "A culture quadruples every 2 hours, starting at 10 cells. When does it reach 160?",
                     "A culture doubles every 3 hours from 500 to 8000 and then triples. When does it reach that?",
                     "A culture doubles every 3 hours from 500 to 4000, for part of the time. How long?",
                     "A culture doubles every 3 hours from 500 to 4000, such as twice. How long?",
                     "A culture doubles every 3 hours from 500 to 8000 percent. How long?",
                     "A culture doubles every 3 hours from 500 to 4000 with three dishes. How long?"):
            self.assertIsNone(answers(text), text)

    def test_clock_and_growth_set(self):
        """Set 16: wordings for the hour abbreviation, catch_up_clock and periodic_growth, written after everything was finished and run once, untuned."""
        from fresh_word_problems_16 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (sixteenth set, h / clock / growth): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (8, 0, 7))

    def test_fixed_plus_rate(self):
        self.assertEqual(answers("A venue charges $100 plus $15 per guest. The total was $865. How many guests came?"), values(51))
        self.assertEqual(answers("A taxi charges $3 plus $2 per mile, the ride cost $19. How many miles was the ride?"), values(8))
        self.assertEqual(answers("A taxi charges $3.50 plus $1.50 per mile. A ride costs $39.50. How many miles was the ride?"), values(24))
        self.assertEqual(answers("A gym charges a $20 joining fee and $15 per month. Ana has paid $155 in total. How many months has Ana been a member?"), values(9))
        self.assertEqual(answers("A plumber charges a $60 call-out fee plus $45 per hour. The bill was $150. How long did the job take?"), values(2))
        r = WS.solve("A venue charges $100 plus $15 per guest. The total was $865. How many guests came?")
        self.assertIn("100 + 15n = 865", r.reading)
        self.assertIn("n = 51 guests", r.reading)
        # a continuous unit may be a fraction, exactly: 80 / 45 hours
        r = WS.solve("A plumber charges a $60 call-out fee plus $45 per hour. The bill was $140. How long did the job take?")
        self.assertEqual(r.values, [Fraction(16, 9)])
        self.assertIn("16/9 hours", r.reading)
        # a question for the total or a price, a count that is not whole, not positive, a total below the fixed cost, "each" after a total or the fixed cost,
        # a discount, a different unit asked, a spelled number, part of the year, a first-hour or additional-hour rule
        for text in ("A venue charges $100 plus $15 per guest. The total was $865. What was the total for 10 guests?",
                     "A venue charges $100 plus $15 per guest. The total was $865. What is the total cost?",
                     "A venue charges $100 plus $15 per guest. The total was $865. How much per guest?",
                     "A venue charges $100 plus $15 per guest. The total was $860. How many guests came?",
                     "A venue charges $100 plus $15 per guest. The total was $50. How many guests came?",
                     "A venue charges $100 plus $15 per guest. The total was $100. How many guests came?",
                     "A venue charges $100 plus $15 per guest. The total was $865 each. How many guests came?",
                     "A venue charges $100 each plus $15 per guest. The total was $865. How many guests came?",
                     "A venue charges $100 plus $15 per guest. The total was $865, with a 10% discount. How many guests came?",
                     "A venue charges $100 plus $15 per guest for part of the year. The total was $865. How many guests came?",
                     "A venue charges $100 plus $15 per guest. The total was $865. How many tickets were sold?",
                     "A venue charges $100 plus twice $15 per guest. The total was $865. How many guests came?"):
            self.assertIsNone(answers(text), text)
        # a first-hour rule is a wording the word archive proved: fixed_plus_rate still declines it, an archive family answers it (5 + 2 (h - 1) = 13, so 5 hours)
        parking = "A parking garage charges $5 for the first hour and $2 for each additional hour. A driver paid $13. How many hours did they park?"
        self.assertIsNone(WS.fixed_plus_rate(parking))
        self.assertEqual(answers(parking), values(5))

    def test_two_changing_equal(self):
        self.assertEqual(answers("Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and shrinks by 500 a year. In how many years are they equal?"), values(18))
        self.assertEqual(answers("Town A has 18,000 people and grows by 2000 a year. Town B has 63,000 people and shrinks by 500 a year. In how many years will they be equal?"), values(18))
        self.assertEqual(answers("Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and grows by 500 a year. In how many years are they equal?"), values(30))
        r = WS.solve("Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and shrinks by 500 a year. In how many years are they equal?")
        self.assertIn("18000 + 2000 t = 63000 - 500 t", r.reading)
        self.assertIn("t = 18 years", r.reading)
        # a negative time, equal changes, a time that is not whole, mixed units, a population asked for, a percent, a spelled number, part of the time
        for text in ("Town A has 63,000 people and grows by 2,000 a year. Town B has 18,000 and shrinks by 500 a year. In how many years are they equal?",
                     "Town A has 18,000 people and grows by 500 a year. Town B has 63,000 and grows by 500 a year. In how many years are they equal?",
                     "Town A has 18,000 people and grows by 2,000 a year. Town B has 63,001 and shrinks by 500 a year. In how many years are they equal?",
                     "Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and shrinks by 500 a month. In how many years are they equal?",
                     "Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and shrinks by 500 a year. What will the population be when they are equal?",
                     "Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and shrinks by 500 a year. How many people will each have when they are equal?",
                     "Town A has 18,000 people and grows by 2% a year. Town B has 63,000 and shrinks by 500 a year. In how many years are they equal?",
                     "Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and shrinks by twice 500 a year. In how many years are they equal?",
                     "Town A has 18,000 people and grows by 2,000 a year. Town B has 63,000 and shrinks by 500 a year for part of the time. In how many years are they equal?"):
            self.assertIsNone(answers(text), text)

    def test_add_to_blend(self):
        self.assertEqual(answers("How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $9 a pound?"), values(14))
        self.assertEqual(answers("How many pounds of coffee worth $10/lb must be added to 14 lb of coffee worth $8/lb to make a mix worth $9/lb?"), values(14))
        r = WS.solve("How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $9 a pound?")
        self.assertIn("8(14) + 10x = 9(14 + x)", r.reading)
        self.assertIn("x = 14 lb", r.reading)
        r = WS.solve("How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $9.50 a pound?")
        self.assertEqual(r.values, [Fraction(42)])                       # 14 * 1.5 / 0.5
        r = WS.solve("How many pounds of coffee worth $10 a pound must be added to 7 lb of coffee worth $8 a pound to make a mix worth $8.50 a pound?")
        self.assertEqual(r.values, [Fraction(7, 3)])                     # an exact fraction
        self.assertIn("7/3 lb", r.reading)
        # the price blend of two coffees to a total weight stays on the price_blend family
        self.assertEqual(WS.solve("How many pounds of coffee at $6 per pound must be mixed with coffee at $10 per pound to make 40 lb worth $7 per pound?").family, "price_blend")
        # a blend price not strictly between the two, equal prices, different units, water, a spelled number (found by fresh set 17), part of the year
        for text in ("How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $12 a pound?",
                     "How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $10 a pound?",
                     "How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $7 a pound?",
                     "How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $10 a pound to make a mix worth $9 a pound?",
                     "How many pounds of coffee worth $10 a pound must be added to 14 kg of coffee worth $8 a pound to make a mix worth $9 a pound?",
                     "How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $9 a pound, with water?",
                     "How many pounds of tea at $5 a pound must be added to 6 lb of tea at $9 a pound to make a blend priced at $7 a pound if two pounds spill?",
                     "How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee worth $8 a pound to make a mix worth $9 a pound for part of the year?"):
            self.assertIsNone(answers(text), text)

    def test_fixed_changing_blend_sets(self):
        """Fresh set 17 (14 wordings, written after the three families were finished, run once, untuned) found one WRONG answer: "... if two pounds spill"
        was answered 6 because add_to_blend did not decline a spelled "two".  That is fixed (every spelled number now declines there), so set 17 is a
        development set: 6 solved, 1 declined (safe), 6 of 6 required declines.  Set 18 (9 wordings) was written after that fix and run once, untuned."""
        from fresh_word_problems_17 import FRESH as F17
        from fresh_word_problems_18 import FRESH as F18
        s17, s18 = score(F17), score(F18)
        print("  development wordings (seventeenth set, found one wrong answer, now fixed): %d solved, %d declined, %d required declines correct" % s17)
        print("  fresh wordings (eighteenth set, written after the fix): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (s18[0], s18[0] + s18[1], s18[1], s18[2], s18[2]))
        self.assertEqual(s17, (6, 1, 7))
        # (3, 3, 3) when written; "Plant A is 30 cm tall and grows 4 cm a week ..." was a safe miss and is now solved (20 weeks) by the measured-things statement: (4, 2, 3)
        self.assertEqual(s18, (4, 2, 3))

    def test_two_scores(self):
        self.assertEqual(answers("A basketball team scored 92 points from 40 field goals, all 2-pointers and 3-pointers. How many of each?"), values(12, 28))
        self.assertEqual(answers("A basketball team scored 92 points from 40 field goals, all two-pointers and three-pointers. How many of each?"), values(12, 28))
        self.assertEqual(answers("A football team scored 48 points from 8 scores, all 7-point touchdowns (with extra point) and 3-point field goals. How many of each?"), values(2, 6))
        r = WS.solve("A basketball team scored 92 points from 40 field goals, all 2-pointers and 3-pointers. How many of each?")
        self.assertEqual(r.values, [Fraction(28), Fraction(12)])           # twos first, then threes
        self.assertIn("x + y = 40 and 2x + 3y = 92", r.reading)
        self.assertIn("x = 28 and y = 12", r.reading)
        # a third point value, free throws, equal values, not whole or not positive counts, no "all", a spelled number, part of the season, a question for something else
        for text in ("A basketball team scored 92 points from 40 field goals, all 2-pointers, 3-pointers and free throws. How many of each?",
                     "A basketball team scored 92 points from 40 field goals, all 1-pointers, 2-pointers and 3-pointers. How many of each?",
                     "A basketball team scored 92 points from 40 field goals, all 2-pointers and 2-pointers. How many of each?",
                     "A basketball team scored 80 points from 40 field goals, all 2-pointers and 3-pointers. How many of each?",
                     "A basketball team scored 70 points from 40 field goals, all 2-pointers and 3-pointers. How many of each?",
                     "A team scored 50 points from 8 scores, all 7-point touchdowns and 3-point field goals. How many of each?",
                     "A basketball team scored 92 points from 40 field goals, 2-pointers and 3-pointers. How many of each?",
                     "A basketball team scored twice 92 points from 40 field goals, all 2-pointers and 3-pointers. How many of each?",
                     "A basketball team scored 92 points from 40 field goals, all 2-pointers and 3-pointers, for part of the season. How many of each?",
                     "A basketball team scored 92 points from 40 field goals, all 2-pointers and 3-pointers. How many points per shot?"):
            self.assertIsNone(answers(text), text)

    def test_two_discounts(self):
        self.assertEqual(answers("A coat is marked 40% off, and then an extra 10% is taken off the sale price. The final price is $464.40. What was the original price?"), values(860))
        self.assertEqual(answers("A jacket is 30% off. Then a coupon takes an extra 20% off the discounted price. It now costs $168. What was the original price?"), values(300))
        r = WS.solve("A coat is marked 40% off, and then an extra 10% is taken off the sale price. The final price is $464.40. What was the original price?")
        self.assertIn("0.6 x 0.9 x p = 464.4", r.reading)
        # the answer stays exact: a price that is not a whole number of cents is an exact fraction, never a rounded decimal
        r = WS.solve("A coat is marked 40% off, and then an extra 10% is taken off the sale price. The final price is $464.41. What was the original price?")
        self.assertEqual(r.values, [Fraction(46441, 54)])
        self.assertIn("46441/54", r.reading)
        # both cuts off the ORIGINAL price (an additive 50%, a different equation), no "sale price", a question for the savings, tax, a total, a percent over 100,
        # a spelled number, part of the year
        for text in ("A coat is marked 40% off, and then an extra 10% is taken off the original price. The final price is $464.40. What was the original price?",
                     "A coat is marked 40% off and an extra 10% is taken off. The final price is $464.40. What was the original price?",
                     "A coat is marked 40% off, and then an extra 10% is taken off the sale price. The final price is $464.40. How much did you save?",
                     "A coat is marked 40% off, and then an extra 10% is taken off the sale price, plus 5% tax. The final price is $464.40. What was the original price?",
                     "A coat is marked 40% off, and then an extra 10% is taken off the sale price. Both cuts together give a final price of $464.40. What was the original price?",
                     "A coat is marked 140% off, and then an extra 10% is taken off the sale price. The final price is $464.40. What was the original price?",
                     "A coat is marked 40% off, and then an extra 10% is taken off the sale price. The final price is $464.40. What was the original price of two coats?",
                     "A coat is marked 40% off, and then an extra 10% is taken off the sale price for part of the year. The final price is $464.40. What was the original price?"):
            self.assertIsNone(answers(text), text)

    def test_triangle_ratio(self):
        self.assertEqual(answers("The angles of a triangle are in the ratio 3:5:7. Find each angle."), values(36, 60, 84))
        self.assertEqual(answers("The angles of a triangle are in the ratio 2:3:4. What are the angles?"), values(40, 60, 80))
        r = WS.solve("The angles of a triangle are in the ratio 3:5:7. Find each angle.")
        self.assertEqual(r.values, [Fraction(36), Fraction(60), Fraction(84)])
        self.assertEqual(sum(r.values), 180)                                # the three angles always add to 180
        self.assertIn("15 parts in all, so one part is 180/15 = 12", r.reading)
        r = WS.solve("The angles of a triangle are in the ratio 1:1:5. Find each angle.")
        self.assertEqual(r.values, [Fraction(180, 7), Fraction(180, 7), Fraction(900, 7)])     # exact fractions
        self.assertEqual(sum(r.values), 180)
        # two parts, four parts, a decimal or zero part, only the largest, a right triangle, another number, spelled parts, part of the time
        for text in ("The angles of a triangle are in the ratio 3:5. Find each angle.",
                     "The angles of a triangle are in the ratio 3:5:7:9. Find each angle.",
                     "The angles of a triangle are in the ratio 2.5:3:4. Find each angle.",
                     "The angles of a triangle are in the ratio 3:5:0. Find each angle.",
                     "The angles of a triangle are in the ratio 3:5:7. Find the largest angle.",
                     "The angles of a right triangle are in the ratio 3:5:7. Find each angle.",
                     "The angles of a triangle are in the ratio 3:5:7 and one side is 12 cm. Find each angle.",
                     "The angles of a triangle are in the ratio three to five to seven. Find each angle.",
                     "The angles of a triangle are in the ratio 3:5:7 for part of the time. Find each angle."):
            self.assertIsNone(answers(text), text)

    def test_scores_discounts_triangles_set(self):
        """Set 19: wordings for two_scores, two_discounts and triangle_ratio, written after all three were finished and run once, untuned.
        One answer is declined (a safe miss): "In a triangle the three angles are in the ratio ..." is not one of the angles-of-a-triangle phrases."""
        from fresh_word_problems_19 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (nineteenth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 1, 7))

    def test_scores_count_is_introduced_by_from(self):
        # "from 40 field goals" is the number of scores; "in 40 games" and "on 40 ..." are not (the 40 could be games, not baskets)
        self.assertEqual(answers("A team scored 92 points from 40 field goals, all 2-pointers and 3-pointers. How many of each?"), values(12, 28))
        self.assertIsNone(answers("A team scored 92 points in 40 games, all 2-pointers and 3-pointers. How many of each?"))
        self.assertIsNone(answers("A team scored 92 points on 40 field goals, all 2-pointers and 3-pointers. How many of each?"))
        self.assertIsNone(answers("A team scored 92 points with 40 field goals, all 2-pointers and 3-pointers. How many of each?"))

    def test_two_prices_known_count(self):
        self.assertEqual(answers("Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65. How many of each?"), values(9, 21))
        self.assertEqual(answers("Yara works two jobs paying $16/h and $22/h. Last month 61 hours were worked in total, earning $1156. How many hours were worked at the $16 job?"), values(30, 31))
        self.assertEqual(answers("Yara works at $16 an hour and $22 an hour for 61 hours, earning $1,156. How many hours at each rate?"), values(30, 31))
        r = WS.solve("Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65. How many of each?")
        self.assertEqual(r.values, [Fraction(9), Fraction(21)])
        self.assertIn("0.55x + 0.7y = 19.65", r.reading)                   # cents became dollars before meeting the dollar total
        self.assertIn("a price in cents is divided by 100", r.reading)
        r = WS.solve("Yara works at $16 an hour and $22 an hour for 61 hours, earning $1,156. How many hours at each rate?")
        self.assertIn("16x + 22y = 1156", r.reading)
        self.assertNotIn("cents", r.reading)
        # a third price, equal prices, a total that is "each", counts that are not whole or not positive, a question for money, a percent / tax,
        # a spelled number, part of the year, a fractional number of hours
        for text in ("Noah bought 30 stamps, some at 55¢, some at 70¢ and some at 90¢, for $19.65. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and some at 55¢, for $19.65. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65 each. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.00. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and some at 70¢, for $10. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65. How much did the 55¢ ones cost?",
                     "Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65 plus 5% tax. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and some at 70¢, for $1965. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and twice as many at 70¢, for $19.65. How many of each?",
                     "Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65 for part of the year. How many of each?",
                     "Yara works at $16 an hour and $22 an hour for 61.5 hours, earning $1,156. How many hours at each rate?",
                     "Yara works at $16 an hour and $22 an hour and $30 an hour for 61 hours, earning $1,156. How many hours at each rate?"):
            self.assertIsNone(answers(text), text)

    def test_drain_or_fill(self):
        self.assertEqual(answers("A pool holds 9,300 L and drains at 50 L per minute. After how many minutes will 500 L remain?"), values(176))
        self.assertEqual(answers("A tank holds 500 L and fills at 25 L per minute. After how many minutes will it hold 2,000 L?"), values(60))
        r = WS.solve("A pool holds 9,300 L and drains at 50 L per minute. After how many minutes will 500 L remain?")
        self.assertIn("9300 - 50t = 500", r.reading)
        self.assertIn("t = 176 minutes", r.reading)
        r = WS.solve("A tank holds 500 L and fills at 25 L per minute. After how many minutes will it hold 2,000 L?")
        self.assertIn("500 + 25t = 2000", r.reading)                       # filling uses a plus
        r = WS.solve("A pool holds 1,000 L and drains at 300 L per minute. After how many minutes will 100 L remain?")
        self.assertEqual(r.values, [Fraction(3)])
        r = WS.solve("A pool holds 1,000 L and drains at 300 L per minute. After how many minutes will 400 L remain?")
        self.assertEqual(r.values, [Fraction(2)])
        r = WS.solve("A pool holds 1,000 L and drains at 300 L per minute. After how many minutes will 150 L remain?")
        self.assertEqual(r.values, [Fraction(17, 6)])                      # an exact fraction of a minute
        # a mark that is above the start when draining or below it when filling (negative time), a question for the amount, another time unit,
        # another volume unit, two rates, a spelled number, part of the day, "empty"
        for text in ("A pool holds 9,300 L and drains at 50 L per minute. After how many minutes will 9,500 L remain?",
                     "A tank holds 500 L and fills at 25 L per minute. After how many minutes will it hold 100 L?",
                     "A pool holds 9,300 L and drains at 50 L per minute. How many liters remain after 10 minutes?",
                     "A pool holds 9,300 L and drains at 50 L per minute. After how many hours will 500 L remain?",
                     "A pool holds 9,300 L and drains at 50 gallons per minute. After how many minutes will 500 L remain?",
                     "A pool holds 9,300 L and drains at 50 L per minute while a pump fills 20 L per minute. After how many minutes will 500 L remain?",
                     "A pool holds 9,300 L and drains at 50 L per minute. After how many minutes will half remain?",
                     "A pool holds 9,300 L and drains at 50 L per minute. After how many minutes will it be empty?",
                     "A pool holds 9,300 L and drains at 50 L per minute. After how many minutes will 500 L remain for part of the day?"):
            self.assertIsNone(answers(text), text)

    def test_percent_of_count(self):
        self.assertEqual(answers("A test has 20 questions. Jamal scored 65%. How many questions were answered correctly?"), values(13))
        self.assertEqual(answers("A test has 40 questions. Pablo scored 95%. How many questions were answered correctly?"), values(38))
        r = WS.solve("A test has 20 questions. Jamal scored 65%. How many questions were answered correctly?")
        self.assertIn("20 x 65/100", r.reading)
        self.assertIn("13 answered correctly", r.reading)
        # a result that is not a whole number, a percent of a percent, a question for the percent or for the wrong ones, a spelled number,
        # a second percent, part of the year, a percent over 100
        for text in ("A test has 25 questions. Jamal scored 65%. How many questions were answered correctly?",
                     "A test has 20 questions. Jamal scored 65% of 80%. How many questions were answered correctly?",
                     "A test has 20 questions. Jamal scored 65%. What percent were answered correctly?",
                     "A test has 20 questions. Jamal scored 65%. How many questions were answered incorrectly?",
                     "A test has twenty questions. Jamal scored 65%. How many questions were answered correctly?",
                     "A test has 20 questions. Jamal scored 65% and then 10% more. How many questions were answered correctly?",
                     "A test has 20 questions. Jamal scored 65% for part of the year. How many questions were answered correctly?",
                     "A test has 20 questions. Jamal scored 130%. How many questions were answered correctly?",
                     "A test has 20 questions. Jamal scored 65%. How many questions were answered correctly in two tests?"):
            self.assertIsNone(answers(text), text)

    def test_prices_drain_percent_set(self):
        """Set 20: wordings for two_prices_known_count, drain_or_fill and percent_of_count, written after all three were finished and run once, untuned."""
        from fresh_word_problems_20 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twentieth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (6, 0, 7))

    def test_percent_of_count_needs_a_score(self):
        # "65% of the students passed" is a percent of the STUDENTS, not a score on the questions
        self.assertIsNone(answers("A test has 20 questions. 65% of the students passed. How many questions were answered correctly?"))
        self.assertIsNone(answers("A test has 20 questions. 65% of them were hard. How many questions were answered correctly?"))
        self.assertEqual(answers("A test has 20 questions. Jamal scored 65%. How many questions were answered correctly?"), values(13))
        self.assertEqual(answers("A test has 20 questions. Jamal got 65%. How many questions were answered correctly?"), values(13))
        self.assertEqual(answers("A test has 20 questions. Jamal earned 65%. How many questions were answered correctly?"), values(13))

    def test_percent_change_between(self):
        self.assertEqual(answers("A town's population changed from 2,500 to 4,000. What was the percent change?"), values(60))
        self.assertEqual(answers("A town's population changed from 2000 to 1200. What was the percent change?"), values(-40))     # a fall is negative
        self.assertEqual(answers("A price went from $20 to $23. What is the percent change?"), values(15))
        r = WS.solve("A town's population changed from 2,500 to 4,000. What was the percent change?")
        self.assertIn("(4000 - 2500) / 2500 x 100 = 60 percent", r.reading)
        r = WS.solve("A price went from $30 to $31. By what percent did it change?")
        self.assertEqual(r.values, [Fraction(10, 3)])                     # exact, never 3.3333
        self.assertIn("10/3 percent", r.reading)
        # the new amount asked for, a starting amount of zero, no change, "increase" / "decrease" worded, a percent in the problem, another number, a spelled number, per year
        for text in ("A town's population changed from 2,500 to 4,000. What is the new population?",
                     "A town's population changed from 0 to 4,000. What was the percent change?",
                     "A town's population changed from 2,500 to 2,500. What was the percent change?",
                     "A town's population changed from 2,500 to 4,000. What was the percent increase?",
                     "A town's population changed from 25% to 40%. What was the percent change?",
                     "A town's population changed from 2,500 to 4,000 in 5 years. What was the percent change?",
                     "A town's population changed from two thousand to 4,000. What was the percent change?",
                     "A town's population changed from 2,500 to 4,000. What was the percent change per year?",
                     "A town's population changed from 2,500 to 4,000 for part of the year. What was the percent change?"):
            self.assertIsNone(answers(text), text)

    def test_ages_later_multiple(self):
        self.assertEqual(answers("Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is each now?"), values(15, 75))
        self.assertEqual(answers("Kira is 4 times as old as Ava. In 8 years, Kira will be 2 times as old as Ava. How old is each now?"), values(4, 16))
        r = WS.solve("Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is each now?")
        self.assertEqual(r.values, [Fraction(75), Fraction(15)])
        self.assertIn("j = 5e;  j + 5 = 4(e + 5)", r.reading)
        self.assertIn("e = 15 and j = 75", r.reading)
        # equal multiples, an age that is not whole or not positive, "years ago", a third person, the roles swapped, twice, an extra number, a question for someone else
        for text in ("Jade is 5 times as old as Emeka. In 5 years, Jade will be 5 times as old as Emeka. How old is each now?",
                     "Jade is 5 times as old as Emeka. In 5 years, Jade will be 6 times as old as Emeka. How old is each now?",
                     "Jade is 5 times as old as Emeka. In 5 years, Jade will be 1 times as old as Emeka. How old is each now?",
                     "Jade is 5 times as old as Emeka. 5 years ago, Jade was 4 times as old as Emeka. How old is each now?",
                     "Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka, and Sam is 3 times as old as Jade. How old is each now?",
                     "Jade is 5 times as old as Emeka. In 5 years, Emeka will be 4 times as old as Jade. How old is each now?",
                     "Jade is twice as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is each now?",
                     "Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is each now? Their mother is 40.",
                     "Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is Jade's sister?",
                     "Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka for part of the year. How old is each now?"):
            self.assertIsNone(answers(text), text)

    def test_shared_fixed_cost(self):
        self.assertEqual(answers("A field trip costs $350 for the bus plus $15 admission per student. Each student pays $32.50 in total. How many students?"), values(20))
        self.assertEqual(answers("A field trip costs $350 for the bus plus $15 admission per student. The bus cost is shared equally, and each student pays $32.50 in total. How many students went?"), values(20))
        r = WS.solve("A field trip costs $350 for the bus plus $15 admission per student. Each student pays $32.50 in total. How many students?")
        self.assertIn("350/n + 15 = 32.5", r.reading)
        self.assertIn("n = 350 / 35/2 = 20", r.reading)                    # exact: 32.5 - 15 = 35/2
        # a question for the cost per student, each pays only the admission or less, a count that is not whole, another unit asked, tax,
        # "each" after the bus cost, part of the year, an extra person
        for text in ("A field trip costs $350 for the bus plus $15 admission per student. Each student pays $32.50 in total. How much does the bus cost per student?",
                     "A field trip costs $350 for the bus plus $15 admission per student. Each student pays $15 in total. How many students?",
                     "A field trip costs $350 for the bus plus $15 admission per student. Each student pays $33 in total. How many students?",
                     "A field trip costs $350 for the bus plus $15 admission per student. Each student pays $32.50 in total. How many buses?",
                     "A field trip costs $350 for the bus plus $15 admission per student plus 5% tax. Each student pays $32.50 in total. How many students?",
                     "A field trip costs $350 each for the bus plus $15 admission per student. Each student pays $32.50 in total. How many students?",
                     "A field trip costs $350 for the bus plus $15 admission per student for part of the year. Each student pays $32.50 in total. How many students?",
                     "A field trip costs $350 for the bus plus $15 admission per student. Each student pays $32.50 in total and two chaperones come. How many students?"):
            self.assertIsNone(answers(text), text)

    def test_change_ages_shared_set(self):
        """Set 21: wordings for percent_change_between, ages_later_multiple and shared_fixed_cost, written after all three were finished and run once, untuned.
        Two answers are declined (safe misses): "twice as old" is a spelled number, and "per ticket" does not match "people"."""
        from fresh_word_problems_21 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-first set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 2, 6))

    def test_known_weight_at_two_prices(self):
        # "two teas" is the two prices, the same way "two jobs" already is
        self.assertEqual(answers("A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $239. How many kg of each?"), values(12, 19))
        self.assertEqual(answers("A shop sold 30 kg of two teas, one at $6/kg and one at $9/kg, for $231. How many kg of each?"), values(13, 17))
        self.assertEqual(answers("A shop sold 50 kg of two coffees, one at $8/kg and one at $10/kg, for $424. How many kg of each?"), values(12, 38))
        r = WS.solve("A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $239. How many kg of each?")
        self.assertEqual(r.values, [Fraction(19), Fraction(12)])
        self.assertIn("x + y = 31 and 5x + 12y = 239", r.reading)
        # a third price, a spelled number other than "two <kinds>", a total that is not reachable, equal prices, "each" after the total, a question for money, part of the year
        for text in ("A shop sold 31 kg of two teas, one at $5/kg, one at $8/kg and one at $12/kg, for $239. How many kg of each?",
                     "A shop sold 31 kg of three teas, one at $5/kg and one at $12/kg, for $239. How many kg of each?",
                     "A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $240. How many kg of each?",
                     "A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $100. How many kg of each?",
                     "A shop sold 31 kg of two teas, one at $5/kg and one at $5/kg, for $239. How many kg of each?",
                     "A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $239 each. How many kg of each?",
                     "A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $239. How much did the first tea earn?",
                     "A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $239 for part of the year. How many kg of each?"):
            self.assertIsNone(answers(text), text)

    def test_two_rates_one_pile(self):
        self.assertEqual(answers("Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1,440 words?"), values(16))
        self.assertEqual(answers("Two typists type 70 and 30 words per minute. Working together, how long will they take to type 3800 words?"), values(38))
        self.assertEqual(answers("Two typists type 55 words per minute and 35 words per minute. Working together, how long will they take to type 1,440 words?"), values(16))
        self.assertEqual(answers("Two pumps move 25 and 15 gallons per hour. Working together, how many hours will they take to move 200 gallons?"), values(5))
        r = WS.solve("Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1,440 words?")
        self.assertIn("(55 + 35)t = 1440", r.reading)
        self.assertIn("t = 16 minutes", r.reading)
        r = WS.solve("Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1,445 words?")
        self.assertEqual(r.values, [Fraction(289, 18)])                   # an exact fraction of a minute
        # the unit asked is not the unit of the rates, a rate asked for, a rate of zero, "alone", a different pile unit, a third typist, a spelled number, part of the day
        for text in ("Two typists type 55 and 35 words per minute. Working together, how many hours will they take to type 1,440 words?",
                     "Two typists type 55 and 35 words per minute. Working together, how many words per minute is that?",
                     "Two typists type 55 and 0 words per minute. Working together, how long will they take to type 1,440 words?",
                     "Two typists type 55 and 35 words per minute. Alone, how long will the first take to type 1,440 words?",
                     "Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1,440 pages?",
                     "Three typists type 55 and 35 words per minute. Working together, how long will they take to type 1,440 words?",
                     "Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1,440 words for part of the day?"):
            self.assertIsNone(answers(text), text)

    def test_least_for_profit(self):
        self.assertEqual(answers("A school dance costs $303 to run. Tickets are $8. How many tickets must be sold for a profit of at least $2,200?"), values(313))
        self.assertEqual(answers("A school dance costs $385 to run. Tickets are $12. How many tickets must be sold for a profit of at least $700?"), values(91))
        self.assertEqual(answers("A club dinner costs $450 to host. Plates are $15. How many plates must be sold for a profit of at least $600?"), values(70))
        r = WS.solve("A school dance costs $303 to run. Tickets are $8. How many tickets must be sold for a profit of at least $2,200?")
        self.assertIn("8n - 303 >= 2200", r.reading)
        self.assertIn("313 sold make $2201, one fewer makes $2193", r.reading)   # 313 reaches the goal, 312 does not
        for text, n in (("A school dance costs $303 to run. Tickets are $8. How many tickets must be sold for a profit of at least $2,200?", 313),
                        ("A school dance costs $385 to run. Tickets are $12. How many tickets must be sold for a profit of at least $700?", 91),
                        ("A club dinner costs $450 to host. Plates are $15. How many plates must be sold for a profit of at least $600?", 70)):
            nums = [Fraction(x.replace(",", "")) for x in re.findall(r"\$([\d,]+)", text)]
            cost, price, goal = nums[0], nums[1], nums[2]
            self.assertGreaterEqual(price * n - cost, goal)                   # n is enough
            self.assertLess(price * (n - 1) - cost, goal)                     # one fewer is not
        # "at most", a question about something that can be sold ("can be sold"), another thing sold, break even, a "per" or percent, a spelled number, part of the year, tax
        for text in ("A school dance costs $303 to run. Tickets are $8. How many tickets must be sold for a profit of at most $2,200?",
                     "A school dance costs $303 to run. Tickets are $8. How many tickets can be sold for a profit of at least $2,200?",
                     "A school dance costs $303 to run. Tickets are $8. How many snacks must be sold for a profit of at least $2,200?",
                     "A school dance costs $303 to run. Tickets are $8. How many tickets must be sold to break even?",
                     "A school dance costs $303 to run. Tickets are twice $8. How many tickets must be sold for a profit of at least $2,200?",
                     "A school dance costs $303 to run. Tickets are $8. How many tickets must be sold for a profit of at least $2,200 for part of the year?",
                     "A school dance costs $303 to run. Tickets are $8. How many tickets must be sold for a profit of at least $2,200 after tax?"):
            self.assertIsNone(answers(text), text)

    def test_weights_piles_profit_set(self):
        """Set 22: wordings for the three families added together, written after all three were finished and run once, untuned.
        One answer is declined (a safe miss): "two flours" is not one of the "two <kinds>" words."""
        from fresh_word_problems_22 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-second set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (6, 1, 4))

    def test_known_amount_unit_matches_the_price_unit(self):
        # 31 lb at $5/kg is not 31 kg: the known amount's unit has to be the unit of the price
        self.assertIsNone(answers("A shop sold 31 lb of two teas, one at $5/kg and one at $12/kg, for $239. How many kg of each?"))
        self.assertIsNone(answers("A shop sold 31 kg of two teas, one at $5/lb and one at $12/lb, for $239. How many kg of each?"))
        self.assertIsNone(answers("A shop sold 31 hours of two teas, one at $5/kg and one at $12/kg, for $239. How many kg of each?"))
        self.assertIsNone(answers("Yara works at $16 an hour and $22 an hour for 61 kg, earning $1,156. How many hours at each rate?"))
        # the same units still answer
        self.assertEqual(answers("A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $239. How many kg of each?"), values(12, 19))
        self.assertEqual(answers("A shop sold 31 lb of two teas, one at $5/lb and one at $12/lb, for $239. How many lb of each?"), values(12, 19))
        self.assertEqual(answers("Yara works at $16 an hour and $22 an hour for 61 hours, earning $1,156. How many hours at each rate?"), values(30, 31))
        self.assertEqual(answers("Yara works two jobs paying $16/h and $22/h. Last month 61 hours were worked in total, earning $1156. How many hours were worked at the $16 job?"), values(30, 31))
        self.assertEqual(answers("A cafe sold 40 drinks, some at $3 each and some at $5 each, for $150. How many of each?"), values(15, 25))

    def test_two_priced_items(self):
        self.assertEqual(answers("A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,500. How many of each?"), values(133, 495))
        self.assertEqual(answers("A school play sold 150 tickets: adult tickets at $12 and student tickets at $7. Sales came to $1,380. How many of each?"), values(66, 84))
        r = WS.solve("A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,500. How many of each?")
        self.assertEqual(r.values, [Fraction(495), Fraction(133)])
        self.assertIn("x + y = 628 and 30x + 50y = 21500", r.reading)
        # a third price, equal prices, counts that are not whole or not positive, "each" after the total, a fee, a question for money, twice, part of the season
        for text in ("A concert sold 628 tickets: lawn seats at $30, reserved seats at $50 and VIP seats at $90. Ticket sales totaled $21,500. How many of each?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $30. Ticket sales totaled $21,500. How many of each?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,501. How many of each?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $2,000. How many of each?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,500 each. How many of each?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,500, plus a 5% fee. How many of each?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,500. How much was the lawn revenue?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50, and twice as many lawn. Ticket sales totaled $21,500. How many of each?",
                     "A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,500 for part of the season. How many of each?"):
            self.assertIsNone(answers(text), text)

    def test_plan_with_included(self):
        self.assertEqual(answers("A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How much data was used?"), values(13))
        self.assertEqual(answers("A phone plan costs $30 a month and includes 15 GB of data. Each extra GB costs $8. The bill was $62. How much data was used?"), values(19))
        r = WS.solve("A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How much data was used?")
        self.assertEqual(r.values, [Fraction(13)])                         # the total data, not the 8 extra gigabytes
        self.assertIn("50 + 5(d - 5) = 90", r.reading)
        r = WS.solve("A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $92. How much data was used?")
        self.assertEqual(r.values, [Fraction(67, 5)])                      # exact, never 13.4 rounded
        # a bill that is not above the monthly price, a question for the extra only, another unit for the extra, a question for a price, unlimited,
        # "each" after the bill, part of the year
        for text in ("A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $50. How much data was used?",
                     "A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $40. How much data was used?",
                     "A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How much extra data was used?",
                     "A phone plan costs $50 a month and includes 5 GB of data. Each extra minute costs $5. The bill was $90. How much data was used?",
                     "A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How much was the bill per GB?",
                     "A phone plan costs $50 a month and includes unlimited data. Each extra GB costs $5. The bill was $90. How much data was used?",
                     "A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90 each. How much data was used?",
                     "A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90 for part of the year. How much data was used?"):
            self.assertIsNone(answers(text), text)

    def test_most_that_fits(self):
        self.assertEqual(answers("An elevator holds at most 1,200 lb. A 200 lb worker is loading 60 lb boxes. How many boxes can go up with the worker?"), values(16))
        self.assertEqual(answers("An elevator holds at most 1200 lb. A 180 lb worker is loading 60 lb boxes. How many boxes can go up with the worker in one trip?"), values(17))
        r = WS.solve("An elevator holds at most 1,200 lb. A 200 lb worker is loading 60 lb boxes. How many boxes can go up with the worker?")
        self.assertIn("200 + 60n <= 1200", r.reading)
        self.assertIn("one more would weigh 1220, over 1200", r.reading)               # 200 + 60 * 17
        for limit, w, b in ((1200, 200, 60), (1200, 180, 60), (1500, 160, 40), (1800, 150, 50)):   # n is the most: n boxes fit, one more does not
            text = "An elevator holds at most %d lb. A %d lb worker is loading %d lb boxes. How many boxes can go up with the worker in one trip?" % (limit, w, b)
            n = int(next(iter(answers(text))))
            self.assertLessEqual(w + b * n, limit)
            self.assertGreater(w + b * (n + 1), limit)
        # a load already at or over the limit, "at least", another unit, another thing, a question for weight, several trips, two workers, part of the day
        for text in ("An elevator holds at most 1,200 lb. A 1,300 lb worker is loading 60 lb boxes. How many boxes can go up with the worker?",
                     "An elevator holds at most 1,200 lb. A 1,200 lb worker is loading 60 lb boxes. How many boxes can go up with the worker?",
                     "An elevator holds at least 1,200 lb. A 200 lb worker is loading 60 lb boxes. How many boxes can go up with the worker?",
                     "An elevator holds at most 1,200 lb. A 200 lb worker is loading 60 kg boxes. How many boxes can go up with the worker?",
                     "An elevator holds at most 1,200 lb. A 200 lb worker is loading 60 lb boxes. How many crates can go up with the worker?",
                     "An elevator holds at most 1,200 lb. A 200 lb worker is loading 60 lb boxes. How much can go up with the worker?",
                     "An elevator holds at most 1,200 lb. A 200 lb worker is loading 60 lb boxes in several trips. How many boxes can go up with the worker?",
                     "An elevator holds at most 1,200 lb. Two 200 lb workers are loading 60 lb boxes. How many boxes can go up with the workers?",
                     "An elevator holds at most 1,200 lb. A 200 lb worker is loading 60 lb boxes for part of the day. How many boxes can go up with the worker?"):
            self.assertIsNone(answers(text), text)

    def test_units_seats_plans_fits_set(self):
        """Set 23: wordings for the unit fix and the three families added together, written after all of them were finished and run once, untuned.
        One answer is declined (a safe miss): "How many GB were stored?" does not say "used"."""
        from fresh_word_problems_23 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-third set, unit fix and three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (6, 1, 6))

    def test_plan_question_counts_the_included_unit(self):
        # "how many hours were used" on a plan in gigabytes asks for something else: X in "how many X" has to be the included unit
        self.assertIsNone(answers("A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How many hours were used?"))
        self.assertIsNone(answers("A gym plan costs $40 a month and includes 10 hours of court time. Each extra hour costs $6. The bill was $76. How many days were used?"))
        self.assertEqual(answers("A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How much data was used?"), values(13))
        self.assertEqual(answers("A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How many GB were used?"), values(13))
        self.assertEqual(answers("A gym plan costs $40 a month and includes 10 hours of court time. Each extra hour costs $6. The bill was $76. How many hours were used?"), values(16))

    def test_line_from_two_points(self):
        self.assertEqual(answers("For a taxi, 4 miles cost $46 and 11 miles cost $88. The cost is C = m·x + b. How many miles cost $136?"), values(19))
        self.assertEqual(answers("For a taxi ride, 4 miles cost $46 and 11 miles cost $88. The cost is linear: C = m·x + b. Find m and b, then how many miles cost $136."), values(6, 19, 22))
        self.assertEqual(answers("For a plumber's bill, 5 hours cost $107 and 7 hours cost $121. The cost is linear: C = m·x + b. Find m and b, then how many hours cost $163."), values(7, 13, 72))
        r = WS.solve("For a taxi, 4 miles cost $46 and 11 miles cost $88. The cost is C = m·x + b. How many miles cost $136?")
        self.assertEqual(r.values, [Fraction(19)])
        self.assertIn("m = (88 - 46) / (11 - 4) = 6 and b = 46 - 6 x 4 = 22", r.reading)       # m and b are shown
        self.assertIn("6x + 22 = 136", r.reading)
        r = WS.solve("For a taxi, 4 miles cost $46 and 11 miles cost $88. The cost is C = m·x + b. How many miles cost $137?")
        self.assertEqual(r.values, [Fraction(115, 6)])                      # an exact fraction of a mile
        # a third ride that is on the line still answers; one that is not declines
        self.assertEqual(answers("For a taxi, 4 miles cost $46 and 11 miles cost $88 and 6 miles cost $58. The cost is C = m·x + b. How many miles cost $136?"), values(19))
        for text in ("For a taxi, 4 miles cost $46 and 11 miles cost $88 and 6 miles cost $60. The cost is C = m·x + b. How many miles cost $136?",
                     "For a taxi, 4 miles cost $46 and 4 miles cost $50. The cost is C = m·x + b. How many miles cost $136?",
                     "For a taxi, 4 miles cost $46 and 11 miles cost $88. The cost is C = m·x + b. How many miles cost $20?",
                     "For a taxi, 4 miles cost $46 and 11 hours cost $88. The cost is C = m·x + b. How many miles cost $136?",
                     "For a taxi, 4 miles cost $46 and 11 miles cost $88. The cost is C = m·x + b. How much do 19 miles cost?",
                     "For a taxi, 4 miles cost $46 and 11 miles cost $40. The cost is C = m·x + b. How many miles cost $136?",
                     "For a taxi, 4 miles cost $46 and 11 miles cost $88. The cost is quadratic. How many miles cost $136?",
                     "For a taxi, 4 miles cost $46 and 11 miles cost $88. The cost is C = m·x + b. How many miles cost $136 for part of the year?"):
            self.assertIsNone(answers(text), text)

    def test_election_margin(self):
        self.assertEqual(answers("The winner got 58% of the votes and won by 3,392 votes. How many votes were cast?"), values(21200))
        self.assertEqual(answers("In a two-candidate election, the winner got 60% of the votes and won by 1360 votes. How many votes were cast?"), values(6800))
        r = WS.solve("The winner got 58% of the votes and won by 3,392 votes. How many votes were cast?")
        self.assertEqual(r.values, [Fraction(21200)])
        self.assertIn("58% of V - 42% of V = 3392", r.reading)
        self.assertIn("0.16V = 3392 and V = 21200", r.reading)
        # a total that is not a whole number, a share of 50% or less, a third candidate, the loser's figures, a question for a percent, twice, part of the year
        for text in ("The winner got 58% of the votes and won by 3,393 votes. How many votes were cast?",
                     "The winner got 50% of the votes and won by 3,392 votes. How many votes were cast?",
                     "The winner got 48% of the votes and won by 3,392 votes. How many votes were cast?",
                     "In a three-candidate race, the winner got 58% of the votes and won by 3,392 votes. How many votes were cast?",
                     "The winner got 58% of the votes and won by 3,392 votes over the third candidate. How many votes were cast?",
                     "The loser got 42% of the votes and lost by 3,392 votes. How many votes were cast?",
                     "The winner got 58% of the votes and won by 3,392 votes. What percent did the loser get?",
                     "The winner got 58% of the votes and won by twice 3,392 votes. How many votes were cast?",
                     "The winner got 58% of the votes and won by 3,392 votes for part of the year. How many votes were cast?"):
            self.assertIsNone(answers(text), text)

    def test_wind_same_time(self):
        self.assertEqual(answers("A plane flies 1,590 miles with a 40 mph tailwind in the same time it flies 1,350 miles into that wind. What is its speed in still air?"), values(490))
        self.assertEqual(answers("A plane flies 1590 miles with a 40 mph tailwind in the same time it flies 1350 miles into the same wind as a headwind. What is the plane's speed in still air?"), values(490))
        r = WS.solve("A plane flies 1,590 miles with a 40 mph tailwind in the same time it flies 1,350 miles into that wind. What is its speed in still air?")
        self.assertIn("1590/(p + 40) = 1350/(p - 40)", r.reading)
        self.assertIn("p = 490 mph", r.reading)
        r = WS.solve("A plane flies 1,000 miles with a 30 mph tailwind in the same time it flies 900 miles into that wind. What is its speed in still air?")
        self.assertEqual(r.values, [Fraction(30 * 1900, 100)])               # 570, and the two times really are equal
        p = r.values[0]
        self.assertEqual(Fraction(1000) / (p + 30), Fraction(900) / (p - 30))
        # the headwind trip is longer, the trips are equal, mixed units, the wind speed asked, a return trip, part of the year
        for text in ("A plane flies 1,350 miles with a 40 mph tailwind in the same time it flies 1,590 miles into that wind. What is its speed in still air?",
                     "A plane flies 1,590 miles with a 40 mph tailwind in the same time it flies 1,590 miles into that wind. What is its speed in still air?",
                     "A plane flies 1,590 miles with a 40 km/h tailwind in the same time it flies 1,350 miles into that wind. What is its speed in still air?",
                     "A plane flies 1,590 miles with a 40 mph tailwind in the same time it flies 1,350 miles into that wind. What is the wind speed?",
                     "A plane flies 1,590 miles with a 40 mph tailwind in the same time it flies 1,350 miles into that wind and then returns. What is its speed in still air?",
                     "A plane flies 1,590 miles with a 40 mph tailwind in the same time it flies 1,350 miles into that wind for part of the year. What is its speed in still air?"):
            self.assertIsNone(answers(text), text)

    def test_line_election_wind_set(self):
        """Set 24: wordings for the question-unit fix and the three families added together, written after all of it was finished and run once, untuned.
        One answer is declined (a safe miss): "two people" is not one of the "two <candidates>" phrases."""
        from fresh_word_problems_24 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-fourth set, question unit and three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 1, 5))

    def test_measured_heights_until_equal(self):
        self.assertEqual(answers("Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week. After how many weeks will they be the same height?"), values(Fraction(15, 2)))
        self.assertEqual(answers("Plant A is 15 cm tall and grows 3 cm a week. Plant B is 35 cm tall and grows 2 cm a week. After how many weeks will they be the same height?"), values(20))
        self.assertEqual(answers("Plant A is 7 cm tall and grows 2 cm a week. Plant B is 25 cm tall and grows 1.5 cm a week. After how many weeks will they be the same height?"), values(36))
        r = WS.solve("Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week. After how many weeks will they be the same height?")
        self.assertEqual(r.values, [Fraction(15, 2)])
        self.assertIn("13 + 3 t = 28 + 1 t", r.reading)
        self.assertIn("t = 15/2 weeks", r.reading)                          # an exact fraction of a week
        r = WS.solve("Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and shrinks 1 cm a week. After how many weeks will they be the same height?")
        self.assertEqual(r.values, [Fraction(15, 4)])                       # one may shrink
        # people and dollars are still whole numbers only (a fraction of a person), a negative time, equal growth, mixed units, a question for the height
        self.assertIsNone(answers("Town A has 18,000 people and grows by 2,000 a year. Town B has 63,001 and shrinks by 500 a year. In how many years are they equal?"))
        for text in ("Plant A is 28 cm tall and grows 3 cm a week. Plant B is 13 cm tall and grows 1 cm a week. After how many weeks will they be the same height?",
                     "Plant A is 13 cm tall and grows 1 cm a week. Plant B is 28 cm tall and grows 3 cm a week. After how many weeks will they be the same height?",
                     "Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 3 cm a week. After how many weeks will they be the same height?",
                     "Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 inches tall and grows 1 cm a week. After how many weeks will they be the same height?",
                     "Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a month. After how many weeks will they be the same height?",
                     "Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week. How tall will they be when they are the same height?",
                     "Plant A is 13 cm tall and grows twice 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week. After how many weeks will they be the same height?",
                     "Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week for part of the year. After how many weeks will they be the same height?"):
            self.assertIsNone(answers(text), text)

    def test_base_plus_extra_over_time(self):
        self.assertEqual(answers("Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120. How many extra chores were done?"), values(10))
        self.assertEqual(answers("Zane gets $10 allowance a week plus $3 for each extra chore. Over 8 weeks that came to $92. How many extra chores were done?"), values(4))
        r = WS.solve("Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120. How many extra chores were done?")
        self.assertEqual(r.values, [Fraction(10)])                          # the TOTAL number of extra chores
        self.assertIn("8 x 10 + 4n = 120", r.reading)
        # money asked for, a total that is not above the allowance, not a whole number of chores, another period, another noun, "each" after the total, a fee, twice, part of the year
        for text in ("Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120. How much money did the chores earn?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $80. How many extra chores were done?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $70. How many extra chores were done?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $121. How many extra chores were done?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 months that came to $120. How many extra chores were done?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120. How many extra dishes were done?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120 each. How many extra chores were done?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120, less a 5% fee. How many extra chores were done?",
                     "Umar gets $10 allowance a week plus twice $4 for each extra chore. Over 8 weeks that came to $120. How many extra chores were done?",
                     "Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120 for part of the year. How many extra chores were done?"):
            self.assertIsNone(answers(text), text)

    def test_distance_speed_time(self):
        self.assertEqual(answers("How long does it take to travel 160 km at 40 km/h?"), values(4))
        self.assertEqual(answers("Using distance = speed × time, how long does it take to travel 490 km at 50 km/h?"), values(Fraction(49, 5)))
        self.assertEqual(answers("How far does a car go in 4 hours at 40 km/h?"), values(160))
        self.assertEqual(answers("A cyclist travels 160 km in 4 hours. How fast is the cyclist?"), values(40))
        self.assertEqual(answers("How long does it take to travel 160 miles at 40 mph?"), values(4))
        r = WS.solve("How long does it take to travel 160 km at 40 km/h?")
        self.assertIn("160 = 40t, so t = 4 hours", r.reading)
        r = WS.solve("How far does a car go in 4 hours at 40 km/h?")
        self.assertIn("d = 40 x 4, so d = 160 km", r.reading)
        r = WS.solve("A cyclist travels 160 km in 4 hours. How fast is the cyclist?")
        self.assertIn("s = 40 km/h", r.reading)
        # the distance unit does not match the speed unit, a zero speed, a third quantity, two legs, only one quantity given, a time in minutes, a spelled number,
        # a question for the wrong quantity, part of the day
        for text in ("How long does it take to travel 160 km at 40 mph?",
                     "How long does it take to travel 160 miles at 40 km/h?",
                     "How long does it take to travel 160 km at 0 km/h?",
                     "How long does it take to travel 160 km at 40 km/h in 3 hours?",
                     "How long does it take to travel 160 km at 40 km/h and then 20 km at 10 km/h?",
                     "How far does a car go in 4 hours?",
                     "How long does it take to travel 160 km?",
                     "How far does a car travel in 30 minutes at 40 km/h?",
                     "How long does it take to travel two hundred km at 40 km/h?",
                     "How fast does a car go in 4 hours at 40 km/h?",
                     "How long does it take to travel 160 km at 40 km/h for part of the day?"):
            self.assertIsNone(answers(text), text)

    def test_average_speed_two_leg_unknown_time(self):
        cases = [
            ("Kofi drove 1 hour at 30 mph and then some hours at 55 mph. The average speed for the whole trip was 50 mph. How long was the second part?", 4),
            ("Aiden drove 2 hours at 60 mph and then some hours at 45 mph. The average speed for the whole trip was 55 mph. How long was the second part?", 1),
            ("Lena drove 2 hours at 30 mph and then some hours at 75 mph. The average speed for the whole trip was 45 mph. How long was the second part?", 1),
            ("Emeka drove 1 hour at 50 mph and then some hours at 45 mph. The average speed for the whole trip was 46 mph. How long was the second part?", 4),
            ("Sofia drove 3 hours at 60 mph and then some hours at 75 mph. The average speed for the whole trip was 66 mph. How long was the second part?", 2),
        ]
        for sentence, expected in cases:
            self.assertEqual(answers(sentence), values(expected), sentence)
        self.assertIsNone(answers("Kofi drove 1 hour at 30 mph and then some hours at 55 mph. The average speed for the whole trip was 50 mph. How far was the second part?"))
        self.assertIsNone(answers("Kofi drove 1 hour at 30 mph and then some hours at 55 mph. How long was the second part?"))
        self.assertIsNone(answers("Kofi drove 1 hour at 30 mph and then 2 hours at 55 mph. The average speed for the whole trip was 50 mph. How long was the second part?"))

    def test_heights_chores_distance_set(self):
        """Set 25: wordings for the three families added together, written after all three were finished and run once, untuned.
        One answer is declined (a safe miss): "the total was $76" is not one of the total cues (came to / received / earned / made ...)."""
        from fresh_word_problems_25 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-fifth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (6, 1, 5))

    def test_pages_per_day(self):
        self.assertEqual(answers("A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days?"), values(53))
        self.assertEqual(answers("A 548-page book has 116 pages already read. How many pages a day must be read to finish in 18 days?"), values(24))
        r = WS.solve("A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days?")
        self.assertIn("13 + 6p = 331", r.reading)
        self.assertIn("p = (331 - 13) / 6 = 53", r.reading)
        r = WS.solve("A 331-page book has 13 pages already read. How many pages a day must be read to finish in 7 days?")
        self.assertEqual(r.values, [Fraction(318, 7)])                      # an exact fraction
        # zero days, the whole book (or more) already read, another period asked, a question for days or for pages left, a spelled number, twice, part of the term
        for text in ("A 331-page book has 13 pages already read. How many pages a day must be read to finish in 0 days?",
                     "A 331-page book has 331 pages already read. How many pages a day must be read to finish in 6 days?",
                     "A 331-page book has 400 pages already read. How many pages a day must be read to finish in 6 days?",
                     "A 331-page book has 13 pages already read. How many pages a week must be read to finish in 6 days?",
                     "A 331-page book has 13 pages already read. How many days must be read to finish in 6 days?",
                     "A 331-page book has 13 pages already read. How many pages are left?",
                     "A 331-page book has 13 pages already read. How many pages a day must be read to finish in six days?",
                     "A 331-page book has 13 pages already read, and twice that tomorrow. How many pages a day must be read to finish in 6 days?",
                     "A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days for part of the term?"):
            self.assertIsNone(answers(text), text)

    def test_opposite_angles_equal(self):
        self.assertEqual(answers("Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle."), values(80))
        self.assertEqual(answers("Where two lines cross, opposite angles are (3x − 10)° and (6x − 118)°. Find the angle."), values(98))
        self.assertEqual(answers("Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. Find x."), values(38))
        self.assertEqual(answers("Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. Find x and the angle."), values(38, 80))
        self.assertEqual(answers("Where two lines cross, vertical angles are (2x + 4) degrees and (5x - 110) degrees. Find each angle."), values(80))
        r = WS.solve("Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle.")
        self.assertIn("2x + 4 = 5x - 110", r.reading)
        self.assertIn("x = 38 and each angle is 80 degrees", r.reading)
        r = WS.solve("Where two lines cross, opposite angles are (2x + 4)° and (5x − 100)°. Find the angle.")
        self.assertEqual(r.values, [Fraction(220, 3)])                       # an exact fraction of a degree
        # adjacent angles, angles that add to 180, equal coefficients, an angle over 180 or not positive, a third angle, part of the year
        for text in ("Where two lines cross, adjacent angles are (2x + 4)° and (5x − 110)°. Find the angle.",
                     "Where two lines cross, opposite angles add to 180: (2x + 4)° and (5x − 110)°. Find the angle.",
                     "Where two lines cross, opposite angles are (2x + 4)° and (2x − 110)°. Find the angle.",
                     "Where two lines cross, opposite angles are (2x + 90)° and (5x − 120)°. Find the angle.",
                     "Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)° and 30°. Find the angle.",
                     "Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)° for part of the year. Find the angle."):
            self.assertIsNone(answers(text), text)
        # an angle of 0 or less (x = -2 gives 0) and an angle past a straight line (x = 100 gives 204) decline
        self.assertIsNone(answers("Where two lines cross, opposite angles are (2x + 4)° and (3x + 6)°. Find the angle."))
        self.assertIsNone(answers("Where two lines cross, opposite angles are (2x + 4)° and (3x − 96)°. Find the angle."))

    def test_rectangle_from_perimeter_area(self):
        self.assertEqual(answers("A rectangle has a perimeter of 40 ft and an area of 36 ft². Find its length and width."), values(2, 18))
        self.assertEqual(answers("A rectangle has a perimeter of 104 ft and an area of 651 ft². Find its length and width."), values(21, 31))
        self.assertEqual(answers("A rectangle has a perimeter of 40 ft and an area of 100 ft². Find its length and width."), values(10, 10))       # a square is a rectangle
        r = WS.solve("A rectangle has a perimeter of 40 ft and an area of 36 ft². Find its length and width.")
        self.assertEqual(r.values, [Fraction(18), Fraction(2)])
        self.assertIn("l + w = 20 and l w = 36", r.reading)
        for l, w in [(r.values[0], r.values[1])]:
            self.assertEqual(2 * l + 2 * w, 40)                              # both sides fit the perimeter and the area
            self.assertEqual(l * w, 36)
        r = WS.solve("A rectangle has a perimeter of 41 ft and an area of 100 ft². Find its length and width.")
        self.assertEqual(r.values, [Fraction(25, 2), Fraction(8)])           # exact fractions
        # sides that are not real, not exact, an area in another unit, a zero area, a square, another question, part of the year
        for text in ("A rectangle has a perimeter of 40 ft and an area of 101 ft². Find its length and width.",
                     "A rectangle has a perimeter of 40 ft and an area of 37 ft². Find its length and width.",
                     "A rectangle has a perimeter of 40 ft and an area of 36 m². Find its length and width.",
                     "A rectangle has a perimeter of 40 ft and an area of 0 ft². Find its length and width.",
                     "A square has a perimeter of 40 ft and an area of 100 ft². Find its length and width.",
                     "A rectangle has a perimeter of 40 ft and an area of 36 ft². Find its diagonal.",
                     "A rectangle has a perimeter of 40 ft and an area of 36 ft² for part of the year. Find its length and width."):
            self.assertIsNone(answers(text), text)

    def test_pages_angles_rectangle_set(self):
        """Set 26: wordings for pages_per_day, opposite_angles_equal and rectangle_from_perimeter_area, written after all three were finished and run once, untuned."""
        from fresh_word_problems_26 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-sixth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (6, 0, 6))

    def test_pages_days_are_the_time_to_finish(self):
        # the day count must be the time allowed to FINISH the book: "to finish in 6 days" and "within 5 days" stay
        self.assertEqual(answers("A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days?"), values(53))
        self.assertEqual(answers("A 100-page book has 20 pages already read. How many pages a day must be read to finish within 5 days?"), values(16))
        self.assertEqual(answers("A 331-page book has 13 pages already read. How many pages a day must be read to finish the book in 6 days?"), values(53))
        # a day count that is something else (she leaves in 6 days, the library closes in 10 days) is not the time to finish
        self.assertIsNone(answers("A 331-page book has 13 pages already read. She leaves in 6 days. How many pages a day must be read to finish?"))
        self.assertIsNone(answers("In 10 days the library closes. A 100-page book has 20 pages already read. How many pages a day must be read?"))
        self.assertIsNone(answers("A 240-page book has 40 pages already read. The exam is in 8 days. How many pages a day must be read to finish?"))
        self.assertIsNone(answers("A 331-page book has 13 pages already read. How many pages a day must be read to finish before 6 days?"))

    def test_opposite_angles_question_must_ask_for_the_angle(self):
        base = "Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. "
        self.assertEqual(answers(base + "Find the angle."), values(80))
        self.assertEqual(answers(base + "Find each angle."), values(80))
        self.assertEqual(answers(base + "Find x."), values(38))
        self.assertEqual(answers(base + "Find x and the angle."), values(38, 80))
        self.assertEqual(answers(base + "Find the larger angle."), values(80))                 # the two opposite angles are the same
        # a complement, a supplement, a difference, a sum, a half: not the angle itself (10, 100 and 0 are the right answers to those)
        for q in ("Find the complement of the angle.", "Find the supplement of the angle.", "Find the difference of the opposite angles.",
                  "Find the sum of the opposite angles.", "Find half of the angle.", "Find twice the angle."):
            self.assertIsNone(answers(base + q), q)
        # a quadrilateral, a cyclic quadrilateral, an inscribed angle and a circle follow another rule (cyclic opposite angles add to 180)
        for text in ("In a cyclic quadrilateral, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle.",
                     "In a quadrilateral, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle.",
                     "An inscribed angle in a circle: opposite angles are (2x + 4)° and (5x − 110)°. Find the angle.",
                     "In a circle, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle.",
                     "Two vertical angles measure (2x + 4)° and (5x − 110)°. Find the angle."):
            self.assertIsNone(answers(text), text)
        # a parallelogram keeps its opposite angles equal: 80 is right
        self.assertEqual(answers("In a parallelogram, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle."), values(80))

    def test_rectangle_question_and_squared_area(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        self.assertEqual(answers(base + "Find its sides."), values(2, 18))
        self.assertEqual(answers(base + "What are its dimensions?"), values(2, 18))
        # the length is the longer side and the width the shorter
        self.assertEqual(answers(base + "What is its length?"), values(18))
        self.assertEqual(answers(base + "What is its width?"), values(2))
        self.assertEqual(answers(base + "Find the length."), values(18))
        self.assertEqual(answers(base + "Find the width."), values(2))
        r = WS.solve(base + "Find its length and width.")
        self.assertEqual(r.values, [Fraction(18), Fraction(2)])
        self.assertEqual(2 * r.values[0] + 2 * r.values[1], 40)             # both sides still fit the perimeter and the area
        self.assertEqual(r.values[0] * r.values[1], 36)
        # a sum, difference or product of the sides is not the sides (20, 16 and 36 are the right answers to those)
        for q in ("Find the sum of its length and width.", "Find the difference of its length and width.", "Find the product of its length and width.",
                  "Find the ratio of its length to its width.", "Find its diagonal."):
            self.assertIsNone(answers(base + q), q)
        # the area has to be marked squared: ft^2, ft², sq ft and square ft stay; a bare "36 ft" does not
        for mark in ("ft²", "ft^2", "sq ft", "square ft"):
            self.assertEqual(answers("A rectangle has a perimeter of 40 ft and an area of 36 %s. Find its length and width." % mark), values(2, 18), mark)
        self.assertEqual(answers("A rectangle has a perimeter of 40 feet and an area of 36 square feet. Find its length and width."), values(2, 18))
        self.assertIsNone(answers("A rectangle has a perimeter of 40 ft and an area of 36 ft. Find its length and width."))
        self.assertIsNone(answers("A rectangle has a perimeter of 40 m and an area of 36 m. Find its length and width."))
        self.assertIsNone(answers("A square has a perimeter of 40 ft and an area of 100 ft². Find its length and width."))

    def test_neighbours_of_the_fixes_set(self):
        """Set 27: neighbours of the wordings fixed in this batch, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_27 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-seventh set, neighbours of the fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 0, 6))

    def test_pages_deadline_belongs_to_this_book(self):
        base = "A 331-page book has 13 pages already read. How many pages a day must be read to finish"
        # the forms that stay answered
        self.assertEqual(answers(base + " in 6 days?"), values(53))
        self.assertEqual(answers(base + " within 6 days?"), values(53))
        self.assertEqual(answers(base + " the book in 6 days?"), values(53))
        self.assertEqual(answers(base + " it in 6 days?"), values(53))
        self.assertEqual(answers(base + " reading the book in 6 days?"), values(53))
        self.assertEqual(answers("A 100-page book has 20 pages already read. How many pages a day must be read to finish within 5 days?"), values(16))
        # "She must finish in 6 days" is the deadline: the 80 pages left over 6 days
        self.assertEqual(answers("A 100-page book has 20 pages already read. She must finish in 6 days. How many pages a day must be read?"), values(Fraction(40, 3)))
        # the past tense does not count: "already finished in 6 days" is how long the 20 pages took
        self.assertIsNone(answers("A 100-page book has 20 pages already finished in 6 days. How many pages a day must be read to finish?"))
        # the words between "finish" and the day count must be about the same book: another job's deadline declines
        self.assertIsNone(answers(base + " the chapter in 6 days?"))
        self.assertIsNone(answers("A 200-page book has 20 pages already read. How many pages a day must be read to finish the essay in 8 days?"))
        self.assertIsNone(answers("A 100-page book has 20 pages already read. How many pages a day must be read to finish the race in 2 days?"))
        self.assertIsNone(answers("A 300-page novel has 60 pages already read. How many pages a day must be read to finish the assignment in 8 days?"))
        # a novel is a book; a report is not
        self.assertEqual(answers("A 100-page novel has 20 pages already read. How many pages a day must be read to finish the book in 5 days?"), values(16))
        self.assertIsNone(answers("A 100-page report has 20 pages already read. How many pages a day must be read to finish the book in 5 days?"))

    def test_opposite_angles_named_kind(self):
        d = "Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. "          # 80 degrees
        e = "Where two lines cross, opposite angles are (3x − 10)° and (6x − 118)°. "     # 98 degrees
        for q in ("Find the angle.", "Find each angle.", "Find x.", "Find x and the angle.", "Find the larger angle."):
            self.assertIsNotNone(answers(d + q), q)                                                    # the plain questions stay
        self.assertEqual(answers(d + "Find the angle."), values(80))
        self.assertEqual(answers(d + "Find x and the angle."), values(38, 80))
        self.assertEqual(answers("In a parallelogram, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle."), values(80))
        # a named kind is answered only when the angle IS that kind
        self.assertEqual(answers(d + "Find the acute angle."), values(80))
        self.assertEqual(answers(e + "Find the obtuse angle."), values(98))
        self.assertIsNone(answers(e + "Find the acute angle."))                                      # 98 is not acute
        self.assertIsNone(answers(d + "Find the obtuse angle."))                                     # 80 is not obtuse
        self.assertIsNone(answers(d + "Find the right angle."))                                      # 80 is not 90
        self.assertIsNone(answers("Where two lines cross, the opposite angles form a straight angle: (2x + 4)° and (5x − 110)°. Find the angle."))
        self.assertIsNone(answers("Where two lines cross, the opposite angles form a right angle: (4x + 10)° and (6x − 20)°. Find x."))
        # and a straight or right angle is answered when it really is one: 2x = x + 90 gives x = 90 and an angle of 180; 2x = x + 45 gives 90
        # (the 180 example moved onto the question: "form a straight angle" is a statement that the two add up to 180, see test_opposite_angles_form_is_a_statement)
        self.assertEqual(answers("Where two lines cross, opposite angles are (2x + 0)° and (x + 90)°. Find the straight angle."), values(180))
        self.assertEqual(answers("Where two lines cross, opposite angles are (2x + 0)° and (x + 45)°. Find the right angle."), values(90))

    def test_rectangle_uses_the_problems_own_statement_of_the_longer_side(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # with no statement the length is the longer side
        self.assertEqual(answers(base + "What is its length?"), values(18))
        self.assertEqual(answers(base + "What is its width?"), values(2))
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        # the problem says which is longer
        self.assertEqual(answers(base + "The length is shorter than the width. What is its length?"), values(2))
        self.assertEqual(answers(base + "Its width is the longer side. What is its width?"), values(18))
        self.assertEqual(answers(base + "The length is the smaller side. What is its length?"), values(2))
        self.assertEqual(answers(base + "The width is greater than the length. What is its width?"), values(18))
        self.assertEqual(answers(base + "The width is greater than the length. What is its length?"), values(2))
        self.assertEqual(answers(base + "The length is longer than the width. What is its length?"), values(18))
        self.assertEqual(answers(base + "The longer side is the width. What is its width?"), values(18))
        r = WS.solve(base + "The length is shorter than the width. Find its length and width.")
        self.assertEqual(r.values, [Fraction(2), Fraction(18)])             # both sides: the length 2, the width 18
        self.assertEqual(2 * r.values[0] + 2 * r.values[1], 40)
        self.assertEqual(r.values[0] * r.values[1], 36)
        # a statement that contradicts itself, or compares a side with itself, declines
        self.assertIsNone(answers(base + "The length is shorter than the length. What is its length?"))
        self.assertIsNone(answers(base + "The length is longer than the width and the width is longer than the length. What is its width?"))

    def test_deadline_kind_and_orientation_set(self):
        """Set 28: neighbours of the batch-25 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_28 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-eighth set, neighbours of the batch-25 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (7, 0, 6))

    def test_pages_question_may_not_name_another_job(self):
        book = "A 100-page book has 20 pages already read. "
        # the forms that stay answered: 80 pages over 6 days is 40/3
        for tail in ("She must finish the book in 6 days. How many pages a day must be read?",
                     "She must finish the book in 6 days. How many pages a day must be read to finish?",
                     "She must finish the book in 6 days. How many pages a day must be read to finish it?",
                     "She must finish the book in 6 days. How many pages a day must be read to finish reading the book?"):
            self.assertEqual(answers(book + tail), values(Fraction(40, 3)), tail)
        self.assertEqual(answers("A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days?"), values(53))
        self.assertEqual(answers("A 100-page novel has 20 pages already read. She must finish the story in 6 days. How many pages a day must be read?"), values(Fraction(40, 3)))
        self.assertEqual(answers("A 100-page report has 20 pages already read. She must finish the report in 6 days. How many pages a day must be read?"), values(Fraction(40, 3)))
        # the question (or any sentence) naming a different job declines: the chapter is not the book
        self.assertIsNone(answers(book + "She must finish the book in 6 days. How many pages a day must be read to finish the chapter?"))
        self.assertIsNone(answers(book + "How many pages a day must be read to finish the chapter? She must finish the book in 6 days."))
        self.assertIsNone(answers(book + "She must finish the book in 6 days. How many pages a day must be read to finish the homework?"))
        self.assertIsNone(answers("A 100-page report has 20 pages already read. She must finish the story in 6 days. How many pages a day must be read?"))

    def test_opposite_angles_form_is_a_statement(self):
        # "form a straight angle" says the two angles ADD UP to 180; here each angle is 180, so the statement is false and the problem declines
        self.assertIsNone(answers("Where two lines cross, the opposite angles form a straight angle: (2x + 0)° and (x + 90)°. Find the angle."))
        self.assertIsNone(answers("Where two lines cross, the opposite angles form a right angle: (4x + 10)° and (6x − 20)°. Find x."))
        self.assertIsNone(answers("Where two lines cross, the opposite angles form an obtuse angle: (2x + 4)° and (5x − 110)°. Find the angle."))
        # the 180 example lives on the question: "Find the straight angle"
        d = "Where two lines cross, opposite angles are (2x + 0)° and (x + 90)°. "
        self.assertEqual(answers(d + "Find the straight angle."), values(180))
        self.assertEqual(answers(d + "Find the angle."), values(180))
        self.assertIsNone(answers(d + "Find the right angle."))                                      # 180 is not 90
        e = "Where two lines cross, opposite angles are (2x + 0)° and (x + 45)°. "
        self.assertEqual(answers(e + "Find the right angle."), values(90))
        self.assertIsNone(answers(e + "Find the straight angle."))
        f = "Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. "
        self.assertEqual(answers(f + "Find the acute angle."), values(80))
        self.assertIsNone(answers(f + "Find the obtuse angle."))

    def test_rectangle_more_less_wider_and_a_condition_in_the_question(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # no statement: the length is the longer side
        self.assertEqual(answers(base + "What is its length?"), values(18))
        self.assertEqual(answers(base + "What is its width?"), values(2))
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        # less / more / wider / narrower are comparisons too
        self.assertEqual(answers(base + "The length is less than the width. What is its length?"), values(2))
        self.assertEqual(answers(base + "The width is more than the length. What is its width?"), values(18))
        self.assertEqual(answers(base + "The width is the wider side. What is its width?"), values(18))
        self.assertEqual(answers(base + "The length is the narrower side. What is its length?"), values(2))
        # a statement inside the question counts, and naming the other side there does not ask for both
        self.assertEqual(answers(base + "What is its length if the length is shorter than the width?"), values(2))
        self.assertEqual(answers(base + "What is its width if the length is shorter than the width?"), values(18))
        self.assertEqual(answers(base + "What is its length when the width is the longer side?"), values(2))
        self.assertEqual(answers(base + "What is its length if the length is longer than the width?"), values(18))
        r = WS.solve(base + "Find its length and width if the length is shorter than the width.")
        self.assertEqual(r.values, [Fraction(2), Fraction(18)])             # both sides asked: both returned
        self.assertEqual(2 * r.values[0] + 2 * r.values[1], 40)
        self.assertEqual(r.values[0] * r.values[1], 36)
        r = WS.solve(base + "Find its length and width.")
        self.assertEqual(r.values, [Fraction(18), Fraction(2)])
        # a sum asked with a condition still declines
        self.assertIsNone(answers(base + "What is the sum of its length and width if the length is shorter than the width?"))
        self.assertIsNone(answers(base + "What is its length if the length is less than the length?"))

    def test_neighbours_of_batch_26_set(self):
        """Set 29: neighbours of the batch-26 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_29 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (twenty-ninth set, neighbours of the batch-26 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (6, 0, 5))

    def test_pages_finishing_and_other_deadlines(self):
        book = "A 100-page book has 20 pages already read. She must finish the book in 6 days. "
        # the forms that stay answered: 80 pages over 6 days is 40/3
        for q in ("How many pages a day must be read?", "How many pages a day must be read to finish?", "How many pages a day must be read to finish it?",
                  "How many pages a day must be read to finish reading the book?", "How many pages a day must be read while finishing the book?"):
            self.assertEqual(answers(book + q), values(Fraction(40, 3)), q)
        self.assertEqual(answers("A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days?"), values(53))
        # "finishing" counts as "finish": the chapter is not the book
        self.assertIsNone(answers(book + "How many pages a day must be read while finishing the chapter?"))
        # today / tomorrow / tonight (and by / before ...) are a deadline of their own, and are not dropped to use the 6 days
        for q in ("How many pages a day must be read to finish it today?", "How many pages a day must be read to finish it by tomorrow?",
                  "How many pages a day must be read to finish it tonight?", "How many pages a day must be read to finish before Friday?"):
            self.assertIsNone(answers(book + q), q)
        # the words after the day count are checked too
        self.assertIsNone(answers("A 331-page book has 13 pages already read. How many pages a day must be read to finish it in 6 days by tomorrow?"))
        self.assertIsNone(answers("A 240-page book has 40 pages already read. How many pages a day must be read to finish it in 8 days by Friday?"))

    def test_rectangle_comparison_with_it_or_one_as_subject(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # the statements that already worked stay
        self.assertEqual(answers(base + "The length is less than the width. What is its length?"), values(2))
        self.assertEqual(answers(base + "The width is more than the length. What is its width?"), values(18))
        self.assertEqual(answers(base + "What is its length if the length is shorter than the width?"), values(2))
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        # "it" and "one" are the side the question asks for
        self.assertEqual(answers(base + "What is its length? It is shorter than the width."), values(2))
        self.assertEqual(answers(base + "It is less than the width. What is its length?"), values(2))
        self.assertEqual(answers(base + "What is its width? It is the longer side."), values(18))
        self.assertEqual(answers(base + "The longer one is the width. What is its width?"), values(18))
        self.assertEqual(answers(base + "The shorter one is the length. What is its length?"), values(2))
        self.assertEqual(answers(base + "The longer one is the length. What is its width?"), values(2))
        self.assertEqual(answers(base + "What is its length if it is shorter than the width?"), values(2))
        self.assertEqual(answers(base + "What is its width if it is longer than the length?"), values(18))
        self.assertEqual(answers(base + "What is its width? It is the narrower side."), values(2))
        # when both sides are asked, or the pronoun compares the side with itself, nothing says which side "it" is: decline
        self.assertIsNone(answers(base + "Find its length and width. It is shorter than the width."))
        self.assertIsNone(answers(base + "It is shorter than the width. Find its length and width."))
        self.assertIsNone(answers(base + "What is its width? It is shorter than the width."))
        # "the same as" / "equal to" says the sides are equal, which a 40 / 36 rectangle is not
        self.assertIsNone(answers(base + "What is its length? It is the same as the width."))
        self.assertIsNone(answers(base + "What is its length? It is equal to the width."))

    def test_finishing_and_it_set(self):
        """Set 30: neighbours of the batch-27 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_30 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirtieth set, neighbours of the batch-27 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 0, 5))

    def test_rectangle_comparison_word_must_compare_the_two_sides(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # comparisons of the two sides stay as they are
        for q, want in (("What is its length? It is more than the width.", 18), ("What is its width? It is more than the length.", 18),
                        ("What is its length? It is shorter than the width.", 2), ("The length is less than the width. What is its length?", 2),
                        ("The width is more than the length. What is its width?", 18), ("What is its width? It is the longer side.", 18),
                        ("The longer one is the width. What is its width?", 18), ("What is its length? It is shorter than the other side.", 2),
                        ("What is its width? It is less than the length.", 2), ("The longer side is the length. What is its length?", 18)):
            self.assertEqual(answers(base + q), values(want), q)
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        self.assertEqual(answers(base + "What is its length?"), values(18))
        # a comparison with anything else is not a comparison of the sides: decline
        for q in ("What is its length? It is shorter than a foot.", "The length is longer than a mile. What is its length?",
                  "What is its width? It is more interesting than the length.", "What is its length? It is less obvious than the width.",
                  "What is its length? One is less certain than the width.", "What is its length? It is shorter than 3 ft.",
                  "What is its length? It is shorter than the width of a door.", "What is its width? It is longer than a tennis court.",
                  "What is its length? It is more beautiful than the width.",
                  "What is its length? It is shorter.", "What is its length? It is longer.",
                  "The width is the smaller of the two sides in a garden. What is its width?"):
            self.assertIsNone(answers(base + q), q)

    def test_rectangle_statement_and_question_in_one_sentence(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # the part before "so / then / therefore / ;" is a statement; naming the width in it does not ask for both sides
        self.assertEqual(answers(base + "The length is shorter than the width, so what is its length?"), values(2))
        self.assertEqual(answers(base + "The width is shorter than the length, so what is its width?"), values(2))
        self.assertEqual(answers(base + "The length is shorter than the width, so what is its width?"), values(18))
        self.assertEqual(answers(base + "The length is shorter than the width; what is its length?"), values(2))
        r = WS.solve(base + "The length is shorter than the width, so find its length and width.")
        self.assertEqual(r.values, [Fraction(2), Fraction(18)])             # both sides asked: the length is the shorter one
        self.assertEqual(2 * r.values[0] + 2 * r.values[1], 40)
        self.assertEqual(r.values[0] * r.values[1], 36)

    def test_comparison_word_set(self):
        """Set 31: neighbours of the batch-28 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_31 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-first set, neighbours of the batch-28 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 0, 5))

    def test_rectangle_clause_hanging_on_the_side_just_named(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # the usual forms stay
        self.assertEqual(answers(base + "The length is shorter than the width, so what is its length?"), values(2))
        self.assertEqual(answers(base + "What is its width? It is the longer side."), values(18))
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        self.assertEqual(answers(base + "What is its length?"), values(18))
        # a "which is ..." clause or an apposition says which side the NAMED side is; it does not ask for the other side
        for q, want in (("What is its length, which is shorter than the width?", 2), ("Find its width, which is the longer side.", 18),
                        ("Find the length, the shorter side.", 2), ("What is its width, the longer one?", 18),
                        ("What is its length, which is the longer side?", 18), ("Find its width, the shorter one.", 2),
                        ("What is its length, the shorter one?", 2), ("Find the length, which is the longer side.", 18),
                        ("What is its length, which is the shorter side?", 2), ("Find its width, which is the longer one.", 18),
                        ("What is its width, the narrower side?", 2), ("Find the length, which is less than the width.", 2),
                        ("What is its length, the longer one?", 18)):
            self.assertEqual(answers(base + q), values(want), q)
        # the clause counts as a statement: when it is not a comparison of the two sides, or compares a side with itself, the problem declines
        for q in ("What is its length, which is shorter than a foot?", "What is its width, which is more interesting than the length?",
                  "What is its length, which is shorter?", "Find its width, which is less than the width.",
                  "What is its width, the longer side of the two?", "What is its width, which is longer than a bus?",
                  "Find its length, which is the shorter side of the lot.", "What is its length, which is shorter than the length?"):
            self.assertIsNone(answers(base + q), q)
        # asking both sides with a phrase after them ("Find its length and width, the longer side.") was read as a statement about the last side named; it declines
        # now (see test_rectangle_both_sides_with_a_trailing_phrase_declines), because the same words give opposite answers when the two names are swapped
        self.assertIsNone(answers(base + "Find its length and width, the longer side."))

    def test_clause_on_the_named_side_set(self):
        """Set 32: neighbours of the batch-29 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_32 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-second set, neighbours of the batch-29 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 0, 3))

    def test_rectangle_both_sides_with_a_trailing_phrase_declines(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # with no phrase after it, "Find its length and width" still returns both
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        self.assertEqual(answers(base + "Find its width and length."), values(2, 18))
        # a phrase after BOTH sides does not say which of the two it describes: "length and width, the longer side" and "width and length, the longer side" would
        # give opposite answers for the same words, so every one of these declines
        for q in ("Find its length and width, the longer side.", "Find its width and length, the longer side.",
                  "Find its length and width, which is the longer side.", "Find its width and length, which is the longer side.",
                  "Find its width and length which is the shorter side.", "Find its length and width the longer one.",
                  "Find its length and width the shorter one.", "Find its length and width, the shorter one."):
            self.assertIsNone(answers(base + q), q)

    def test_rectangle_clause_without_a_comma(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # the comma is optional: the same four sentences as the batch-29 ones, without it
        for q, want in (("What is its length which is shorter than the width?", 2), ("Find its width which is the longer side.", 18),
                        ("Find the length the shorter side.", 2), ("What is its width the longer one?", 18),
                        ("What is its length which is the longer side?", 18), ("Find its width the shorter one.", 2),
                        ("What is its length that is the shorter side?", 2), ("Find the length which is less than the width.", 2),
                        ("What is its width which is the narrower side?", 2)):
            self.assertEqual(answers(base + q), values(want), q)
        # and the same words with a comma still agree
        for q, want in (("What is its length, which is shorter than the width?", 2), ("Find its width, which is the longer side.", 18),
                        ("Find the length, the shorter side.", 2), ("What is its width, the longer one?", 18)):
            self.assertEqual(answers(base + q), values(want), q)
        # a clause that is not a comparison of the two sides declines, with or without the comma
        for q in ("What is its length which is shorter than a foot?", "What is its width which is shorter than the width?",
                  "What is its width which is the longer side of the lot?", "What is its length which is shorter than a house?"):
            self.assertIsNone(answers(base + q), q)

    def test_comma_less_clause_set(self):
        """Set 33: neighbours of the batch-30 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_33 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-third set, neighbours of the batch-30 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 0, 4))

    def test_rectangle_length_of_the_shorter_side(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # the usual forms stay
        self.assertEqual(answers(base + "Find its length and width."), values(2, 18))
        self.assertEqual(answers(base + "What is its length?"), values(18))
        self.assertEqual(answers(base + "What is its width?"), values(2))
        self.assertEqual(answers(base + "What is its length, which is shorter than the width?"), values(2))
        self.assertEqual(answers(base + "Find the length the shorter side."), values(2))
        self.assertIsNone(answers(base + "Find its length and width, the longer side."))
        # "of the shorter side" means the shorter side and "of the longer side" the longer; the word in front of "of" does not switch them
        for q, want in (("Find the length of the shorter side.", 2), ("What is the width of the longer side?", 18),
                        ("What is the length of the longer side?", 18), ("Find the width of the shorter side.", 2),
                        ("Find the length of the shorter one.", 2), ("What is the length of the narrower one?", 2)):
            self.assertEqual(answers(base + q), values(want), q)
        # a phrase that does not END on the comparison declines, it does not fall back to the usual side
        for q in ("What is its width, the longer side of the rectangle?", "What is its width, the longer side of the lot?",
                  "What is its length, the shorter side of the rectangle?", "What is its length, the shorter side of the plot?",
                  "Find the length of the shorter side of the rectangle.", "Find the width of the longer side of the garden.",
                  "Find the length of the shorter side and the width.", "Find the length of the longer side and the width.",
                  "What is the longer side?"):
            self.assertIsNone(answers(base + q), q)

    def test_rectangle_clause_in_the_middle_of_the_question(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # the length is named and then called the shorter side: that assignment stands even though the width is asked afterwards
        for q in ("What is its length, the shorter side, and its width?", "Find the length, the shorter side, and the width.",
                  "What is its width, the longer side, and its length?", "What is its length, which is shorter than the width, and its width?"):
            r = WS.solve(base + q)
            self.assertEqual(r.values, [Fraction(2), Fraction(18)], q)                 # [length, width]
            self.assertEqual(2 * r.values[0] + 2 * r.values[1], 40)
            self.assertEqual(r.values[0] * r.values[1], 36)
        # a second statement in the same question is more than one clause can handle: decline
        self.assertIsNone(answers(base + "What is its length, the shorter side, and its width, the longer side?"))

    def test_length_of_side_and_clause_set(self):
        """Set 34: neighbours of the batch-31 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_34 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-fourth set, neighbours of the batch-31 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 0, 3))

    def test_rectangle_question_without_find_or_what(self):
        base = "A rectangle has a perimeter of 40 ft and an area of 36 ft². "
        # these raised TypeError (there was no "find" or "what" sentence, so the question was None); they are answered now
        for q, want in (("How long is the shorter side?", (2,)), ("How wide is the longer side?", (18,)), ("How long is the longer side?", (18,)),
                        ("How wide is the shorter side?", (2,)), ("Calculate the sides.", (2, 18)), ("Compute its length and width.", (2, 18)),
                        ("Please give the sides.", (2, 18)), ("List the dimensions.", (2, 18))):
            self.assertEqual(answers(base + q), values(*want), q)
        # a question the solver does not recognise declines; it must not raise
        for q in ("The sides please.", "Sides?", "How long is it?", "How wide is it?", "How many sides does it have?", "How long is the side?",
                  "How long is the shorter side of the lot?", "How long is the shorter side, and how wide is the longer side?", "Tell me the sides.", "The rectangle.", ""):
            self.assertIsNone(answers(base + q), q)
        for text in ("A rectangle has a perimeter of 40 ft and an area of 36 ft².", "A rectangle has a perimeter of 40 ft and an area of 36 ft²", "", " ", "How long is the shorter side?"):
            self.assertIsNone(answers(text), text)

    def test_no_family_ever_raises(self):
        """solve() swallows ZeroDivisionError, ValueError, KeyError and IndexError, so a TypeError (a None where a string was expected) escaped it and crashed the caller.
        Every family is called DIRECTLY (not through solve) on the hand-written problems, every fresh set, and cut-up versions of them (the question removed, the first
        sentence removed, half the text, no digits, upper case): none may raise."""
        import glob
        import importlib
        import os
        import algebra_matcher as AM

        def variants(text):
            sents = [x for x in re.split(r"(?<=[.?!])\s+", text.strip()) if x]
            out = {text, text.replace("?", "").replace(".", ""), text.upper(), text[: len(text) // 2], text[len(text) // 2:], "", re.sub(r"\d", "", text), text.replace(",", "")}
            if len(sents) > 1:
                out.update((" ".join(sents[:-1]), " ".join(sents[1:]), sents[-1], sents[0]))
            return out
        here = os.path.dirname(os.path.abspath(__file__))
        problems = [t for t, _ in AM.HAND_TEST + AM.FRESH_TEST]
        for path in sorted(glob.glob(os.path.join(here, "fresh_word_problems*.py"))):
            problems += [p for p, _ in importlib.import_module(os.path.basename(path)[:-3]).FRESH]
        raised = []
        for p in problems:
            for v in variants(p):
                for fam in WS.FAMILIES:
                    try:
                        fam(v)
                    except Exception as e:                                         # any error at all, not only the four solve() swallows
                        raised.append((fam.__name__, type(e).__name__, v[:80]))
        self.assertEqual(raised[:5], [])

    def test_question_without_find_set(self):
        """Set 35: neighbours of the batch-32 crash, written after the fix was finished and run once, untuned."""
        from fresh_word_problems_35 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-fifth set, neighbours of the batch-32 crash): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 0, 4))

    def test_temperature_whole_hours(self):
        t = "The temperature is %s°F and %s %s°F per hour. For how many whole hours will it stay %s %s°F?"
        self.assertEqual(answers(t % ("26", "falling", "3", "at or above", "1")), values(8))
        self.assertEqual(answers(t % ("15", "falling", "2", "at or above", "8")), values(3))
        self.assertEqual(answers(t % ("16", "falling", "3", "at or above", "-8")), values(8))                 # a negative limit
        r = WS.solve(t % ("26", "falling", "3", "at or above", "1"))
        self.assertEqual(r.values, [Fraction(8)])
        self.assertIn("26 - 3h >= 1", r.reading)
        self.assertIn("after 8 hours it is 2°F, after 9 it is -1°F", r.reading)                       # 8 hours is still at or above 1, 9 is not
        for h, T0, rate, L in ((8, 26, 3, 1), (3, 15, 2, 8), (1, 29, 4, 22), (8, 16, 3, -8)):                  # the answer is the LAST whole hour at or above the limit
            self.assertGreaterEqual(T0 - rate * h, L)
            self.assertLess(T0 - rate * (h + 1), L)
        # "at or above" includes the limit and "above" does not: 25 - 3 * 8 = 1 lands exactly on 1 at hour 8
        self.assertEqual(answers(t % ("25", "falling", "3", "at or above", "1")), values(8))
        self.assertEqual(answers(t % ("25", "falling", "3", "above", "1")), values(7))
        self.assertEqual(answers(t % ("16", "falling", "3", "above", "-8")), values(7))
        self.assertEqual(answers(t % ("26", "falling", "3", "above", "1")), values(8))                        # no whole-hour landing on 1: same answer
        # a rising temperature, "at or below" / "below", a limit above the start or equal to it, a zero rate, another scale, another unit asked, no question for hours
        for args in (("26", "rising", "3", "at or above", "1"), ("26", "falling", "3", "at or below", "1"), ("26", "falling", "3", "below", "1"),
                     ("26", "falling", "3", "at or above", "30"), ("1", "falling", "3", "at or above", "1"), ("26", "falling", "0", "at or above", "1")):
            self.assertIsNone(answers(t % args), args)
        self.assertIsNone(answers("The temperature is 26°F and falling 3°C per hour. For how many whole hours will it stay at or above 1°F?"))
        self.assertIsNone(answers("The temperature is 26°F and falling 3°F per hour. For how many minutes will it stay at or above 1°F?"))
        self.assertIsNone(answers("The temperature is 26°F and falling 3°F per hour. What will it be after 4 hours?"))
        self.assertIsNone(answers("The temperature is 26°F and falling 3°F per hour for part of the night. For how many whole hours will it stay at or above 1°F?"))

    def test_two_candles_equal(self):
        c = "One candle is %s cm tall and burns %s cm per hour. Another is %s cm tall and burns %s cm per hour. %s"
        self.assertEqual(answers(c % ("13", "2", "22", "4", "When will they be the same height?")), values(Fraction(9, 2)))
        self.assertEqual(answers(c % ("30", "1.5", "38", "3.5", "When will they be the same height?")), values(4))
        self.assertEqual(answers(c % ("22", "4", "13", "2", "When will they be the same height?")), values(Fraction(9, 2)))          # either candle first
        r = WS.solve(c % ("13", "2", "22", "4", "When will they be the same height?"))
        self.assertIn("13 - 2t = 22 - 4t", r.reading)
        self.assertIn("t = 9/2 hours", r.reading)
        self.assertEqual(Fraction(13) - 2 * r.values[0], Fraction(22) - 4 * r.values[0])                                      # the heights really are equal ...
        self.assertGreater(Fraction(13) - 2 * r.values[0], 0)                                                                 # ... and still above 0
        # the answer is the time: a question for the height declines; one that would burn out first declines; equal rates, no meeting in the future
        for args in (("13", "2", "22", "4", "How tall will they be when they are the same height?"), ("13", "2", "22", "4", "When will they burn out?"),
                     ("6", "3", "24", "9", "When will they be the same height?"), ("4", "2", "20", "8", "When will they be the same height?"),
                     ("10", "5", "12", "6", "When will they be the same height?"),        # both reach 0 exactly when they meet: not above 0
                     ("13", "2", "20", "2", "When will they be the same height?"), ("13", "2", "10", "4", "When will they be the same height?"),
                     ("13", "4", "22", "2", "When will they be the same height?"),
                     ("13", "2", "22", "4", "How long until they are the same height for part of the night?")):
            self.assertIsNone(answers(c % args), args)

    def test_transversal_equal_angles(self):
        x = "Two parallel lines are cut by a transversal. A pair of %s angles measure (%s)° and (%s)°. %s"
        self.assertEqual(answers(x % ("alternate exterior", "2x + 24", "1x + 49", "Find x and the angle.")), values(25, 74))
        self.assertEqual(answers(x % ("corresponding", "4x + 4", "6x − 54", "Find x and the angle.")), values(29, 120))
        self.assertEqual(answers(x % ("alternate interior", "2x + 24", "1x + 49", "Find the angle.")), values(74))           # "Find the angle" returns the angle alone
        self.assertEqual(answers(x % ("alternate interior", "2x + 24", "1x + 49", "Find x.")), values(25))
        r = WS.solve(x % ("alternate exterior", "2x + 24", "1x + 49", "Find x and the angle."))
        self.assertEqual(r.values, [Fraction(25), Fraction(74)])                                                              # x first, then the angle
        self.assertIn("2x + 24 = 1x + 49", r.reading)
        self.assertIn("x = 25 and each angle is 74 degrees", r.reading)
        # same-side (consecutive) interior angles ADD to 180, they are not equal: decline.  Also equal slopes, an angle over 180 or not positive, "both angles", a sum asked
        for args in (("same-side interior", "2x + 24", "1x + 49", "Find x and the angle."), ("consecutive interior", "2x + 24", "1x + 49", "Find x and the angle."),
                     ("alternate exterior", "2x + 24", "2x + 49", "Find x and the angle."), ("alternate exterior", "2x + 100", "1x + 200", "Find x and the angle."),
                     ("alternate exterior", "2x + 24", "1x - 100", "Find x and the angle."), ("alternate exterior", "2x + 24", "1x + 49", "Find both angles."),
                     ("alternate exterior", "2x + 24", "1x + 49", "Find the sum of the angles.")):
            self.assertIsNone(answers(x % args), args)
        self.assertIsNone(answers("A transversal cuts two lines. A pair of alternate exterior angles measure (2x + 24)° and (1x + 49)°. Find x and the angle."))   # the lines are not parallel

    def test_checker_expects_x_and_the_angle_when_both_are_asked(self):
        """The stored answer "x = 25; each angle is 74 degrees" is compared by the checker: for "Find the angle." it keeps only the angle; for "Find x and the angle."
        it keeps both numbers; for "Find x." only x."""
        stored = "x = 25; each angle is 74°"
        self.assertEqual(GroundTruth.numbers_of(stored, "Two parallel lines are cut by a transversal. A pair of alternate exterior angles measure (2x + 24)° and (1x + 49)°. Find x and the angle."), values(25, 74))
        self.assertEqual(GroundTruth.numbers_of(stored, "Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle."), values(74))
        self.assertEqual(GroundTruth.numbers_of(stored, "Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. Find x."), values(25))
        self.assertEqual(GroundTruth.numbers_of(stored), values(74))                                                          # no problem text: the old behaviour

    def test_temperature_candles_transversal_set(self):
        """Set 36: wordings for temperature_whole_hours, two_candles_equal and transversal_equal_angles, written after all three were finished and run once, untuned."""
        from fresh_word_problems_36 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-sixth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (6, 0, 6))

    def test_temperature_needs_whole_or_full_hours(self):
        t = "The temperature is 26°F and falling 3°F per hour. For how many %s will it stay at or above 1°F?"
        # "whole hours" and "full hours" are 8; plain "how many hours" would be the continuous 25/3 hours, which is not a whole number of hours: decline
        self.assertEqual(answers(t % "whole hours"), values(8))
        self.assertEqual(answers(t % "full hours"), values(8))
        for w in ("hours", "complete hours", "hours in a row"):
            self.assertIsNone(answers(t % w), w)
        self.assertEqual(answers("The temperature is 30°F and falling 4°F per hour. For how many full hours will it stay at or above 5°F?"), values(6))
        self.assertIsNone(answers("The temperature is 30°F and falling 4°F per hour. For how many hours will it stay at or above 5°F?"))

    def test_candle_question_must_be_about_the_candles(self):
        c = "One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour. "
        # the time question about the candles stays 9/2 hours, in each form
        for q in ("When will they be the same height?", "How long until they are the same height?", "After how many hours will they be the same height?"):
            self.assertEqual(answers(c + q), values(Fraction(9, 2)), q)
        self.assertEqual(answers("When will they be the same height? One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour."), values(Fraction(9, 2)))
        self.assertEqual(answers("One candle is 13 cm tall and burns 2 cm per hour, and another is 22 cm tall and burns 4 cm per hour. When will they be the same height?"), values(Fraction(9, 2)))
        self.assertEqual(answers("One candle is 13 cm tall and burns 2 cm per hour, another is 22 cm tall and burns 4 cm per hour; when will they be the same height?"), values(Fraction(9, 2)))
        # a different question after the statements declines, even when "when they are the same height" is tucked into a statement
        self.assertIsNone(answers("One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour when they are the same height. How old is the room?"))
        self.assertIsNone(answers(c + "They were the same height yesterday. When will the power return?"))
        self.assertIsNone(answers(c + "They were the same height yesterday. When will they be the same height?"))      # a second mention of "same height" is another event
        self.assertIsNone(answers(c + "How old is the room?"))
        self.assertIsNone(answers(c + "When will the power return?"))
        self.assertIsNone(answers(c + "When will they burn out?"))
        self.assertIsNone(answers(c + "How tall will they be when they are the same height?"))

    def test_temperature_and_candle_neighbours_set(self):
        """Set 37: neighbours of the batch-34 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_37 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-seventh set, neighbours of the batch-34 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (4, 0, 5))

    def test_candles_same_height_as_what(self):
        c = "One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour. "
        # the candles matched with each other: 9/2 hours, at 4 cm
        for q in ("When will they be the same height?", "When will they be the same height as each other?", "When will they be the same height as one another?",
                  "When will one be the same height as the other?", "When will they be the same height as the other candle?", "When will they be the same height to each other?"):
            self.assertEqual(answers(c + q), values(Fraction(9, 2)), q)
        r = WS.solve(c + "When will they be the same height as each other?")
        self.assertIn("t = 9/2 hours (both candles are still 4 cm tall)", r.reading)
        # the same height as the table (a door, the bookshelf, the wall ...): the other height is not given, so it declines, and so does a third thing added after "each other"
        for q in ("When will they be the same height as the table?", "When will they be the same height as a door?", "How long until they are the same height as the table?",
                  "When will they be the same height as each other and the table?", "When will they be the same height as the bookshelf?",
                  "When will they be the same height as each other and the wall?"):
            self.assertIsNone(answers(c + q), q)

    def test_candles_second_sentence_that_asks(self):
        c = "One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour. "
        # a request without a question word is a question too: another sentence that asks its own question declines
        for pre in ("Find the age of the room. ", "Determine the room's age. ", "Calculate the cost. ", "Tell me the time. ", "Find when they will be the same height. ",
                    "Determine the height of the room. ", "Find the price of the candles. "):
            self.assertIsNone(answers(pre + c + "When will they be the same height?"), pre)
        self.assertIsNone(answers(c + "Find the age of the room. When will they be the same height?"))
        # a sentence that asks nothing is harmless
        for pre in ("The room is old. ", "It is dark. "):
            self.assertEqual(answers(pre + c + "When will they be the same height?"), values(Fraction(9, 2)), pre)
        # "Find when ..." as the ONE question stays answered
        self.assertEqual(answers(c + "Find when they will be the same height."), values(Fraction(9, 2)))

    def test_candles_as_what_set(self):
        """Set 38: neighbours of the batch-35 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_38 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-eighth set, neighbours of the batch-35 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (3, 0, 4))

    def test_class_ratio_after_join(self):
        r_ = "The ratio of boys to girls in a class is %s. After %s more %s join, the ratio becomes %s. %s"
        q = "How many students were there originally?"
        self.assertEqual(answers(r_ % ("3:8", "4", "girls", "1:3", q)), values(44))
        self.assertEqual(answers(r_ % ("6:3", "6", "girls", "8:5", q)), values(72))
        self.assertEqual(answers(r_ % ("5:4", "2", "girls", "7:6", q)), values(63))
        res = WS.solve(r_ % ("3:8", "4", "girls", "1:3", q))
        self.assertIn("3k / (8k + 4) = 1/3", res.reading)
        self.assertIn("k = 4: 12 boys and 32 girls at first, 44 in all", res.reading)
        # the 4 girls joined the girls: with 12 boys and 32 girls the new ratio really is 1:3
        self.assertEqual(Fraction(12) / (Fraction(32) + 4), Fraction(1, 3))
        self.assertEqual(answers(r_ % ("3:4", "6", "girls", "1:2", q)), values(21))                      # 9 boys and 12 girls
        self.assertEqual(answers(r_ % ("3:8", "5", "girls", "1:3", q)), values(55))
        # boys joining are added to the boys: (b k + n) / (g k) = p / q
        self.assertEqual(answers("The ratio of boys to girls in a class is 2:3. After 4 more boys join, the ratio becomes 1:1. How many students were there originally?"), values(20))
        # the newcomers are not the named groups, the ratio does not change or gives no positive whole counts, a question for boys or for the total now, leaving, reversed order, part of the year
        for text in (r_ % ("3:8", "4", "dogs", "1:3", q), r_ % ("3:8", "4", "boys", "1:3", q), r_ % ("3:8", "4", "girls", "3:8", q), r_ % ("3:8", "4", "girls", "1:2", q),
                     r_ % ("3:8", "4", "girls", "1:3", "How many boys were there originally?"), r_ % ("3:8", "4", "girls", "1:3", "How many students are there now?"),
                     r_ % ("3:8", "4", "girls", "1:3", "How many students were there originally for part of the year?"),
                     "The ratio of boys to girls in a class is 3:8. After 4 more girls leave, the ratio becomes 1:3. How many students were there originally?",
                     "The ratio of boys to girls in a class is 3:8. After 4 more girls join, the ratio of girls to boys becomes 3:1. How many students were there originally?"):
            self.assertIsNone(answers(text), text)

    def test_kinematics_time(self):
        k = "Using v = u + at, how long does it take an object to go from %s to %s with acceleration %s?"
        self.assertEqual(answers(k % ("0 m/s", "30 m/s", "5 m/s²")), values(6))
        self.assertEqual(answers(k % ("7 m/s", "11 m/s", "4 m/s²")), values(1))
        self.assertEqual(answers(k % ("5 m/s", "21 m/s", "2 m/s²")), values(8))
        self.assertEqual(answers(k % ("0 m/s", "30 m/s", "5 m/s^2")), values(6))
        self.assertEqual(answers(k % ("0 ft/s", "30 ft/s", "5 ft/s²")), values(6))
        self.assertEqual(answers(k % ("0 km/h", "30 km/h", "5 km/h²")), values(6))                    # one system of units: hours here
        res = WS.solve(k % ("0 m/s", "30 m/s", "5 m/s²"))
        self.assertIn("0 + 5t = 30", res.reading)
        self.assertIn("t = (30 - 0) / 5 = 6 seconds", res.reading)
        res = WS.solve(k % ("0 m/s", "31 m/s", "5 m/s²"))
        self.assertEqual(res.values, [Fraction(31, 5)])                                                    # exact
        # an acceleration of 0, a speed that goes down (a negative time), speed and acceleration in different systems, another time unit, a different question
        for args in (("0 m/s", "30 m/s", "0 m/s²"), ("30 m/s", "0 m/s", "5 m/s²"), ("7 m/s", "7 m/s", "5 m/s²"), ("0 m/s", "30 m/s", "5 km/h²"),
                     ("0 km/h", "30 km/h", "5 m/s²"), ("0 m/s", "30 km/h", "5 m/s²")):
            self.assertIsNone(answers(k % args), args)
        self.assertIsNone(answers("Using v = u + at, how many minutes does it take an object to go from 0 m/s to 30 m/s with acceleration 5 m/s²?"))
        self.assertIsNone(answers("Using v = u + at, how fast is an object after 5 seconds from 0 m/s with acceleration 5 m/s²?"))

    def test_pipes_and_drain(self):
        p = "Pipe A fills a pool in %s hours, pipe B in %s hours, and a drain empties it in %s hours. %s"
        q = "With all three open, how long does it take to fill the pool?"
        self.assertEqual(answers(p % ("4", "5", "20", q)), values(Fraction(5, 2)))
        self.assertEqual(answers(p % ("4", "5", "10", q)), values(Fraction(20, 7)))
        self.assertEqual(answers(p % ("4", "20", "5", q)), values(10))
        res = WS.solve(p % ("4", "5", "20", q))
        self.assertIn("1/4 + 1/5 - 1/20 = 2/5 of the pool per hour", res.reading)                         # the drain's rate is subtracted
        self.assertIn("1 / 2/5 = 5/2 hours", res.reading)
        self.assertEqual(Fraction(1, 4) + Fraction(1, 5) - Fraction(1, 20), Fraction(2, 5))
        self.assertEqual(answers("Tap A fills a tub in 10 minutes, tap B in 15 minutes, and a leak empties it in 30 minutes. With all three open, how long does it take to fill the tub?"), values(Fraction(15, 2)))
        # the three together do not fill the pool (the drain keeps up), the pool is asked to EMPTY, the question does not say all open, mixed units, only some open, part of the year
        for text in (p % ("4", "5", "2", q), p % ("6", "3", "2", q),
                     p % ("4", "5", "20", "With all three open, how long does it take to empty the pool?"),
                     p % ("4", "5", "20", "How long does it take to fill the pool?"),
                     p % ("4", "5", "20", "With pipe A open, how long does it take to fill the pool?"),
                     p % ("4", "5", "20", "With all three open, how long does it take to fill the pool for part of the year?"),
                     "Pipe A fills a pool in 4 hours, pipe B in 5 minutes, and a drain empties it in 20 hours. With all three open, how long does it take to fill the pool?",
                     "Pipe A fills a pool in 4 hours and a drain empties it in 20 hours. With both open, how long does it take to fill the pool?"):
            self.assertIsNone(answers(text), text)

    def test_ratio_kinematics_pipes_set(self):
        """Set 39: wordings for class_ratio_after_join, kinematics_time and pipes_and_drain, written after all three were finished and run once, untuned.
        One answer is declined (a safe miss): "animals" is not one of the nouns for a total of students."""
        from fresh_word_problems_39 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (thirty-ninth set, three families): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (5, 1, 6))

    def test_class_ratio_question_must_say_originally(self):
        base = "The ratio of boys to girls in a class is 3:8. After 4 more girls join, the ratio becomes 1:3. "
        # the question that says originally (or at first / to begin with) stays 44
        for q in ("How many students were there originally?", "How many students were there at first?", "How many students were there to begin with?", "Originally, how many students were there?"):
            self.assertEqual(answers(base + q), values(44), q)
        # the class now has 12 + 32 + 4 = 48 students; "now" is not the original total
        self.assertIsNone(answers(base + "How many students are there now?"))
        self.assertIsNone(answers("Originally there were some. After 4 more girls join, the ratio becomes 1:3. How many students are there now?"))
        self.assertIsNone(answers("The ratio of boys to girls in a class is 3:8. Originally there were some students. After 4 more girls join, the ratio becomes 1:3. How many students are there now?"))
        # two questions make the problem ask two things
        self.assertIsNone(answers(base + "How many students were there originally? How many are there now?"))
        self.assertIsNone(answers(base + "How many are there now? How many students were there originally?"))
        self.assertIsNone(answers(base + "How many students were there originally, and how many are there now?"))

    def test_pipes_the_drain_must_be_open_too(self):
        base = "Pipe A fills a pool in 4 hours, pipe B in 5 hours, and a drain empties it in 20 hours. "
        # everything open, the drain included: 5/2 hours
        for q in ("With all three open, how long does it take to fill the pool?", "With all three running, how long does it take to fill the pool?",
                  "All three are open. How long does it take to fill the pool?", "With everything open, how long does it take to fill the pool?",
                  "The pipes and the drain are all open. How long does it take to fill the pool?", "The pipes and the drain are open together. How long does it take to fill the pool?",
                  "With both pipes and the drain open, how long does it take to fill the pool?", "All open, how long does it take to fill the pool?",
                  "How long does it take to fill the pool with all three open?"):
            self.assertEqual(answers(base + q), values(Fraction(5, 2)), q)
        # "The pipes work together" does not open the drain: the two pipes alone take 1 / (1/4 + 1/5) = 20/9 hours, a different problem
        self.assertEqual(Fraction(1) / (Fraction(1, 4) + Fraction(1, 5)), Fraction(20, 9))
        for q in ("The pipes work together. How long does it take to fill the pool?", "The pipes work together at the same time. How long does it take to fill the pool?",
                  "Both pipes are open. How long does it take to fill the pool?", "Both pipes are open at the same time. How long does it take to fill the pool?",
                  "Both pipes work at once. How long does it take to fill the pool?"):
            self.assertIsNone(answers(base + q), q)

    def test_class_ratio_and_pipes_neighbours_set(self):
        """Set 40: neighbours of the batch-37 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_40 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (fortieth set, neighbours of the batch-37 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (3, 0, 4))

    def test_pipes_all_must_be_the_three_devices(self):
        base = "Pipe A fills a pool in 4 hours, pipe B in 5 hours, and a drain empties it in 20 hours. "
        # "all" that is the pipes and the drain: 5/2 hours
        for q in ("With all three open, how long does it take to fill the pool?", "The pipes and the drain are open. How long does it take to fill the pool?",
                  "The pipes and the drain are all open. How long does it take to fill the pool?", "All three are open. How long does it take to fill the pool?",
                  "All of them are open. How long does it take to fill the pool?", "With everything open, how long does it take to fill the pool?",
                  "All open, how long does it take to fill the pool?", "How long does it take to fill the pool with all three open?"):
            self.assertEqual(answers(base + q), values(Fraction(5, 2)), q)
        # "all together" or "all on" said of something else opens nothing: the two pipes alone take 20/9 hours, and the lights do not open the drain
        self.assertEqual(Fraction(1) / (Fraction(1, 4) + Fraction(1, 5)), Fraction(20, 9))
        for q in ("The pipes are all together. How long does it take to fill the pool?", "The lights are all on. How long does it take to fill the pool?",
                  "The pipes are all open. How long does it take to fill the pool?", "The pipes work together. How long does it take to fill the pool?",
                  "All on. How long does it take to fill the pool?", "Everything is on. How long does it take to fill the pool?",
                  "The taps are all together. How long does it take to fill the pool?", "The lamps are all on. How long does it take to fill the pool?"):
            self.assertIsNone(answers(base + q), q)

    def test_class_ratio_one_how_many(self):
        base = "The ratio of boys to girls in a class is 3:8. After 4 more girls join, the ratio becomes 1:3. "
        self.assertEqual(answers(base + "How many students were there originally?"), values(44))
        # the boys were 12: a second "how many" in the same sentence asks for them too, so the problem asks two things
        for q in ("How many students were there originally and how many boys?", "How many students were there originally, and how many boys were there?",
                  "How many students were there originally and how many girls?", "How many students were there originally? How many boys?",
                  "How many boys and girls were there originally?", "How many were there originally?"):
            self.assertIsNone(answers(base + q), q)

    def test_all_and_second_how_many_set(self):
        """Set 41: neighbours of the batch-38 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_41 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (forty-first set, neighbours of the batch-38 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (3, 0, 5))

    def test_pipes_all_three_must_be_open_not_stopped(self):
        base = "Pipe A fills a pool in 4 hours, pipe B in 5 hours, and a drain empties it in 20 hours. "
        ask = " How long does it take to fill the pool?"
        # the three devices said to be open, running or working: 5/2 hours
        for q in ("With all three open, how long does it take to fill the pool?", "All three are open." + ask, "All three are running." + ask,
                  "With all of them open, how long does it take to fill the pool?", "The pipes and the drain are open." + ask, "The pipes and the drain are all open." + ask,
                  "The pipes and the drain are open together." + ask, "With both pipes and the drain open, how long does it take to fill the pool?",
                  "All open, how long does it take to fill the pool?", "How long does it take to fill the pool with all three open?",
                  "With everything open, how long does it take to fill the pool?", "All three are working." + ask, "All the pipes and the drain are running." + ask,
                  "All three are flowing." + ask):
            self.assertEqual(answers(base + q), values(Fraction(5, 2)), q)
        # "all three" is only a count: stopped, off, broken, negated, or not about the pipes at all do not turn the drain on
        for q in ("All three are stopped." + ask, "Both pipes and the drain are off." + ask, "All the pipes and the drain are broken." + ask,
                  "Not all three are open." + ask, "The job uses all three hours of the morning." + ask, "I like all of them." + ask,
                  "All three are not open." + ask, "All three are open except the drain." + ask, "With all three open but the drain blocked, how long does it take to fill the pool?",
                  "All three aren't open." + ask, "All three are clogged." + ask, "All three are idle." + ask, "All three are jammed." + ask,
                  "The class has all three students." + ask, "Everything is open except the drain." + ask, "Both pipes and the drain are closed." + ask,
                  "The pipes work together." + ask, "The pipes are all together." + ask, "The lights are all on." + ask, "The pipes are all open." + ask):
            self.assertIsNone(answers(base + q), q)

    def test_three_devices_open_set(self):
        """Set 42: neighbours of the batch-39 fixes, written after the fixes were finished and run once, untuned."""
        from fresh_word_problems_42 import FRESH
        solved, declined, required = score(FRESH)
        print("  fresh wordings (forty-second set, neighbours of the batch-39 fixes): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (solved, solved + declined, declined, required, required))
        self.assertEqual((solved, declined, required), (3, 0, 6))

    def test_pipes_sealed_capped_plugged_and_the_all_that_is_not_the_devices(self):
        base = "Pipe A fills a pool in 4 hours, pipe B in 5 hours, and a drain empties it in 20 hours. "
        ask = " How long does it take to fill the pool?"
        # the forms that stay answered: 5/2 hours, including a bare "All open," at the start of the question and "With all open"
        for q in ("All open, how long does it take to fill the pool?", "With all open, how long does it take to fill the pool?", "All open." + ask,
                  "With all three open, how long does it take to fill the pool?", "All three are open." + ask, "All three are running." + ask,
                  "With all of them open, how long does it take to fill the pool?", "The pipes and the drain are open." + ask,
                  "With both pipes and the drain open, how long does it take to fill the pool?", "How long does it take to fill the pool with all three open?"):
            self.assertEqual(answers(base + q), values(Fraction(5, 2)), q)
        # a sealed, capped, plugged (covered, locked, bolted, disabled ...) drain is shut
        for q in ("All three are open but the drain is sealed." + ask, "All three are open but the drain is capped." + ask, "All three are open but the drain is plugged." + ask,
                  "All three are open but the drain is covered." + ask, "All three are open but the drain is bolted." + ask, "All three are locked." + ask, "All three are disabled." + ask):
            self.assertIsNone(answers(base + q), q)
        # that "all open" is the pool, not the three devices: it has to start the sentence (or follow "with") and end there
        for q in ("The pool, all open to swimmers, is in use." + ask, "The pool, all open, is in use." + ask, "The pool is all open to swimmers." + ask,
                  "All open to swimmers." + ask, "With all open to swimmers, how long does it take to fill the pool?"):
            self.assertIsNone(answers(base + q), q)

    def test_pipes_nothing_else_may_be_said_about_the_drain(self):
        """Fresh set 43 found a real hole: "All three are open but the drain is covered." was answered 12/5.  A list of shut-words is whack-a-mole, so the rule is general now:
        a contrast word (but / however / although / though / yet / unless / except) declines, and any sentence that talks about the drain without giving its time may only be
        the "everything is open" phrase itself, with nothing else about the drain left in it."""
        base = "Pipe A fills a pool in 4 hours, pipe B in 5 hours, and a drain empties it in 20 hours. "
        ask = " How long does it take to fill the pool?"
        for q in ("All three are open. The drain is covered." + ask, "All three are open, however the drain is plugged." + ask, "All three are open although the drain is half shut." + ask,
                  "All three are open. The drain is pinched." + ask, "All three are open. The outlet is jammed." + ask, "All three are open. The drain has a lid." + ask,
                  "All three are open yet the drain does not work." + ask, "The drain is covered. All three are open." + ask, "All three are open and the drain is full of leaves." + ask,
                  "All three are open and the drain is silted up." + ask, "All three are open. The drain has a grate on it." + ask, "All three are open. The leak is pinched shut." + ask,
                  "All three are open though the drain is jammed." + ask, "The outlet is small. All three are open." + ask):
            self.assertIsNone(answers(base + q), q)
        # the phrase itself still carries the drain's name: "the pipes and the drain are open", "with both pipes and the drain open"
        self.assertEqual(answers(base + "The pipes and the drain are open." + ask), values(Fraction(5, 2)))
        self.assertEqual(answers(base + "With both pipes and the drain open, how long does it take to fill the pool?"), values(Fraction(5, 2)))
        self.assertEqual(answers(base + "All the pipes and the drain are running." + ask), values(Fraction(5, 2)))

    def test_drain_state_sets(self):
        """Fresh set 43 (7 wordings) found one WRONG answer ("the drain is covered") before the general rule, so it is a development set: 2 solved, 5 required declines now.
        Set 44 (9 wordings) was written after the general rule and run once, untuned: 2 solved, 7 required declines, 0 wrong."""
        from fresh_word_problems_43 import FRESH as F43
        from fresh_word_problems_44 import FRESH as F44
        s43, s44 = score(F43), score(F44)
        print("  development wordings (forty-third set, found one wrong answer, now fixed): %d solved, %d declined, %d required declines correct" % s43)
        print("  fresh wordings (forty-fourth set, written after the general rule): %d of the %d with an answer solved, %d declined (safe), 0 wrong; %d of %d required declines correct"
              % (s44[0], s44[0] + s44[1], s44[1], s44[2], s44[2]))
        self.assertEqual(s43, (2, 0, 5))
        self.assertEqual(s44, (2, 0, 7))

    def test_pipes_the_time_clause_ends_the_sentence_and_nothing_else_goes_on(self):
        """"A drain empties it in 12 hours and is pinched." and "... and is full of leaves." were answered 12/5, and so was "Water also leaves through a crack." (another way out
        with no rate).  The time clause has to END its sentence, and a sentence that gives no time, asks nothing and does not open the devices declines the problem."""
        base = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours"
        ask = " How long does it take to fill the tank?"
        self.assertEqual(answers(base + ". All three are open." + ask), values(Fraction(12, 5)))             # the time clause ends there
        self.assertEqual(answers(base + ". With all three open, how long does it take to fill the tank?"), values(Fraction(12, 5)))
        for q in (base + " and is pinched. All three are open." + ask, base + " and is full of leaves. All three are open." + ask,
                  base + ", and it is old. All three are open." + ask,
                  base + ". All three are open. Water also leaves through a crack." + ask, base + ". Water also leaves through a crack. All three are open." + ask,
                  base + ". All three are open. Rain also falls in." + ask):
            self.assertIsNone(answers(q), q)

    def test_pipes_time_clause_set(self):
        """Set 45 (9 wordings) was written after the batch-41 fixes and run once, untuned: 2 solved, 7 required declines, 0 wrong."""
        from fresh_word_problems_45 import FRESH
        self.assertEqual(score(FRESH), (2, 0, 7))

    def test_pipes_the_open_statement_and_the_question_carry_nothing_else(self):
        """The same extra water got through when it was said INSIDE the "all open" sentence or the question: "All three are open and water also leaves through a crack." and
        "... how long does it take to fill the tank if water also leaves through a crack?" were answered 12/5.  What is left of the statement once the open phrase is taken out may
        only be small filler words, and the question may not hang a clause on (if / when / while / and / also / as ...)."""
        base = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. "
        ask = " How long does it take to fill the tank?"
        for q in ("All three are open." + ask, "With all three open, how long does it take to fill the tank?", "All three are open, how long does it take to fill the tank?",
                  "How long does it take to fill the tank with all three open?", "All three are open together." + ask):
            self.assertEqual(answers(base + q), values(Fraction(12, 5)), q)
        for q in ("All three are open and water also leaves through a crack." + ask,
                  "All three are open. How long does it take to fill the tank if water also leaves through a crack?",
                  "With all three open, how long does it take to fill the tank if rain also falls in?",
                  "How long does it take to fill the tank with all three open and rain falling in?",
                  "All three are open while it is raining." + ask):
            self.assertIsNone(answers(base + q), q)

    def test_pipes_open_statement_set(self):
        """Set 46 (9 wordings) was written after the batch-42 fixes and run once, untuned: 3 solved, 6 required declines, 0 wrong."""
        from fresh_word_problems_46 import FRESH
        self.assertEqual(score(FRESH), (3, 0, 6))

    def test_pipes_the_question_ends_once_it_names_what_is_filled(self):
        """Extra water said in a phrase the batch-42 list did not hold still got through: "How long does it take to fill the tank during a storm / under a downpour / amid the rain?"
        was answered 12/5.  Once the question has named the tank, the pool or the tub, it has to END (only up / completely / the / empty ... may follow); the "with all three open" phrase is
        taken out before this check, so "... fill the tank with all three open?" still answers."""
        base = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. "
        for q in ("All three are open. How long does it take to fill the tank?", "With all three open, how long does it take to fill the tank?",
                  "How long does it take to fill the tank with all three open?", "All three are open. How long does it take to fill it?"):
            self.assertEqual(answers(base + q), values(Fraction(12, 5)), q)
        for q in ("All three are open. How long does it take to fill the tank during a storm?", "All three are open. How long does it take to fill the tank under a downpour?",
                  "All three are open. How long does it take to fill the tank amid the rain?", "All three are open. How long does it take to fill the tank overnight?"):
            self.assertIsNone(answers(base + q), q)

    def test_pipes_question_end_set(self):
        """Set 47 (9 wordings) was written after the batch-43 fix and run once, untuned: 2 solved, 1 declined (safe: "fill the EMPTY pool" is declined by the older rule against a
        question that asks to empty), 6 required declines, 0 wrong."""
        from fresh_word_problems_47 import FRESH
        self.assertEqual(score(FRESH), (2, 1, 6))

    def test_pipes_the_question_words_before_fill_are_the_plain_ones(self):
        """A storm named BEFORE "fill" still got the plain answer: "How long does it take during a storm to fill the pool?" and "How long, during a storm, does it take to fill the pool?"
        were answered 6.  Between "how long" and "fill" only the plain question words may stand (does / will / it / take / to / for / the / the vessel ...); the open phrase is taken out first."""
        base = "Pipe A fills a pool in 4 hours, pipe B in 12 hours, and a drain empties it in 6 hours. "
        for q in ("All three are open. How long does it take to fill the pool?", "How long does it take to fill the pool with all three open?",
                  "All three are open. How long does it take to fill it?", "All three are open. How long will it take for the pool to fill?"):
            self.assertEqual(answers(base + q), values(Fraction(6)), q)
        for q in ("All three are open. How long does it take during a storm to fill the pool?", "All three are open. How long, during a storm, does it take to fill the pool?"):
            self.assertIsNone(answers(base + q), q)

    def test_pipes_question_words_set(self):
        """Set 48 (9 wordings) was written after the batch-44 fix and run once, untuned: 3 solved, 6 required declines, 0 wrong."""
        from fresh_word_problems_48 import FRESH
        self.assertEqual(score(FRESH), (3, 0, 6))

    def test_percent_spent_left(self):
        """"Yara spent 75% of a paycheck on rent and had $280 left" is $1120 (the $280 is the 25% not spent); the same for fuel.  The percent is above 0 and below 100, the amount left is positive,
        and a second amount, a different question word or a changed noun declines."""
        self.assertEqual(answers("Yara spent 75% of a paycheck on rent and had $280 left. How much was the paycheck?"), values(1120))
        self.assertEqual(answers("After using 75% of the fuel in a tank, 280 liters remain. How much fuel was there at first?"), values(1120))
        for bad in ("Yara spent 100% of a paycheck on rent and had $280 left. How much was the paycheck?", "Yara spent 0% of a paycheck on rent and had $280 left. How much was the paycheck?",
                    "Yara spent 75% of a paycheck on rent and had $0 left. How much was the paycheck?", "Yara spent 75% of a paycheck on rent and $20 on food and had $280 left. How much was the paycheck?",
                    "Yara spent 75% of a paycheck on rent and had $280 left. How much was the rent?", "After using 75% of the fuel in a tank, 280 liters remain. How much was used?"):
            self.assertIsNone(answers(bad), bad)

    def test_price_minus_coupon(self):
        """"Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $46.00" is 14 (3.5n - 3 = 46).  The count is a positive whole number and a coupon larger than the amount paid declines."""
        self.assertEqual(answers("Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $46.00. How many notebooks were bought?"), values(14))
        self.assertEqual(answers("Bags of chips cost $7.50 each. With a $10 coupon, Kira paid $12.50. How many bags of chips were bought?"), values(3))
        for bad in ("Notebooks cost $4.50 each. With a $10 coupon, Bea paid $8.00. How many notebooks were bought?", "Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $47.00. How many notebooks were bought?",
                    "Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $46.00. How many pens were bought?"):
            self.assertIsNone(answers(bad), bad)

    def test_complementary_and_supplementary_angles(self):
        """"Two angles are complementary. One angle is 12 less than 5 times the other." is 17 and 73; supplementary angles add to 180; "more than" adds and "less than" subtracts; both are positive."""
        self.assertEqual(answers("Two angles are complementary. One angle is 12 less than 5 times the other. Find both angles."), values(17, 73))
        self.assertEqual(answers("Two angles are supplementary. One angle is 6 less than 5 times the other. Find both angles."), values(31, 149))
        self.assertEqual(answers("Two angles are complementary. One angle is 20 more than 4 times the other. Find both angles."), values(14, 76))
        for bad in ("Two angles are complementary. One angle is 120 more than 4 times the other. Find both angles.", "Two angles are complementary. One angle is 12 less than 5 times the other. Find the smaller angle.",
                    "Two angles are complementary. One angle is 12 less than 5 times the other, and the third is 4. Find both angles."):
            self.assertIsNone(answers(bad), bad)

    def test_percent_coupon_angle_set(self):
        """Set 49 (15 wordings) was written after the batch-45 families and run once, untuned: 6 solved, 1 declined (safe: "an allowance" is not an article the pattern lists), 8 required declines,
        0 wrong.  One item was first written as a required decline by mistake (190/3 and 80/3 are both positive, so the solver's answer was right) and was corrected."""
        from fresh_word_problems_49 import FRESH
        self.assertEqual(score(FRESH), (6, 1, 8))

    def test_fourth_set_is_now_a_development_set(self):
        from fresh_word_problems_4 import FRESH
        self.assertEqual(score(FRESH), (3, 1, 4))


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)

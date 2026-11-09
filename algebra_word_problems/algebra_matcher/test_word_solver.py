"""Tests for word_solver.py.   Run:  python test_word_solver.py

1. Phrasings for each of the five families, and problems it must decline.
2. Ground truth: every one of the 1,000 generated problems either gets None or the stored answer (a wrong answer fails).
3. The 100 hand-written matcher problems: every claim must be in the table of hand-calculated answers below.
4. 33 fresh wordings (fresh_word_problems.py), written after the solver was finished and run once, untuned.
"""
import re
import sys
import unittest
from fractions import Fraction

import number_puzzle as NP
import word_solver as WS
from test_number_puzzle import load_problems

# Answers worked out by hand for the hand-written matcher problems the solver claims.
HAND_ANSWERS = {
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
        for name in ("word_solver.py", "number_puzzle.py"):
            text = open(name, encoding="utf-8").read()
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
        self.assertIsNone(answers("The product of two consecutive integers is 56. Find them."))

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
        self.assertIsNone(answers("Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1440 words?"))

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
    def numbers_of(text):
        if re.search(r"\$[\d,.]+ each", text):                                   # two prices: compare the dollars
            return sorted(Fraction(x.replace(",", "")) for x in re.findall(r"\$([\d,]+(?:\.\d+)?)", text))
        if re.search(r"\$[\d,.]+ at \d+(?:\.\d+)?%", text):                # an interest answer: compare the dollars, not the rates
            return sorted(Fraction(x.replace(",", "")) for x in re.findall(r"\$([\d,]+(?:\.\d+)?)", text))
        if re.search(r"^\d+ (?:weeks|months|days) \(each will have", text):      # a savings answer: compare the time, not the amount each has
            return [Fraction(re.match(r"\d+", text).group())]
        if re.search(r"\d\s?(?:lb|kg) at \$", text):                           # a price-blend answer: compare the weights, not the prices
            return sorted(Fraction(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s?(?:lb|kg)\b", text))
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
            got, want = sorted(Fraction(v) for v in r.values), self.numbers_of(p["answer"])
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
        self.assertEqual((solved, declined, required), (21, 0, 12))


class DevelopmentWordingsLater(unittest.TestCase):
    """Fresh sets 2 and 3 became development sets when they led to changes (cue verbs; the spelled-number rule)."""

    def test_second_and_third_sets(self):
        from fresh_word_problems_2 import FRESH as F2
        from fresh_word_problems_3 import FRESH as F3
        self.assertEqual(score(F2), (21, 0, 6))      # it scored 18 solved / 3 declined before the cue verbs were added
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
            data = open(path, "rb").read()
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
        for text in ("Each interior angle of a regular polygon measures 150°. How many sides does the polygon have?",
                     "Each exterior angle of a regular polygon is 30°. How many sides does it have?",
                     "The exterior angles of a polygon add up to 360°. How many sides does it have?",
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

    def test_fourth_set_is_now_a_development_set(self):
        from fresh_word_problems_4 import FRESH
        self.assertEqual(score(FRESH), (3, 1, 4))


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)

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
}


def answers(problem):
    r = WS.solve(problem)
    return None if r is None else sorted(Fraction(v) for v in r.values)


def values(*xs):
    return sorted(Fraction(x) for x in xs)


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
        self.assertIsNone(answers("Working together, two gardeners weed a park in 6 hours. One alone would need 10 hours. How long would the other need alone?"))
        self.assertIsNone(answers("A tap fills a tank in 5 hours but a leak empties it in 8 hours. How long to fill it with both going?"))
        # regression: found by this test file, the stem "empt" must also catch "empties", "leaks" and "plug"
        self.assertIsNone(answers("A tap fills a bath in 10 minutes but the plug leaks and empties it in 30 minutes. With both going, how long to fill it?"))

    def test_percent_change(self):
        self.assertEqual(answers("After a 5% raise, Vera's salary is $32,550.00. What was the salary before the raise?"), values(31000))
        self.assertEqual(answers("A TV is marked down 25% to $450. What was the original price?"), values(600))
        self.assertEqual(answers("A store marks up a rug by 100% and sells it for $240.00. What did the store pay for it?"), values(120))
        # the question asks for the AFTER value, or the known amount is a saving: never answer
        self.assertIsNone(answers("A shirt costs $40 and is 25% off. What is the sale price?"))
        self.assertIsNone(answers("A shirt is 25% off, saving $10. What was the original price?"))
        self.assertIsNone(answers("After a 20% discount and a 5% tax, a TV costs $400. What was the original price?"))

    def test_proportion(self):
        self.assertEqual(answers("If 5 pens cost $12.50, how much do 12 pens cost?"), values(30))
        self.assertEqual(answers("A car travels 480 miles on 15 gallons of gas. At this rate, how many gallons are needed for 736 miles?"), values(Fraction(736, 32)))
        self.assertIsNone(answers("If 6 workers build a wall in 12 days, how long would 9 workers take?"))
        self.assertIsNone(answers("Sam earns $20/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $950. How many overtime hours were worked?"))
        self.assertIsNone(answers("Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1440 words?"))

    def test_every_number_needs_a_role(self):
        # one extra number the patterns do not use -> decline, whatever the rest says
        self.assertIsNone(answers("The sum of two numbers is 90 and their difference is 14. Find the numbers between 1 and 100."))
        self.assertIsNone(answers("After a 20% discount, a jacket costs $64. What was the original price? It was on sale for 3 days."))


class GroundTruth(unittest.TestCase):
    @staticmethod
    def numbers_of(text):
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


class FreshWordings(unittest.TestCase):
    def test_fresh(self):
        from fresh_word_problems import FRESH
        right = declined = 0
        for text, want in FRESH:
            got = answers(text)
            if want is None:
                self.assertIsNone(got, "should decline: " + text)
                right += 1
            elif got is None:
                declined += 1
            else:
                self.assertEqual(got, values(*want), text)
                right += 1
        with_answer = sum(1 for _t, w in FRESH if w is not None)
        print("  fresh wordings: %d of %d right (%d of the %d with an answer solved, %d declined, 0 wrong)" % (
            right, len(FRESH), with_answer - declined, with_answer, declined))
        self.assertEqual(declined, 3)


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)
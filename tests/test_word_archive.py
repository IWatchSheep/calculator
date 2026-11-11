"""The word archive: the final check of a stored equation, and the four lists played on the stored problems.

The rules the four-list tests hold (Grok's ruling, 2026-11-10):
  - a problem is offered a shape only when a problem of a different wording is a source of it;
  - a book game never makes a line "tried" and is never a win; a line that won in another wording is "similar";
  - proven = the same line was played and won on every stored problem of the wording, two of them with different numbers;
  - the proof key takes out people's names, the plural after a number and the name of the work; cue words stay.
Generated lines (ruling of the same day): trees over the sentence's numbers and 1, 2, 100, built from no stored equation;
a game wins only when it gives every asked number; a finished sweep with no winner is one loss record that never answers.
"""
import os
import sys
import tempfile
import types
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "algebra_word_problems", "algebra_matcher"))
import word_archive  # noqa: E402
import word_generator  # noqa: E402
from fractions import Fraction  # noqa: E402

TOGETHER = "X/R0 + X/R1 = 1"


def stored(pid, template, numbers, equation, answer):
    return types.SimpleNamespace(ID=pid, TEMPLATE=template, NUMBERS=numbers, EQUATION=equation, ANSWER=answer, SOLVER=None,
                                 PROBLEM=template.format(*numbers))


TAPS = "One tap fills a tub in {0} minutes and another tap in {1} minutes. How long do both taps take?"
FENCE = "Ann can paint a fence in {0} hours. Bob can do it in {1} hours. How long will it take them working together?"
LAWN = "Cy can mow a lawn in {0} hours. Di can do it in {1} hours. How long will it take them working together?"
LEAK = "A hose fills a pond in {0} days while a leak empties it in {1} days. How long does it take to fill it?"
BELT = "One belt moves a load in {0} minutes and a second belt in {1} minutes. How long do the two belts take?"
PUMP = "Pump one drains a pit in {0} hours and pump two in {1} hours. How long do they need as a pair?"


def small_book():
    return word_archive.Book([
        stored("t1", TAPS, ["6", "3"], "t/6 + t/3 = 1", "2 minutes"),
        stored("t2", TAPS, ["10", "15"], "t/10 + t/15 = 1", "6 minutes"),
        stored("f1", FENCE, ["5", "20"], "t/5 + t/20 = 1", "4 hours"),
        stored("f2", LAWN, ["12", "4"], "t/12 + t/4 = 1", "3 hours"),
        stored("k1", LEAK, ["4", "12"], "t/4 - t/12 = 1", "6 days"),
        stored("k2", LEAK, ["3", "6"], "t/3 - t/6 = 1", "6 days"),
        stored("b1", BELT, ["6", "3"], "t/6 + t/3 = 1", "2 minutes"),
        stored("b2", BELT, ["6", "3"], "t/6 + t/3 = 1", "2 minutes"),
        stored("p1", PUMP, ["8", "8"], "t/8 + t/8 = 1", "4 hours"),
    ])


def play_out(book, limit=500):
    archive, state = {"games": {}}, {"lines": {}, "next": {}, "similar": {}}
    for _ in range(limit):
        if not word_archive.one_pass(book, archive, state=state):
            break
    return archive


class FinalCheck(unittest.TestCase):
    def test_the_join_after_one_hour_is_two_and_a_quarter(self):
        self.assertEqual(word_archive.solve_equation("1/4 + t/4 + t/12 = 1"), 2.25)

    def test_a_match_is_kept_and_a_miss_is_not_called_proven(self):
        solved = word_archive.solve_equation("5x + 25(79 − x) = 1195")
        self.assertEqual(solved, 39.0)
        self.assertIsNone(word_archive.solve_equation("x + y = 3"))

    def test_a_problem_that_only_an_archive_family_answers_stays_in_the_reference_set(self):
        make = types.SimpleNamespace
        self.assertTrue(word_archive._in_reference_set(make(SOLVER=None, FAMILY=None)))
        self.assertTrue(word_archive._in_reference_set(make(SOLVER="word_solver", FAMILY="archive_work_rate_1")))
        self.assertFalse(word_archive._in_reference_set(make(SOLVER="word_solver", FAMILY="work_together")))

    def test_a_clock_time_in_the_answer_is_not_a_number_to_hit(self):
        self.assertEqual(word_archive.asked_numbers("60/11 ≈ 5.45 minutes after 1:00"), [Fraction(60, 11)])    # 5.45 is its rounded copy
        self.assertEqual(word_archive.asked_numbers("Sam is 40, Ben is 48"), [40, 48])
        self.assertEqual(word_archive.asked_numbers("9 hours (new machine: 4.5 hours)"), [9])
        self.assertEqual(word_archive.answer_numbers("12 lb at $3", ["3", "40"]), [12.0])


class ProofKey(unittest.TestCase):
    def setUp(self):
        self.book = small_book()

    def test_the_name_of_the_work_and_the_names_of_people_are_out(self):
        self.assertEqual(self.book.wording["f1"], self.book.wording["f2"])
        self.assertIn("{work}", self.book.wording["f1"])
        self.assertEqual(self.book.work_names[self.book.wording["f1"]], ["mow a lawn", "paint a fence"])
        self.assertEqual(sorted(self.book.mates[self.book.wording["f1"]]), ["f1", "f2"])

    def test_a_cue_word_stays(self):
        more = "A number is {0} more than twice another. Their sum is {1}. Find the smaller number."
        less = "A number is {0} less than twice another. Their sum is {1}. Find the smaller number."
        book = word_archive.Book([stored("m", more, ["3", "30"], "x + 2x + 3 = 30", "9"), stored("l", less, ["3", "30"], "x + 2x - 3 = 30", "11")])
        self.assertNotEqual(book.wording["m"], book.wording["l"])
        self.assertEqual(book.work_names, {})

    def test_a_vehicle_name_hides_a_wheel_count_so_it_is_a_cue(self):
        lot = "A lot has {0}. There are {1} vehicles and {2} wheels. How many of each are there?"
        book = word_archive.Book([
            stored("v1", lot.format("bicycles and tricycles", "{0}", "{1}"), ["112", "277"], "2x + 3(112 - x) = 277", "59 bicycles and 53 tricycles"),
            stored("v2", lot.format("motorcycles and cars", "{0}", "{1}"), ["113", "344"], "2x + 4(113 - x) = 344", "54 motorcycles and 59 cars")])
        self.assertNotEqual(book.wording["v1"], book.wording["v2"])

    def test_the_plural_after_a_number_is_out_but_less_keeps_its_s(self):
        self.assertEqual(self.book.exact_of("in {0} hours, {1} less"), "in {0} hour, {1} less")


class FourLists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.book = small_book()
        cls.archive = play_out(cls.book)

    def test_a_shape_is_offered_only_when_another_wording_is_a_source(self):
        book = self.book
        taps = [shape for _score, shape in word_archive.list1(book, book.words["t1"], 2, book.wording["t1"])]
        self.assertEqual(taps, [TOGETHER, "X/R0 - X/R1 = 1"])     # sources in other wordings: fence, belt, pump; and the leak
        leak = [shape for _score, shape in word_archive.list1(book, book.words["k1"], 2, book.wording["k1"])]
        self.assertEqual(leak, [TOGETHER])                 # "X/R0 - X/R1 = 1" is only in the leak wording: absent for it
        self.assertIn("X/R0 - X/R1 = 1", book.shapes)

    def test_a_book_game_is_not_a_played_game(self):
        lists = word_archive.lists_for(self.book.by_id["t1"], self.book, {"games": {}})
        statuses = [status for _line, status, _won, _lost in lists["list3"]]
        # t2's book game does not make a line "tried"; the two shapes in sentence order won in other wordings: similar
        self.assertEqual(statuses, ["similar", "never tried", "similar", "never tried"])
        self.assertEqual(lists["list3"][0][0], TOGETHER + " | 0,1")
        self.assertEqual({(won, lost) for _line, _status, won, lost in lists["list3"]}, {(0, 0)})
        self.assertIsNone(word_archive.proven_line(self.book, {"games": {}}, self.book.wording["t1"]))

    def test_a_played_line_that_wins_every_problem_is_proven(self):
        for pid in ("t1", "f1"):
            wording = self.book.wording[pid]
            self.assertEqual(word_archive.proven_line(self.book, self.archive, wording), TOGETHER + " | 0,1")
        text = "Eve can clean the house in 6 hours. Flo can do it in 3 hours. How long will it take them working together?"
        self.assertIsNone(word_archive.answer(text, self.book, self.archive))      # "clean the house" is not a stored sentence
        text = "Gil can paint a fence in 6 hours. Hal can do it in 3 hours. How long will it take them working together?"
        self.assertAlmostEqual(word_archive.answer(text, self.book, self.archive), 2.0)

    def test_two_problems_with_the_same_numbers_are_not_proof(self):
        wording = self.book.wording["b1"]
        record = self.archive["games"][wording]["lines"][TOGETHER + " | 0,1"]
        self.assertEqual(sorted(record["won"]), ["b1", "b2"])
        self.assertIsNone(word_archive.proven_line(self.book, self.archive, wording))
        self.assertIsNone(word_archive.answer(BELT.format("6", "3"), self.book, self.archive))

    def test_one_win_is_not_proof(self):
        wording = self.book.wording["p1"]
        self.assertEqual(self.archive["games"][wording]["lines"][TOGETHER + " | 0,1"]["won"], ["p1"])
        self.assertIsNone(word_archive.answer(PUMP.format("8", "8"), self.book, self.archive))

    def test_a_wrong_number_is_a_loss_and_a_lost_line_is_never_chosen(self):
        games = self.archive["games"][self.book.wording["k1"]]
        # the only shape the leak problems may try is the taps' shape; both orders give the wrong number: losses, then a dead end
        self.assertEqual(sorted(games["lines"]), [TOGETHER + " | 0,1", TOGETHER + " | 1,0"])
        self.assertTrue(all(record["lost"] and not record["won"] for record in games["lines"].values()))
        self.assertEqual(sorted(games["dead_end"]), ["k1", "k2"])
        lists = word_archive.lists_for(self.book.by_id["k1"], self.book, self.archive)
        self.assertEqual({status for _line, status, _won, _lost in lists["list3"]}, {"proven loss"})
        self.assertIsNone(word_archive.choose(lists["list3"]))
        self.assertIsNone(word_archive.answer(LEAK.format("4", "12"), self.book, self.archive))

    def test_the_archive_file_keeps_the_games(self):
        keep = word_archive.ARCHIVE
        folder = tempfile.mkdtemp()
        try:
            word_archive.ARCHIVE = os.path.join(folder, "word_archive.json")
            word_archive._write_archive(self.archive)
            again = word_archive._read_archive()
        finally:
            word_archive.ARCHIVE = keep
        for wording, games in self.archive["games"].items():
            self.assertEqual(sorted(again["games"][wording]["dead_end"]), sorted(games["dead_end"]))
            for key, record in games["lines"].items():
                self.assertEqual(sorted(again["games"][wording]["lines"][key]["won"]), sorted(record["won"]))
                self.assertEqual(len(again["games"][wording]["lines"][key]["lost"]), len(record["lost"]))
        self.assertEqual(word_archive.proven_line(self.book, again, self.book.wording["t1"]), TOGETHER + " | 0,1")


class GeneratedLines(unittest.TestCase):
    HEAD = [["4", "8", "2"], ["5", "15", "2"], ["4", "12", "2"], ["4", "12", "1"], ["12", "3", "1"]]
    HEAD_ANSWERS = [Fraction(4, 3), Fraction(9, 4), Fraction(3, 2), Fraction(9, 4), Fraction(11, 5)]

    def test_the_head_start_line_is_found_without_any_stored_equation(self):
        result = word_generator.sweep(self.HEAD, [self.HEAD_ANSWERS], set())
        self.assertEqual(result["line"], ["((N0 - N2) / (1 + (N0 / N1)))"])          # (a - h) / (1 + a/b): the 4 is written twice
        self.assertEqual(result["size"], 5)
        self.assertEqual(word_generator.evaluate(result["line"][0], ["4", "12", "1"]), Fraction(9, 4))

    def test_a_sweep_that_finds_nothing_says_how_far_it_went(self):
        result = word_generator.sweep([["3", "5"], ["4", "9"], ["7", "2"]], [[Fraction(1001, 7), Fraction(1003, 7), Fraction(1009, 7)]], set(), max_size=4)
        self.assertIsNone(result["line"])
        self.assertEqual((result["size"], result["fixed"], result["open"]), (4, [1, 2, 100], [0]))

    def test_a_number_is_not_hidden_as_itself_over_itself(self):
        # the answer is N0 + 1; N1 could only ride along as N1/N1 or as + N1 - N1, which is not a role for it
        result = word_generator.sweep([["3", "5"], ["4", "9"], ["7", "2"]], [[4, 5, 8]], set(), max_size=4)
        self.assertIsNone(result["line"])

    def test_a_cue_constant_is_there_only_with_its_cue_word(self):
        rows, wanted = [["50", "60"], ["45", "80"], ["30", "100"]], [[70, 55, 50]]       # the third angle: 180 - N0 - N1
        self.assertIsNone(word_generator.sweep(rows, wanted, {"angle"}, max_size=3)["line"])
        found = word_generator.sweep(rows, wanted, {"interior", "angle"}, max_size=3)
        self.assertEqual(found["fixed"], [1, 2, 100, 180])
        self.assertEqual(word_generator.evaluate(found["line"][0], ["50", "60"]), 70)

    def test_an_answer_with_two_numbers_needs_a_tree_for_each(self):
        rows = [["85", "13"], ["40", "6"], ["51", "9"]]
        found = word_generator.sweep(rows, [[49, 23, 30], [36, 17, 21]], set())
        self.assertEqual(found["line"], ["((N0 + N1) / 2)", "((N0 - N1) / 2)"])
        half = word_generator.sweep(rows, [[49, 23, 30], [1234, 77, 5]], set(), max_size=4)
        self.assertIsNone(half["line"])                    # one of two asked numbers is not a win
        self.assertEqual(half["open"], [1])

    def _book(self, rows, answers):
        text = "Kit can stack a pallet in {0} hours and Lou in {1} hours. Kit starts {2} hours early. How much longer do both need?"
        return word_archive.Book([stored("h%d" % n, text, row, "0 = 0*x", "%s hours" % answer) for n, (row, answer) in enumerate(zip(rows, answers))])

    def test_three_independent_sets_of_numbers_prove_a_generated_line(self):
        book = self._book(self.HEAD, ["4/3", "2.25", "1.5", "2.25", "2.2"])
        archive = {"games": {}}
        self.assertEqual(word_archive.sweep_wordings(book, archive), 1)
        wording = book.wording["h0"]
        self.assertEqual(word_archive.generated_line(book, archive, wording), ["((N0 - N2) / (1 + (N0 / N1)))"])
        record = archive["generated"][wording]
        self.assertEqual((record["version"], record["ids"], record["fixed"], record["size"]),
                         (word_generator.VERSION, ["h0", "h1", "h2", "h3", "h4"], [1, 2, 100], 5))
        text = book.by_id["h0"].TEMPLATE.format("6", "3", "2")
        self.assertAlmostEqual(word_archive.answer(text, book, archive), 4.0 / 3.0)        # (6 - 2) / (1 + 6/3)
        self.assertEqual(word_archive.sweep_wordings(book, archive), 0)                    # a finished sweep is not repeated

    def test_two_sets_of_numbers_are_a_candidate_not_proof(self):
        book = self._book(self.HEAD[:2], ["4/3", "2.25"])
        archive = {"games": {}}
        word_archive.sweep_wordings(book, archive)
        wording = book.wording["h0"]
        self.assertIsNotNone(word_archive.generated_candidate(book, archive, wording))
        self.assertIsNone(word_archive.generated_line(book, archive, wording))
        self.assertIsNone(word_archive.answer(book.by_id["h0"].PROBLEM, book, archive))

    def test_scaled_sets_of_numbers_are_one_set(self):
        book = self._book([["4", "8", "2"], ["8", "16", "4"], ["12", "24", "6"]], ["4/3", "8/3", "4"])
        self.assertEqual(word_archive._independent(book, book.wording["h0"]), 1)
        archive = {"games": {}}
        word_archive.sweep_wordings(book, archive)
        self.assertIsNone(word_archive.generated_line(book, archive, book.wording["h0"]))

    def test_a_loss_record_never_answers_and_a_new_problem_voids_it(self):
        book = self._book(self.HEAD[:3], ["1001/7", "1003/7", "1009/7"])
        archive = {"games": {}}
        word_archive.sweep_wordings(book, archive, max_size=4)
        wording = book.wording["h0"]
        record = word_archive.generated_record(book, archive, wording)
        self.assertEqual((record["line"], record["size"], record["ids"]), (None, 4, ["h0", "h1", "h2"]))
        self.assertIsNone(word_archive.answer(book.by_id["h0"].PROBLEM, book, archive))
        bigger = self._book(self.HEAD[:4], ["1001/7", "1003/7", "1009/7", "1013/7"])
        self.assertIsNone(word_archive.generated_record(bigger, archive, wording))        # another stored problem: void
        keep = word_generator.VERSION
        try:
            word_generator.VERSION = keep + 1
            self.assertIsNone(word_archive.generated_record(book, archive, wording))      # another generator: void
        finally:
            word_generator.VERSION = keep

    def test_a_book_line_gives_one_number_so_it_loses_an_answer_that_asks_for_two(self):
        ages = "Ana is {0} years older than Bo. The sum of their ages is {1}. How old is each?"
        cut = "A board of {0} cm is cut so one piece is {1} cm longer. How long is the shorter piece?"
        book = word_archive.Book([
            stored("a1", ages, ["13", "85"], "x + x + 13 = 85", "Bo is 36, Ana is 49"),
            stored("a2", ages, ["4", "30"], "x + x + 4 = 30", "Bo is 13, Ana is 17"),
            stored("c1", cut, ["13", "85"], "x + x + 13 = 85", "36 cm"),
            stored("c2", cut, ["4", "30"], "x + x + 4 = 30", "13 cm")])
        archive = play_out(book)
        self.assertEqual(word_archive.proven_line(book, archive, book.wording["c1"]), "X + X + R0 = R1 | 0,1")
        self.assertIsNone(word_archive.proven_line(book, archive, book.wording["a1"]))
        self.assertTrue(all(r["lost"] for r in archive["games"][book.wording["a1"]]["lines"].values()))


class StoredProblems(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.book = word_archive.Book()

    def test_the_final_check_of_0991_is_its_stored_equation(self):
        check = word_archive.final_check(self.book.by_id["0991"])
        self.assertEqual(check["variable"], "t")
        self.assertTrue(check["matched"])
        self.assertEqual(check["solved"], 2.25)

    def test_0991_is_not_offered_the_equation_of_its_own_wording(self):
        problem = self.book.by_id["0991"]
        wording = self.book.wording["0991"]
        self.assertEqual(sorted(self.book.mates[wording]), ["0971", "0974", "0980", "0991", "1000"])
        offered = [shape for _score, shape in word_archive.list1(self.book, self.book.words["0991"], len(problem.NUMBERS), wording)]
        self.assertTrue(offered)
        self.assertNotIn("R0/R1 + X/R1 + X/R2 = 1", offered)          # the head-start shape has no other wording as a source
        self.assertIn("R0/R1 + X/R1 + X/R2 = 1", self.book.shapes)

    def test_0991_is_proven_by_a_generated_line(self):
        archive = {"games": {}}
        wording = self.book.wording["0991"]
        word_archive.sweep_wordings(self.book, archive, wordings=[wording])
        self.assertEqual(word_archive.generated_line(self.book, archive, wording), ["((N0 - N2) / (1 + (N0 / N1)))"])
        self.assertAlmostEqual(word_archive.answer(self.book.by_id["0991"].PROBLEM, self.book, archive), 2.25)

    def test_the_working_together_sentences_are_one_wording_but_cars_is_a_cue(self):
        ids = ["0965", "0976", "0983", "0999"]                 # shelves, fence, lawn, house
        self.assertEqual(len({self.book.wording[i] for i in ids}), 1)
        self.assertEqual(sorted(self.book.mates[self.book.wording["0965"]]), ids)
        self.assertNotEqual(self.book.wording["0992"], self.book.wording["0965"])      # "wash the cars": car is in the cue list


if __name__ == "__main__":
    unittest.main()

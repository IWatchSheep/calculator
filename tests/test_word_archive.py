"""The word archive: the final check of a stored equation, and the four lists played on the stored problems."""
import os
import sys
import tempfile
import types
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "algebra_word_problems", "algebra_matcher"))
import word_archive  # noqa: E402

HEAD_START = "R0/R1 + X/R1 + X/R2 = 1 | 2,0,1"      # head start N2, first worker N0, second worker N1


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


class FourLists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        everything = word_archive.load_problems()
        cls.work = [p for p in everything if p.CATEGORY == "Work rate"]
        cls.book = word_archive.Book(cls.work)
        cls.archive = play_out(cls.book)
        cls.p0991 = cls.book.by_id["0991"]

    def test_the_final_check_of_0991_is_its_stored_equation(self):
        check = word_archive.final_check(self.p0991)
        self.assertEqual(check["variable"], "t")
        self.assertTrue(check["matched"])
        self.assertEqual(check["solved"], 2.25)

    def test_the_first_pass_has_list_1_and_reads_only_other_problems(self):
        lists = word_archive.lists_for(self.p0991, self.book, {"games": {}})
        self.assertEqual(lists["list1"][0], (60, "R0/R1 + X/R1 + X/R2 = 1"))
        statuses = {status for _line, status, _won, _lost in lists["list3"]}
        self.assertTrue(statuses <= {"tried", "similar", "never tried"})          # nothing is proven before a game is played
        tried = [line for line, status, _won, _lost in lists["list3"] if status == "tried"]
        # the book games of the other four problems.  In 1000 the head start is 1, so its book game reads the "= 1" as the
        # head start too; that second line is tried, and it loses as soon as a problem with a 2-hour head start plays it
        self.assertEqual(tried, [HEAD_START, "R0/R1 + X/R1 + X/R2 = R0 | 2,0,1"])
        self.assertEqual(lists["list4"][0][0], HEAD_START)

    def test_a_shape_that_only_the_problem_itself_has_is_not_a_line_for_it(self):
        make = types.SimpleNamespace
        one = make(ID="a", TEMPLATE="A tank holds {0} liters and loses {1} a day. When is it empty?", NUMBERS=["90", "6"],
                   EQUATION="90 - 6d = 0", ANSWER="15 days", SOLVER=None)
        two = make(ID="b", TEMPLATE="A rope of {0} m is cut into {1} equal pieces. How long is each?", NUMBERS=["12", "4"],
                   EQUATION="4x = 12", ANSWER="3 m", SOLVER=None)
        book = word_archive.Book([one, two])
        self.assertEqual(len(book.book_line), 2)
        own = [shape for _score, shape in word_archive.list1(book, book.words["a"], 2, "a")]
        self.assertEqual(own, ["R0*X = R1"])                                      # the other problem's shape, never its own

    def test_the_head_start_wording_is_proven_by_play(self):
        wording = self.book.wording["0991"]
        self.assertEqual(sorted(self.book.mates[wording]), ["0971", "0974", "0980", "0991", "1000"])
        self.assertEqual(word_archive.proven_line(self.book, self.archive, wording), HEAD_START)
        got = word_archive.answer(self.p0991.PROBLEM, self.book, self.archive)
        self.assertAlmostEqual(got, 2.25)

    def test_new_names_and_new_numbers_in_a_proven_wording(self):
        text = "Ann can do a job in 6 hours and Bob can do it in 3 hours. Ann works alone for 2 hours, then Bob joins. How much longer will it take to finish?"
        self.assertAlmostEqual(word_archive.answer(text, self.book, self.archive), 4.0 / 3.0)       # (1 - 2/6) / (1/6 + 1/3)

    def test_one_win_is_not_proof(self):
        text = "Lena can paint a fence in 5 hours. Ava can do it in 10 hours. How long will it take them working together?"
        wording = self.book.wording_of(word_archive.template_of(text)[0])
        self.assertEqual(len(self.book.mates[wording]), 1)
        lines = self.archive["games"][wording]["lines"]
        self.assertTrue(any(record["won"] and not record["lost"] for record in lines.values()))
        self.assertIsNone(word_archive.answer(text, self.book, self.archive))

    def test_a_wrong_number_is_a_loss_and_a_lost_line_is_never_chosen(self):
        make = types.SimpleNamespace
        taps = make(ID="t", TEMPLATE="One tap fills a tub in {0} minutes and another in {1} minutes. How long with both?", NUMBERS=["6", "3"],
                    EQUATION="t/6 + t/3 = 1", ANSWER="2 minutes", SOLVER=None)
        leak = make(ID="k", TEMPLATE="A hose fills a pond in {0} days while a leak empties it in {1} days. How long to fill it?", NUMBERS=["4", "12"],
                    EQUATION="t/4 - t/12 = 1", ANSWER="6 days", SOLVER=None)
        book = word_archive.Book([taps, leak])
        archive = play_out(book)
        games = archive["games"][book.wording["k"]]
        # the only shape the leak problem may try is the taps' shape; both orders give 3, not 6: two losses, then a dead end
        self.assertEqual(sorted(games["lines"]), ["X/R0 + X/R1 = 1 | 0,1", "X/R0 + X/R1 = 1 | 1,0"])
        self.assertTrue(all(record["lost"] and not record["won"] for record in games["lines"].values()))
        self.assertEqual(games["dead_end"], ["k"])
        lists = word_archive.lists_for(leak, book, archive)
        self.assertEqual({status for _line, status, _won, _lost in lists["list3"]}, {"proven loss"})
        self.assertIsNone(word_archive.choose(lists["list3"]))
        self.assertIsNone(word_archive.answer(leak.TEMPLATE.format("4", "12"), book, archive))

    def test_every_answer_from_a_proven_line_is_the_stored_answer(self):
        answered = 0
        for problem in self.work:
            got = word_archive.answer(problem.PROBLEM, self.book, self.archive)
            if got is None:
                continue
            answered += 1
            stored = word_archive.answer_numbers(problem.ANSWER, problem.NUMBERS)
            self.assertTrue(any(abs(got - a) <= 1e-4 * max(1.0, abs(a)) for a in stored), problem.ID)
        self.assertEqual(answered, 32)                                            # 37 problems; the five one-problem wordings decline

    def test_a_clock_time_in_the_answer_is_not_a_number_to_hit(self):
        self.assertEqual(word_archive.answer_numbers("60/11 ≈ 5.45 minutes after 1:00"), [60.0 / 11.0, 5.45])
        self.assertEqual(word_archive.answer_numbers("12 lb at $3", ["3", "40"]), [12.0])

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
            for key, record in games["lines"].items():
                self.assertEqual(sorted(again["games"][wording]["lines"][key]["won"]), sorted(record["won"]))
                self.assertEqual(len(again["games"][wording]["lines"][key]["lost"]), len(record["lost"]))
        self.assertEqual(word_archive.proven_line(self.book, again, self.book.wording["0991"]), HEAD_START)


if __name__ == "__main__":
    unittest.main()

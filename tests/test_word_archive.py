"""The word archive solves a stored equation only when that solution is the stored answer."""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "algebra_word_problems", "algebra_matcher"))
import word_archive  # noqa: E402


class WordArchive(unittest.TestCase):
    def test_the_join_after_one_hour_is_two_and_a_quarter(self):
        self.assertEqual(word_archive.solve_equation("1/4 + t/4 + t/12 = 1"), 2.25)

    def test_a_match_is_kept_and_a_miss_is_not_called_proven(self):
        solved = word_archive.solve_equation("5x + 25(79 − x) = 1195")
        self.assertEqual(solved, 39.0)
        self.assertIsNone(word_archive.solve_equation("x + y = 3"))

    def test_list_2_records_whether_the_stored_answer_was_hit(self):
        module = word_archive.load_problems()
        problem = next(p for p in module if p.ID == "0991")
        lists = word_archive.lists_for(problem)
        self.assertEqual(lists["list1"][0]["variable"], "t")
        self.assertTrue(lists["list2"][0]["matched"])
        self.assertEqual(lists["list2"][0]["solved"], 2.25)
        self.assertIn(lists["list3"][0]["status"], ("never tried", "tried", "proven"))

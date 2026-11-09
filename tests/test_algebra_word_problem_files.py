"""Checks the two algebra word problem folders.

    operators_one_algebra_word_problem_per_file/<category>/<id>/<id>.py and <id>.jpg      the 1,000 problems and their diagrams
    operator_row_math_for_algebra_word_problems/<category>/<id>/<id>.py                  how each problem is laid out as a row

Run from the project root (standard library only):   python tests/test_algebra_word_problem_files.py
The folders are written by operator_keys/make_algebra_word_problem_files.py; if a test here fails after the word solver changed, run that script again
(with the project's .venv, it needs Pillow for the pictures) and run this file again.
"""
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "algebra_word_problems", "algebra_matcher"))

import operator_row_math_for_algebra_word_problems as rows  # noqa: E402
import operators_one_algebra_word_problem_per_file as library  # noqa: E402
import word_solver  # noqa: E402

LIB = os.path.join(ROOT, "operators_one_algebra_word_problem_per_file")
SOURCE = os.path.join(ROOT, "algebra_word_problems", "algebra_word_problems.txt")
THOUSANDS = re.compile(r"(?<=\d),(?=\d{3})")


def stored_ids():
    text = open(SOURCE, encoding="utf-8").read()
    return re.findall(r"^#(\d{4}) \[", text, flags=re.M)


class Folders(unittest.TestCase):
    def test_every_problem_has_a_folder_a_file_a_picture_and_a_row(self):
        ids = stored_ids()
        self.assertEqual(len(ids), 1000)
        keys = library.keys()
        self.assertEqual(len(keys), 1000)
        self.assertEqual(sorted(k.split("/")[1] for k in keys), sorted(ids))
        self.assertEqual(rows.keys(), keys)
        for key in keys:
            category, pid = key.split("/")
            folder = os.path.join(LIB, category, pid)
            self.assertTrue(os.path.exists(os.path.join(folder, pid + ".py")), key)
            jpg = os.path.join(folder, pid + ".jpg")
            self.assertTrue(os.path.exists(jpg), key)
            self.assertGreater(os.path.getsize(jpg), 4000, key)                 # a real picture, not an empty file

    def test_the_problem_files_hold_the_stored_text(self):
        text = open(SOURCE, encoding="utf-8").read()
        for key in library.keys():
            m = library.get(key)
            block = re.search(r"^#%s \[[^\]]+\]\n(.*?)\n-{20,}" % m.ID, text, flags=re.S | re.M).group(1)
            fields = dict(line.partition(": ")[::2] for line in block.splitlines() if ": " in line)
            self.assertEqual(m.PROBLEM, fields["Problem"].strip(), key)
            self.assertEqual(m.EQUATION, fields["Equation"].strip(), key)
            self.assertEqual(m.ANSWER, fields["Answer"].strip(), key)
            self.assertEqual(m.TEMPLATE.format(*m.NUMBERS), THOUSANDS.sub("", m.PROBLEM), key)     # the template and the numbers rebuild the problem (thousands commas are dropped)

    def test_index_lists_every_problem(self):
        index = open(os.path.join(LIB, "INDEX.md"), encoding="utf-8").read()
        for key in library.keys():
            self.assertIn("`%s/`" % key, index)
        self.assertIn("1000 problems", index)


class Rows(unittest.TestCase):
    def test_a_row_has_one_box_for_every_number_and_one_result_box(self):
        for key in rows.keys():
            r, m = rows.get(key), library.get(key)
            self.assertEqual(r.KEY, key)
            self.assertEqual(r.LIBRARY_KEY, key)
            self.assertEqual(r.DEFAULTS, m.NUMBERS, key)
            self.assertEqual(len(r.INPUTS), len(m.NUMBERS), key)
            self.assertEqual(len(r.KINDS), len(m.NUMBERS), key)
            self.assertEqual(sum(1 for kind, _ in r.LEFT if kind == "box"), len(m.NUMBERS), key)
            self.assertEqual(r.RIGHT, [("box", "")], key)
            self.assertEqual(r.CALC, "ready" if m.SOLVER else "reference", key)
            self.assertTrue(callable(r.place))


class Catalog(unittest.TestCase):
    def test_the_index_lists_every_problem_and_its_diagram(self):
        import algebra_word_problem_catalog as catalog
        items = catalog.load_catalog(os.path.join(LIB, "INDEX.md"))
        self.assertEqual(len(items), 1000)
        self.assertEqual(len({i["category"] for i in items}), 55)
        self.assertEqual(sum(1 for i in items if i["status"] == "Ready"), 365)
        savings = next(i for i in items if i["key"] == "savings/0848")
        self.assertIn("Ben has $150", savings["problem"])
        self.assertEqual(savings["id"], "0848")
        self.assertTrue(os.path.isfile(catalog.diagram_path(LIB, savings)))


class Computing(unittest.TestCase):
    def test_ready_problems_compute_with_their_stored_numbers(self):
        ready = 0
        for key in library.keys():
            m = library.get(key)
            if m.SOLVER is None:
                with self.assertRaises(NotImplementedError):
                    m.compute()
                continue
            ready += 1
            answer = m.compute()
            self.assertIsInstance(answer, (int, float, list), key)
            if m.SOLVER == "word_solver":
                expected = word_solver.solve(m.PROBLEM)
                self.assertEqual(expected.family, m.FAMILY, key)
                got = answer if isinstance(answer, list) else [answer]
                self.assertEqual(got, [float(v) if v.denominator != 1 else int(v) for v in expected.values], key)
        self.assertEqual(ready, 365)                                           # 337 word_solver + 28 number_puzzle

    def test_your_own_numbers(self):
        self.assertEqual(library.get("savings/0848").compute(), 16)
        self.assertEqual(library.get("savings/0848").compute(200, 15, 350, 5), 15)        # I have $200 and save $15 a week; $350 and $5: 15 weeks
        with self.assertRaises(ValueError):
            library.get("savings/0848").compute(200, 15, 350, 15)                      # equal rates: the solver declines, it does not guess
        with self.assertRaises(ValueError):
            library.get("savings/0848").compute(200, 15)                               # a box is missing


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)
"""Checks the two algebra word problem folders.

    operators_one_algebra_word_problem_per_file/<category>/<id>/<id>.py and <id>.jpg      the 1,000 problems and their diagrams
    operator_row_math_for_algebra_word_problems/<category>/<id>/<id>.py                  how each problem is laid out as a row

Run from the project root (standard library only):   python tests/test_algebra_word_problem_files.py
The folders are written by operator_keys/make_algebra_word_problem_files.py; if a test here fails after the word solver changed, run that script again
(with the project's .venv, it needs Pillow for the pictures) and run this file again.
"""
import os
import re
from fractions import Fraction
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
    def test_every_card_is_one_column_with_one_token(self):
        """A card's centre shows one symbol: a blue box, a number that is not a box, a word (pay), or one character (a letter, + - x / = ( ) ;)."""
        token = re.compile(r"\d+(?:\.\d+)?|\d{1,3}(?:,\d{3})+(?:\.\d+)?|[A-Za-z]{2,}|\S")
        for key in rows.keys():
            for kind, text in rows.get(key).LEFT:
                if kind == "op":
                    self.assertTrue(token.fullmatch(text), "%s: %r" % (key, text))
        self.assertEqual([t for _, t in rows.get("consecutive_integers/0070").LEFT],
                         ["x", "+", "(", "x", "+", "1", ")", "+", "(", "x", "+", "2", ")", "=", ""])
        self.assertEqual([t for _, t in rows.get("savings/0848").LEFT], ["", "+", "", "w", "=", "", "+", "", "w"])

    def test_a_row_is_the_equation_with_a_box_for_every_blue_number(self):
        """The row is the problem's equation.  A blue box of the picture is a box of the row: same order, same value, prefilled.  A number of the equation that is not
        written in the problem text (the 1 and 2 of x + (x + 1) + (x + 2)) is plain text on both; the answer is the result box."""
        sys.path.insert(0, os.path.join(ROOT, "operator_keys"))
        import make_algebra_word_problem_files as generator
        for key in rows.keys():
            r, m = rows.get(key), library.get(key)
            self.assertEqual(r.KEY, key)
            self.assertEqual(r.LIBRARY_KEY, key)
            blue = [t for t in generator.equation_plan(m.EQUATION, m.NUMBERS) if t[0] == "num"]       # what the picture draws in blue
            self.assertEqual(r.BOX_INDEX, [t[2] for t in blue], key)
            self.assertEqual([Fraction(d) for d in r.DEFAULTS], [Fraction(t[1].replace(",", "")) for t in blue], key)      # same value (the text may write 38.00 where the equation has 38)
            self.assertEqual(r.DEFAULTS, [m.NUMBERS[i] for i in r.BOX_INDEX], key)
            self.assertEqual(len(set(r.BOX_INDEX)), len(r.BOX_INDEX), key)                          # a text number is in one box at most
            self.assertEqual(len(r.INPUTS), len(blue), key)
            self.assertEqual(len(r.KINDS), len(blue), key)
            self.assertEqual(sum(1 for kind, _ in r.LEFT if kind == "box"), len(blue), key)
            self.assertEqual(r.RIGHT, [("box", "")], key)
            self.assertEqual(r.CALC, "ready" if m.SOLVER else "reference", key)
            self.assertTrue(callable(r.place))


class Catalog(unittest.TestCase):
    def test_the_index_lists_every_problem_and_its_diagram(self):
        import algebra_word_problem_catalog as catalog
        items = catalog.load_catalog(os.path.join(LIB, "INDEX.md"))
        self.assertEqual(len(items), 1000)
        self.assertEqual(len({i["category"] for i in items}), 55)
        self.assertEqual(sum(1 for i in items if i["status"] == "Ready"), 554)
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
        self.assertEqual(ready, 554)                                           # 526 word_solver (349 + 177 archive families) + 28 number_puzzle

    def test_your_own_numbers(self):
        self.assertEqual(library.get("savings/0848").compute(), 16)
        self.assertEqual(library.get("savings/0848").compute(200, 15, 350, 5), 15)        # I have $200 and save $15 a week; $350 and $5: 15 weeks
        with self.assertRaises(ValueError):
            library.get("savings/0848").compute(200, 15, 350, 15)                      # equal rates: the solver declines, it does not guess
        with self.assertRaises(ValueError):
            library.get("savings/0848").compute(200, 15)                               # a box is missing


class InTheCalculator(unittest.TestCase):
    """The Ready problems can be put into a calculator row from the Operators window, and = answers them."""

    def test_every_ready_problem_answers_through_the_row_tree(self):
        from operator_row_math import row_tree
        ready = 0
        for key in library.keys():
            lib = library.get(key)
            node = row_tree.new_node(row_tree.WORD_PREFIX + key)
            if lib.SOLVER is None:
                with self.assertRaises(ValueError, msg=key):
                    row_tree.evaluate(node)               # a Reference problem says so, it never shows a number
            else:
                ready += 1
                self.assertEqual(row_tree.evaluate(node), lib.compute(), key)      # the boxes start with the stored numbers
        self.assertEqual(ready, 554)

    def test_a_list_of_answers_cannot_be_joined(self):
        from operator_row_math import row_tree
        for symbol in ("+", "−", "×", "÷", "=", "≠", "<", ">", "≤", "≥"):
            for a, b in (([27, 21], 2), (2, [27, 21]), ([27, 21], [1, 2]), ((1, 2), 3)):
                with self.assertRaises(ValueError, msg=symbol):
                    row_tree.join(symbol, a, b)
        self.assertEqual(row_tree.join("+", 2, 3), 5)                       # plain numbers still join

    def test_the_boxes_start_with_the_problems_own_numbers(self):
        from operator_row_math import row_tree
        for key in library.keys():
            node = row_tree.new_node(row_tree.WORD_PREFIX + key)
            self.assertEqual(node["slots"], [str(d) for d in rows.get(key).DEFAULTS], key)

    def test_the_window_places_a_problem_and_equals_answers_it(self):
        try:
            import tkinter
            import main
            app = main.CalculatorGUI()
            app.update()
        except (ImportError, tkinter.TclError) as exc:
            raise unittest.SkipTest("no GUI available: %s" % exc)
        try:
            import algebra_word_problem_catalog as catalog
            items = {i["key"]: i for i in catalog.load_catalog(os.path.join(LIB, "INDEX.md"))}
            say = lambda: app.results.get("1.0", "end")                                # noqa: E731
            boxes = lambda: [k for k, c in enumerate(app._cards(0)) if c[0] == "box"]  # noqa: E731

            for key, shown in (("savings/0848", "16"), ("system_of_equations/0920", "(27, 21)")):
                app._clear_all()
                app._place_word_problem(items[key])
                self.assertIn(items[key]["problem"], say())
                app._equals()                                                      # the boxes already hold the stored numbers
                self.assertIn("=  " + shown, say(), key)
            # change a number: 200 saved at $15 a week against 350 at $5 is 15 weeks
            app._clear_all()
            app._place_word_problem(items["savings/0848"])
            for k, text in zip(boxes(), ("200", "15", "350", "5")):
                app._pick_box(0, k)
                for _ in range(6):
                    app._key("⌫")
                for ch in text:
                    app._key(ch)
            app._equals()
            self.assertIn("=  15", say())
            # nesting: Addition( word problem, 1 ) -> 16 + 1;  a list answer inside an operator that wants one number says so
            for key, expect in (("savings/0848", "=  17"), ("system_of_equations/0920", "single number")):
                app._clear_all()
                app._place_operator_row("math/arithmetic/addition")
                app._pick_box(0, boxes()[0])
                app._place_word_problem(items[key])
                self.assertEqual(app.rows[0]["node"]["slots"][0]["slots"][0]["key"], "word:" + key)
                last = [k for k, c in enumerate(app._cards(0)) if c[0] == "box"][-1]
                app._pick_box(0, last)
                app._key("1")
                app._equals()
                self.assertIn(expect, say(), key)
            reference = next(i for i in items.values() if i["status"] != "Ready")
            app._clear_all()
            app._place_word_problem(reference)
            self.assertIn("reference only", say())
            self.assertTrue(app._is_blank(app.rows[0]))                              # nothing was placed
        finally:
            app.destroy()


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)
"""The operator rows follow the operators' pictures.

    operators_one_operator_per_file/<operator>.jpg      the picture (the reference)
    operator_row_math/<operator>/<operator>.py          the row of cards, written by operator_keys/make_operator_row_files.py from operator_keys/operator_row_specs.txt

Run from the project root:   python tests/test_operator_pictures.py
"""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import operator_row_math as rows  # noqa: E402
from operator_row_math import row_tree  # noqa: E402

KINDS = {"box", "out", "dec", "op"}


class RowFiles(unittest.TestCase):
    def test_every_row_is_well_formed(self):
        keys = rows.keys()
        self.assertEqual(len(keys), 507)
        for key in keys:
            m = rows.get(key)
            self.assertTrue(m.LEFT, key)
            for kind, text in m.LEFT + m.RIGHT:
                self.assertIn(kind, KINDS, key)
                if kind == "op":
                    self.assertTrue(text and " " not in text, "%s: %r" % (key, text))      # one token per card
            smap = row_tree.slot_map(m)
            self.assertEqual(len(smap), sum(1 for k, _ in m.LEFT if k == "box"), key)
            # every input of a calculating operator has a box on the row; a reference operator only shows its picture
            if m.CALC != "reference":
                self.assertEqual(sorted(set(smap)), list(range(len(m.INPUTS))), key)
            self.assertEqual(len(m.INPUTS), len(m.KINDS), key)
            self.assertTrue(all(j < max(len(m.INPUTS), 1) or m.CALC == "reference" for j in smap), key)

    def test_the_row_starts_with_the_pictures_own_symbols(self):
        text = lambda key: [t for _, t in rows.get(key).LEFT]            # noqa: E731
        self.assertEqual(text("geometry/geometry/cone_surface_area"), ["", "=", "π", "×", "", "×", "(", "", "+", "", ")"])
        self.assertEqual(rows.get("geometry/geometry/cone_surface_area").SLOTS, [0, 0, 1])          # the r is written twice: one input, two boxes
        self.assertEqual([k for k, _ in rows.get("geometry/geometry/cone_surface_area").LEFT][0], "out")   # A is the answer box
        self.assertEqual(text("math/algebra/power"), ["", "^", ""])
        self.assertEqual(rows.get("math/algebra/power").RIGHT, [("box", "")])                       # "a ^ b = [ ]": the picture's last box is the result
        self.assertEqual(text("math/abstract_algebra/kernel")[:2], ["ker", ""])

    def test_exponents_and_subscripts_sit_in_their_own_cell_above_or_below(self):
        """Every card is its own column; an exponent is one grid row up (level -1) and a subscript one row down (+1), and shows ordinary characters."""
        circle = rows.get("geometry/geometry/circle_area")
        self.assertEqual(circle.LEVELS, [0, 0, 0, 0, 0, -1])
        self.assertEqual(circle.LEFT[-1], ("op", "2"))                                 # r squared: the 2 is its own card, one row up
        sigma = rows.get("math/algebra/geometric_series_sum")
        self.assertIn(1, sigma.LEVELS)                                                 # a subscript is one row down
        for key in rows.keys():
            m = rows.get(key)
            levels = getattr(m, "LEVELS", None)
            if levels is not None:
                self.assertEqual(len(levels), len(m.LEFT), key)
                self.assertTrue(set(levels) <= {-1, 0, 1}, key)
        node = row_tree.new_node("geometry/geometry/circle_area")
        self.assertEqual(len(row_tree.levels(node)), len(row_tree.flatten(node)))      # one level for every card the window draws

    def test_a_fraction_is_always_written_top_to_bottom(self):
        """A "/" in a formula is a fraction: the numerator on the row above a bar, the denominator on the row below, centred over the bar.  Brackets that only wrapped
        a whole numerator or denominator are not drawn; a product stays in the numerator; a bracketed denominator is alone; nested fractions stack."""
        from operator_row_math.layout import group_fractions
        from operator_row_math.row_builder import _plan

        def cards(text):
            return [("box", "") if t == "B" else ("op", t) for t in text.split()]

        def table(text):
            c = cards(text)
            f = group_fractions(c, [0] * len(c))
            return [(t, [(g, p) for g, p in fl]) for (_k, t), fl in zip(c, f)]

        t = table("B × B / ( B × B )")                                  # m v / (q B): the bracketed denominator is alone, the brackets are not drawn
        self.assertEqual([p for _t, fl in t for g, p in fl], ["n", "n", "n", "bar", "hide", "d", "d", "d", "hide"])
        t = table("1 / B − 1 / B")                                      # the minus is not part of either fraction
        self.assertEqual([len(fl) for _t, fl in t], [1, 1, 1, 0, 1, 1, 1])
        self.assertEqual(table("yes / no"), [("yes", []), ("/", []), ("no", [])])        # "yes / no" is text, not a fraction
        # where the cards go: numerator one row up, denominator one row down, centred over a bar as wide as the wider side
        c = cards("B B / B")
        f = group_fractions(c, [0, 0, 0, 0])
        placed, bars, end = _plan(4, [0, 0, 0, 0], f)
        self.assertEqual(placed[0], (-1, 0))
        self.assertEqual(placed[1], (-1, 1))
        self.assertEqual(placed[3], (1, 0))                              # the single denominator card is left of centre only if it fits: width 1 over width 2
        self.assertEqual(bars, [(0, 0, 2)])
        self.assertEqual(end, 2)
        # the real rows
        self.assertTrue(any(rows.get("physics/physics/gravitation").FRAC))
        self.assertTrue(any(rows.get("math/algebra/quadratic_formula").FRAC))
        self.assertFalse(any(getattr(rows.get("math/arithmetic/addition"), "FRAC", [[]])))

    def test_a_constant_or_letter_is_an_ordinary_card_not_a_blue_box(self):
        """Only a box the person types is blue.  g in W = m g, and the A of P(A|B), are ordinary cards."""
        weight = rows.get("physics/physics/weight")
        self.assertEqual([c for c in weight.LEFT if c[0] == "box"], [("box", "")])             # only m
        self.assertIn(("op", "g"), weight.LEFT)
        bayes = rows.get("math/statistics_and_probability/bayes_theorem")
        self.assertEqual(bayes.INPUTS, ["p_b_given_a", "p_a", "p_b"])
        self.assertEqual(len(bayes.LEFT) - len([c for c in bayes.LEFT if c[0] != "box"]), 3)   # the three probabilities are the boxes the picture draws
        self.assertNotIn("with", [t for _, t in bayes.LEFT])

    def test_inputs_the_picture_does_not_draw_get_extra_boxes_and_are_listed(self):
        kernel = rows.get("math/abstract_algebra/kernel")
        self.assertEqual([t for k, t in kernel.LEFT if k == "op"], ["ker", "with", ","])
        with open(os.path.join(ROOT, "operator_keys", "operator_rows_with_extra_boxes.txt"), encoding="utf-8") as f:
            listed = f.read()
        self.assertIn("math/abstract_algebra/kernel   extra boxes for: G, identity", listed)
        # a reference operator can't calculate, so it never gets extra boxes
        for key in rows.keys():
            if rows.get(key).CALC == "reference":
                self.assertNotIn(key + "   extra boxes", listed, key)


class InTheWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import tkinter
            import main
            cls.app = main.CalculatorGUI()
            cls.app.update()
        except (ImportError, tkinter.TclError) as exc:
            raise unittest.SkipTest("no GUI available: %s" % exc)

    @classmethod
    def tearDownClass(cls):
        cls.app.destroy()

    def setUp(self):
        self.app._clear_all()

    def paths(self):
        return sorted({p for k, _t, p in self.app._cards(0) if k == "box"})        # one path per input

    def type_into(self, path, text):
        self.app.rows[0]["sel"] = path
        for ch in text:
            self.app._key(ch)

    def outs(self):
        return [t for k, t, _p in self.app._cards(0) if k == "out"]

    def test_the_answer_box_fills_in_and_a_repeated_variable_is_one_input(self):
        app = self.app
        app._place_operator_row("geometry/geometry/cone_surface_area")
        cards = app._cards(0)
        boxes = [c for c in cards if c[0] == "box"]
        self.assertEqual(len(boxes), 3)                                 # r, r, l
        self.assertEqual(len(self.paths()), 2)                          # but two inputs
        self.assertEqual(self.outs(), [""])
        r, l = self.paths()
        self.type_into(r, "3")
        self.type_into(l, "5")
        shown = [t for k, t, _p in app._cards(0) if k == "box"]
        self.assertEqual(shown, ["3", "3", "5"])                        # typing r fills both r boxes
        app._equals()
        self.assertTrue(self.outs()[0].startswith("75.398"))
        self.type_into(l, "1")                                           # changing a number forgets the old answer
        self.assertEqual(self.outs(), [""])

    def test_a_formula_with_two_answer_boxes_shows_each_answer(self):
        app = self.app
        app._place_operator_row("math/algebra/quadratic_formula")
        self.assertEqual(len(self.outs()), 2)
        a, b, c = self.paths()
        self.type_into(a, "1")
        self.type_into(b, "3")
        app._key("±")
        self.type_into(c, "2")
        app._equals()
        self.assertEqual(sorted(self.outs()), ["1", "2"])

    def test_a_picture_that_hides_inputs_still_calculates_through_extra_boxes(self):
        app = self.app
        app._place_operator_row("math/abstract_algebra/kernel")
        self.assertEqual([t for k, t, _p in app._cards(0) if k == "op"], ["ker", "with", ","])
        self.assertEqual(len(self.paths()), 3)                          # phi, G, identity


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)

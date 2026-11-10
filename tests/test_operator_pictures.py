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
        self.assertEqual(len(keys), 627)
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


class RustPort(unittest.TestCase):
    def test_the_rust_layouts_are_up_to_date_with_the_python_rows(self):
        """rust_calculator/src/layouts.rs is generated from the Python row files; if this fails run  python operator_keys/make_rust_layouts.py ."""
        sys.path.insert(0, os.path.join(ROOT, "operator_keys"))
        import make_rust_layouts as generator
        text, count = generator.build_text()
        self.assertEqual(count, 627)
        with open(generator.OUT, encoding="utf-8", newline="") as f:
            self.assertEqual(f.read().replace("\r\n", "\n"), text)

    def test_the_rust_multi_row_texts_are_the_python_ones(self):
        """The words that explain a multi-row operator (its title and each row's title) are the same in Python and in rust_calculator/src/multirow.rs."""
        from operator_row_math import multirow_specs
        with open(os.path.join(ROOT, "rust_calculator", "src", "multirow.rs"), encoding="utf-8") as f:
            rust = f.read()
        for key in ("physics/physics/navier_stokes_equation", "math/differential_geometry_and_tensors/exterior_derivative", "math/abstract_algebra/direct_sum",
                    "math/abstract_algebra/field_extension", "math/optimization_and_numerical_methods/kkt_conditions",
                    "geometry/geometry/heron_s_formula", "physics/physics/relativistic_doppler",
                    "physics/physics/relativistic_kinetic_energy", "physics/physics/relativistic_momentum", "physics/physics/length_contraction",
                    "physics/physics/time_dilation", "math/statistics_and_probability/standard_deviation",
                    "math/statistics_and_probability/sample_standard_deviation", "physics/physics/gravitational_time_dilation",
                    "math/statistics_and_probability/range", "math/statistics_and_probability/interquartile_range",
                    "math/statistics_and_probability/variance_of_random_variable", "physics/physics/kalman_update_state", "physics/physics/pid_sum", "physics/physics/gps_clock_correction"):
            spec = multirow_specs.get(key)
            self.assertIn('title: "%s"' % spec["title"], rust, key)
            for row in spec["rows"]:
                fill = "&[%s]" % ", ".join("(%d, Fill::Row(%d))" % (k, v["chain"]) for k, v in row["fill"].items()) if "fill" in row else "&[]"    # a chained box: Fill::Row(k)
                self.assertIn('RowSpec { title: "%s", node: NodeSpec { op: "%s", fill: %s } }' % (row["title"], row["op"], fill), rust, key)
        for word in ("density", "viscosity", "pressure", "incompressible"):          # the explanation really is in words
            self.assertIn(word, multirow_specs.get("physics/physics/navier_stokes_equation")["title"])


class CardWords(unittest.TestCase):
    def test_the_words_line_up_with_the_cards_of_a_row(self):
        for key in ("physics/physics/gravitation", "math/arithmetic/addition", "physics/physics/navier_stokes_x_momentum"):
            node = row_tree.new_node(key)
            self.assertEqual(len(row_tree.words(node)), len(row_tree.flatten(node)), key)
        outer = row_tree.new_node("math/arithmetic/multiplication")           # an operator written inside a box adds its own cards, with its own words
        row_tree.set_slot(outer, (0,), row_tree.new_node("math/arithmetic/addition"))
        self.assertEqual(len(row_tree.words(outer)), len(row_tree.flatten(outer)))


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

    def paths_of(self, i):
        return sorted({p for k, _t, p in self.app._cards(i) if k == "box"})

    def type_into(self, path, text):
        self.app.rows[0]["sel"] = path
        for ch in text:
            self.app._key(ch)

    def outs(self):
        return [t for k, t, _p in self.app._cards(0) if k == "out"]

    def card_frames(self, i=0):
        """{card index: the card's widget} of row i (a card that is not drawn, like the / of a fraction, has none)."""
        return {w.card_index: w for row in self.app.rows[i]["inner"].winfo_children() for w in row.winfo_children() if hasattr(w, "card_index")}

    def type_word(self, box, text):
        box.focus_force()                       # clicking the box clears its grey hint and sends the typing to it
        box.update()
        box.event_generate("<FocusIn>")
        box.insert(0, text)
        box.event_generate("<KeyRelease>")

    def test_an_operator_opens_with_its_words_in_the_boxes(self):
        self.app._place_operator_row("physics/physics/gravitation")
        self.app.update()
        label, context = self.app._card_words(0)[0]                          # the answer card of F = G m1 m2 / r^2
        self.assertTrue(label and context)
        frame = self.card_frames()[0]
        self.assertEqual((frame.label_box.get(), frame.context_box.get()), (label, context))
        self.assertEqual(self.app.rows[0]["words"], {})                      # nothing typed yet: these are the operator's own words

    def test_the_label_and_context_boxes_take_the_words_you_type(self):
        self.app._place_operator_row("math/arithmetic/addition")             # an operator that comes with no words
        self.app.update()
        frames = self.card_frames()
        self.assertEqual(len(frames), len(self.app._cards(0)))               # every card has its Label / Item and Context boxes
        self.type_word(frames[0].label_box, "force")
        self.type_word(frames[0].context_box, "newtons")
        self.assertEqual(self.app.rows[0]["words"][0], ("force", "newtons"))
        self.app._render_row(0)                                              # drawing the row again keeps what was typed
        self.app.update()
        again = self.card_frames()[0]
        self.assertEqual((again.label_box.get(), again.context_box.get()), ("force", "newtons"))
        self.assertEqual(self.app._card_words(0)[0], ("force", "newtons"))

    def test_words_typed_over_the_operators_own_words_replace_them(self):
        self.app._place_operator_row("physics/physics/gravitation")
        self.app.update()
        box = self.card_frames()[0].label_box
        box.focus_force()
        box.update()
        box.event_generate("<FocusIn>")
        box.delete(0, "end")                                                 # erase the words, then type different ones
        box.insert(0, "pull")
        box.event_generate("<KeyRelease>")
        self.assertEqual(self.app._card_words(0)[0][0], "pull")
        self.assertTrue(self.app._card_words(0)[0][1])                       # the Context box still has its own words

    def test_the_console_puts_a_word_into_the_box_last_clicked(self):
        self.app._place_operator_row("math/arithmetic/addition")
        self.app.update()
        self.card_frames()[2].label_box.event_generate("<FocusIn>")
        self.app._apply_word(0, "pens")
        self.assertEqual(self.app._card_words(0)[2][0], "pens")
        self.card_frames()[2].context_box.event_generate("<FocusIn>")
        self.app._apply_word(None, "in the drawer")                           # None = the box last clicked
        self.assertEqual(self.app._card_words(0)[2], ("pens", "in the drawer"))

    def test_the_words_of_a_row_are_forgotten_when_its_math_changes(self):
        self.app._place_operator_row("math/arithmetic/addition")
        self.type_word(self.card_frames()[0].label_box, "force")
        self.assertEqual(self.app.rows[0]["words"][0][0], "force")
        self.app._place_operator_row("math/arithmetic/addition")
        self.assertEqual(self.app.rows[0]["words"], {})

    # ---------- chaining: a row reads the answer of an earlier row ----------
    def place_chain(self, key, typed):
        """Open a multi-row operator and type numbers into its first row ({box number: value})."""
        from operator_row_math import row_tree
        self.app._place_operator_row(key)
        self.app.update()
        for j, value in typed.items():
            row_tree.set_slot(self.app.rows[0]["node"], (j,), str(value))

    def press_equals(self):
        self.app._equals()
        self.app.update()
        return self.app.results.get("1.0", "end")

    def chained_values(self, row, path):
        from operator_row_math import row_tree
        slot = row_tree.get_slot(self.app.rows[row]["node"], path)
        return slot.get("value")

    def test_heron_in_two_rows_gives_the_same_number_as_heron_in_one(self):
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        compute = library.get("geometry/geometry/heron_s_formula").compute
        for a, b, c in ((3, 4, 5), (7, 8, 9), (5.5, 6.25, 7.75), (0.1, 0.2, 0.25), (1000, 1200, 1500)):
            self.app._clear_all()
            self.place_chain("geometry/geometry/heron_s_formula", {0: a, 1: b, 2: c})
            self.press_equals()
            area = row_tree.evaluate(self.app.rows[1]["node"])
            self.assertEqual(area, compute(a, b, c), (a, b, c))              # the exact same number, not a rounded one
            s = (a + b + c) / 2
            for path in ((0,),):                                              # the s boxes of Row 2 are one input: all four hold Row 1's answer
                self.assertEqual(self.chained_values(1, path), s)
            self.assertEqual([t for k, t, p in self.app._cards(1) if k == "box" and p == (0,)], [row_tree.fmt(s)] * 4)
            for j, value in enumerate((a, b, c), start=1):                    # the sides on Row 2 are the ones typed on Row 1
                self.assertEqual(float(row_tree.get_slot(self.app.rows[1]["node"], (j,))), float(value))

    def test_a_changed_side_gives_a_new_semi_perimeter(self):
        from operator_row_math import row_tree
        self.place_chain("geometry/geometry/heron_s_formula", {0: 3, 1: 4, 2: 5})
        self.press_equals()
        self.assertEqual(self.chained_values(1, (0,)), 6)
        row_tree.set_slot(self.app.rows[0]["node"], (0,), "6")
        self.app._invalidate()                                                # something changed: the chained box forgets its answer
        self.assertIsNone(self.chained_values(1, (0,)))
        self.press_equals()
        self.assertEqual(self.chained_values(1, (0,)), 7.5)                   # (6 + 4 + 5) / 2, not the old 6

    def test_a_triangle_that_cannot_exist_and_an_empty_box_decline(self):
        from operator_row_math import row_tree
        self.place_chain("geometry/geometry/heron_s_formula", {0: 1, 1: 1, 2: 5})
        text = self.press_equals()
        self.assertIn("Row 2", text)                                         # the square root of a negative number: declined, like the one-row Heron
        self.app._clear_all()
        self.place_chain("geometry/geometry/heron_s_formula", {0: 3, 1: 4})   # the third side is left empty
        text = self.press_equals()
        self.assertIn("Fill every square box", text)
        self.assertIsNone(self.chained_values(1, (0,)))                       # no number in the chained box

    def test_typing_into_a_chained_box_does_not_stick(self):
        from operator_row_math import row_tree
        self.place_chain("geometry/geometry/heron_s_formula", {0: 3, 1: 4, 2: 5})
        row_tree.set_slot(self.app.rows[1]["node"], (0,), "999")             # the person types into a chained box
        self.press_equals()
        self.assertEqual(self.chained_values(1, (0,)), 6)                    # = puts the earlier answer back
        self.assertEqual(row_tree.evaluate(self.app.rows[1]["node"]), 6)

    def test_deleting_row_1_clears_the_chain(self):
        self.place_chain("geometry/geometry/heron_s_formula", {0: 3, 1: 4, 2: 5})
        self.press_equals()
        self.app._clear_row_math(0)
        text = self.press_equals()
        self.assertIn("Row 1", text)                                         # Row 1 is empty: declined, the answer is not a number
        self.assertIsNone(self.chained_values(1, (0,)))                       # Row 2 does not keep the old s

    def test_doppler_in_two_rows_gives_the_same_number_as_doppler_in_one(self):
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        compute = library.get("physics/physics/relativistic_doppler").compute
        c = 299792458
        for f0, v in ((100, 0.6 * c), (100, -0.6 * c), (540e12, 1.5e7), (1, 0)):
            self.app._clear_all()
            self.place_chain("physics/physics/relativistic_doppler", {0: v})
            row_tree.set_slot(self.app.rows[1]["node"], (0,), str(f0))      # f0 is typed on Row 2: it is its first input
            self.press_equals()
            self.assertEqual(row_tree.evaluate(self.app.rows[1]["node"]), compute(f0, v), (f0, v))
            self.assertEqual(self.chained_values(1, (1,)), v / c)             # beta is Row 1's answer, both beta boxes
            self.assertEqual(compute(f0, v, c), compute(f0, v))

    def test_doppler_declines_at_the_speed_of_light(self):
        c = 299792458
        for v in (c, -c, 2 * c):
            self.app._clear_all()
            self.place_chain("physics/physics/relativistic_doppler", {0: v})
            text = self.press_equals()
            self.assertIn("speed must be less than the speed of light", text)
            self.assertIsNone(self.chained_values(1, (1,)))

    # ---------- the four operators that take their γ from the Lorentz factor (Row 1) ----------
    GAMMA_ROWS = [
        # operator, the typed box of Row 2 (the others are chained or linked), arguments of today's compute(typed, v)
        ("relativistic_kinetic_energy", (1,), lambda x, v: (x, v)),
        ("relativistic_momentum", (1,), lambda x, v: (x, v)),
        ("length_contraction", (0,), lambda x, v: (x, v)),
        ("time_dilation", (0,), lambda x, v: (x, v)),
    ]

    def test_the_lorentz_chains_give_todays_numbers(self):
        """Row 1 is the Lorentz factor, Row 2 reads it.  Kinetic energy is the same float as today's compute(); the others differ in the last bit now and then
        (L0 / γ is not always the same float as L0 times the square root), so they are checked to one bit (2 ulp), never more."""
        import math
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        c = 299792458
        cases = [(2, 0.6 * c), (1, 0.8 * c), (100, 0.5 * c), (3.5, -0.3 * c), (1e6, 0.99 * c), (0.001, 1000.0), (5, 0)]
        for name, typed_box, _args in self.GAMMA_ROWS:
            today = library.get("physics/physics/" + name).compute
            for x, v in cases:
                self.app._clear_all()
                self.app._place_operator_row("physics/physics/" + name)
                self.app.update()
                row_tree.set_slot(self.app.rows[0]["node"], (0,), repr(v))                 # v is typed on Row 1
                row_tree.set_slot(self.app.rows[1]["node"], (typed_box[0],), repr(x))      # m, L0 or dt0 is typed on Row 2
                self.app._sync_links()
                self.press_equals()
                got = row_tree.evaluate(self.app.rows[1]["node"])
                expected = today(x, v)
                if name == "relativistic_kinetic_energy":
                    self.assertEqual(got, expected, (name, x, v))
                else:
                    self.assertTrue(abs(got - expected) <= 2 * math.ulp(expected), (name, x, v, got, expected))
                gamma = library.get("physics/physics/lorentz_factor").compute(v)
                self.assertEqual(self.chained_values(1, (1,) if name in ("length_contraction", "time_dilation") else (0,)), gamma, name)   # γ is Row 1's exact answer

    def test_the_lorentz_chains_decline_at_the_speed_of_light(self):
        c = 299792458
        for name, typed_box, _args in self.GAMMA_ROWS:
            for v in (c, -c, 2 * c):
                from operator_row_math import row_tree
                self.app._clear_all()
                self.app._place_operator_row("physics/physics/" + name)
                row_tree.set_slot(self.app.rows[0]["node"], (0,), repr(v))
                row_tree.set_slot(self.app.rows[1]["node"], (typed_box[0],), "2")
                self.app._sync_links()
                text = self.press_equals()
                self.assertIn("speed must be less than the speed of light", text, (name, v))
                gamma_box = (1,) if name in ("length_contraction", "time_dilation") else (0,)
                self.assertIsNone(self.chained_values(1, gamma_box), name)                  # no γ in the chained box

    def test_the_momentum_row_uses_the_speed_typed_in_row_1(self):
        from operator_row_math import row_tree
        self.place_chain("physics/physics/relativistic_momentum", {0: 1.5e8})
        row_tree.set_slot(self.app.rows[1]["node"], (1,), "2")
        self.app._sync_links()
        self.press_equals()
        self.assertEqual(float(row_tree.get_slot(self.app.rows[1]["node"], (2,))), 1.5e8)    # v on Row 2 is the v typed on Row 1

    # ---------- standard deviations and gravitational time dilation: Row 1 is an operator that already exists ----------
    def type_list(self, row, values):
        from operator_row_math import row_tree
        text = ", ".join(str(v) for v in values)
        row_tree.set_slot(self.app.rows[row]["node"], (0,), row_tree.advanced_slot("list", text, list(values), "[%s]" % text))

    def test_the_standard_deviation_in_two_rows_matches_todays_to_one_bit(self):
        """Row 1 is the variance, Row 2 its square root.  statistics.pstdev takes the square root of the exact fraction, so now and then (about one case in eight)
        sqrt(pvariance) is the neighbouring float: checked to one bit (2 ulp), never more."""
        import math
        import statistics
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        for key, today, variance in (("math/statistics_and_probability/standard_deviation", statistics.pstdev, statistics.pvariance),
                                     ("math/statistics_and_probability/sample_standard_deviation", statistics.stdev, statistics.variance)):
            for data in ([2, 4, 4, 4, 5, 5, 7, 9], [1, 2, 3, 4], [0.1, 0.2, 0.3], [10.5, 3.25, 7.0], [73.148457, -9.6, -63.067931, 26.0, -81.18], [5, 5]):
                self.app._clear_all()
                self.app._place_operator_row(key)
                self.app.update()
                self.type_list(0, data)
                self.press_equals()
                got = row_tree.evaluate(self.app.rows[1]["node"])
                expected = today(data)
                self.assertTrue(abs(got - expected) <= 2 * math.ulp(expected), (key, data, got, expected))
                self.assertEqual(got, math.sqrt(variance(data)), (key, data))               # the square root of Row 1's exact answer
                self.assertEqual(self.chained_values(1, (0,)), variance(data), (key, data))   # the chained box holds Row 1's exact answer

    def test_the_standard_deviations_decline_like_todays(self):
        key = "math/statistics_and_probability/sample_standard_deviation"
        self.place_chain(key, {})
        self.type_list(0, [5])                                                              # a sample of one number
        text = self.press_equals()
        self.assertIn("at least two data points", text)
        self.assertIsNone(self.chained_values(1, (0,)))
        self.app._clear_all()
        self.app._place_operator_row("math/statistics_and_probability/standard_deviation")  # no numbers typed at all
        text = self.press_equals()
        self.assertIn("Row 1", text)
        self.assertIsNone(self.chained_values(1, (0,)))

    def test_gravitational_time_dilation_in_two_rows_gives_todays_number(self):
        import math
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        today = library.get("physics/physics/gravitational_time_dilation").compute
        key = "physics/physics/gravitational_time_dilation"
        for dt, M, r in ((1000, 1.989e30, 6.957e8), (3600, 5.972e24, 6.371e6), (1, 1.989e30, 1e10), (2.5, 3e31, 5e8)):
            self.app._clear_all()
            self.place_chain(key, {0: M})
            row_tree.set_slot(self.app.rows[1]["node"], (0,), repr(dt))
            row_tree.set_slot(self.app.rows[1]["node"], (2,), repr(r))
            self.press_equals()
            got = row_tree.evaluate(self.app.rows[1]["node"])
            expected = today(dt, M, r)
            self.assertTrue(abs(got - expected) <= 2 * math.ulp(expected), (dt, M, r, got, expected))
            self.assertEqual(self.chained_values(1, (1,)), library.get("physics/physics/schwarzschild_radius").compute(M))      # the exact horizon radius

    def test_gravitational_time_dilation_declines_inside_the_horizon_with_todays_message(self):
        from operator_row_math import row_tree
        key = "physics/physics/gravitational_time_dilation"
        self.place_chain(key, {0: 1.989e30})                                                # the horizon of the Sun is about 2954 metres
        row_tree.set_slot(self.app.rows[1]["node"], (0,), "1000")
        row_tree.set_slot(self.app.rows[1]["node"], (2,), "2000")                           # r is inside it
        text = self.press_equals()
        self.assertIn("r must be outside the Schwarzschild radius", text)
        self.assertIsNotNone(self.chained_values(1, (1,)))                                   # Row 1 did not decline: its radius is in the chained box
        self.app._clear_all()
        self.place_chain(key, {})                                                           # Row 1 itself declines (its mass box is empty): the chained box stays empty
        row_tree.set_slot(self.app.rows[1]["node"], (0,), "1000")
        row_tree.set_slot(self.app.rows[1]["node"], (2,), "1e9")
        self.press_equals()
        self.assertIsNone(self.chained_values(1, (1,)))

    # ---------- three rows: range, interquartile range, variance of a random variable ----------
    def type_values(self, row, slot, values):
        from operator_row_math import row_tree
        text = ", ".join(str(v) for v in values)
        row_tree.set_slot(self.app.rows[row]["node"], (slot,), row_tree.advanced_slot("list", text, list(values), "[%s]" % text))

    def test_the_range_in_three_rows_is_exactly_todays_range(self):
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        today = library.get("math/statistics_and_probability/range").compute
        for data in ([4, 9, 1], [2.5, -7.25, 10.125, 3], [5], [0.1, 0.2, 0.3, 0.7], [-3, -1, -2]):
            self.app._clear_all()
            self.app._place_operator_row("math/statistics_and_probability/range")
            self.app.update()
            self.type_values(0, 0, data)
            self.press_equals()
            self.assertEqual(row_tree.evaluate(self.app.rows[2]["node"]), today(data), data)                # the same float
            self.assertEqual(self.chained_values(2, (0,)), max(data))                                        # Row 3 reads Row 1 ...
            self.assertEqual(self.chained_values(2, (1,)), min(data))                                        # ... and Row 2
            self.assertEqual(row_tree.get_slot(self.app.rows[1]["node"], (0,))["value"], list(data))        # Row 2's list is Row 1's list
            self.assertTrue(self.app.results.get("1.0", "end").strip().endswith(row_tree.fmt(today(data))))   # the answer of the whole chain is the last row's

    def test_an_empty_list_declines_in_the_range_and_nothing_is_chained(self):
        self.app._place_operator_row("math/statistics_and_probability/range")
        self.app.update()
        self.type_values(0, 0, [])
        text = self.press_equals()
        self.assertIn("Row 1", text)
        self.assertIsNone(self.chained_values(2, (0,)))
        self.assertIsNone(self.chained_values(2, (1,)))

    def test_the_interquartile_range_in_three_rows_is_exactly_todays(self):
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        today = library.get("math/statistics_and_probability/interquartile_range").compute
        for data in ([1, 2, 3, 4, 5, 6, 7, 8], [10.5, 3.25, 7.0, 8.75, 1.5], [1, 1, 2, 2, 3, 3], [73.148457, -9.6, -63.067931, 26.0, -81.18], [5, 9]):
            self.app._clear_all()
            self.app._place_operator_row("math/statistics_and_probability/interquartile_range")
            self.app.update()
            self.type_values(0, 0, data)
            self.press_equals()
            self.assertEqual(row_tree.evaluate(self.app.rows[2]["node"]), today(data), data)
            import statistics
            q = statistics.quantiles(data, n=4)
            self.assertEqual((self.chained_values(2, (0,)), self.chained_values(2, (1,))), (q[2], q[0]), data)    # Q3 from Row 1, Q1 from Row 2

    def test_an_empty_list_declines_in_the_interquartile_range(self):
        self.app._clear_all()
        self.app._place_operator_row("math/statistics_and_probability/interquartile_range")
        self.app.update()
        self.type_values(0, 0, [])
        text = self.press_equals()
        self.assertIn("Row 1", text)
        self.assertIsNone(self.chained_values(2, (0,)))

    def test_the_variance_of_a_random_variable_in_three_rows_matches_todays(self):
        """E[X²] from Row 2 and E[X] from Row 1.  Same operations as today's compute(), so the same float."""
        from operator_row_math import row_tree
        import operators_one_operator_per_file as library
        today = library.get("math/statistics_and_probability/variance_of_random_variable").compute
        for values, probs in (([0, 1], [0.5, 0.5]), ([1, 2, 3], [0.2, 0.3, 0.5]), ([-2.5, 0, 4.25, 10], [0.1, 0.4, 0.3, 0.2]), ([7], [1])):
            self.app._clear_all()
            self.app._place_operator_row("math/statistics_and_probability/variance_of_random_variable")
            self.app.update()
            self.type_values(0, 0, values)
            self.type_values(0, 1, probs)
            self.press_equals()
            self.assertEqual(row_tree.evaluate(self.app.rows[2]["node"]), today(values, probs), (values, probs))
            self.assertEqual(self.chained_values(2, (0,)), sum(x * x * p for x, p in zip(values, probs)))      # E[X²] is Row 2's answer
            self.assertEqual(self.chained_values(2, (1,)), sum(x * p for x, p in zip(values, probs)))          # E[X] is Row 1's answer
            self.assertEqual(row_tree.get_slot(self.app.rows[1]["node"], (1,))["value"], list(probs))          # Row 2 uses Row 1's probabilities

    def test_the_kalman_step_in_three_rows_gives_the_plan_numbers(self):
        """Row 1 predicts the state, Row 2 the variance, Row 3 updates: 10 + 2*3 = 16, 4 + 0 = 4, then 16 + 0.5 * (14 - 16) = 15."""
        from operator_row_math import row_tree
        self.app._clear_all()
        self.app._place_operator_row("physics/physics/kalman_update_state")
        self.app.update()
        for row, slot, text in ((0, 0, "10"), (0, 1, "2"), (0, 2, "3"), (1, 0, "4"), (1, 1, "0"), (2, 2, "14"), (2, 3, "4")):
            row_tree.set_slot(self.app.rows[row]["node"], (slot,), text)
        self.press_equals()
        self.assertEqual(row_tree.evaluate(self.app.rows[0]["node"]), 16)
        self.assertEqual(row_tree.evaluate(self.app.rows[1]["node"]), 4)
        self.assertEqual(self.chained_values(2, (0,)), 16)
        self.assertEqual(self.chained_values(2, (1,)), 4)
        self.assertEqual(row_tree.evaluate(self.app.rows[2]["node"]), 15)
        self.assertTrue(self.app.results.get("1.0", "end").strip().endswith("15"))
        # the one-row call of the same operator is the single update step
        import operators_one_operator_per_file as library
        self.assertEqual(library.get("physics/physics/kalman_update_state").compute(10, 4, 14, 4), 12)


    def test_the_pid_output_in_four_rows_gives_the_plan_numbers(self):
        """Kp 2, error 3, Ki 4, stored integral 1, time step 0.5, Kd 0.5, previous error 1: P = 6, I = 10, D = 2 and the output is 18."""
        from operator_row_math import row_tree
        self.app._clear_all()
        self.app._place_operator_row("physics/physics/pid_sum")
        self.app.update()
        for row, slot, text in ((0, 0, "2"), (0, 1, "3"), (1, 0, "4"), (1, 1, "1"), (1, 3, "0.5"), (2, 0, "0.5"), (2, 2, "1")):
            row_tree.set_slot(self.app.rows[row]["node"], (slot,), text)
        self.press_equals()
        self.assertEqual([row_tree.evaluate(self.app.rows[k]["node"]) for k in range(4)], [6, 10, 2, 18])
        self.assertEqual(row_tree.get_slot(self.app.rows[1]["node"], (2,)), "3")           # the error is copied from Row 1 ...
        self.assertEqual(row_tree.get_slot(self.app.rows[2]["node"], (1,)), "3")
        self.assertEqual(row_tree.get_slot(self.app.rows[2]["node"], (3,)), "0.5")         # ... and the time step of Row 3 from Row 2
        self.assertEqual([self.chained_values(3, (k,)) for k in range(3)], [6, 10, 2])
        self.assertTrue(self.app.results.get("1.0", "end").strip().endswith("18"))


    def test_the_gps_clock_in_four_rows_gives_the_plan_numbers(self):
        """Speed 3874, radii 6378137 and 26561750: Row 2 is -7.2137..., Row 3 is 45.6518..., and the correction is 38.4381... microseconds a day."""
        from operator_row_math import row_tree
        self.app._clear_all()
        self.app._place_operator_row("physics/physics/gps_clock_correction")
        self.app.update()
        for row, slot, text in ((0, 0, "3874"), (2, 0, "6378137"), (2, 1, "26561750")):
            row_tree.set_slot(self.app.rows[row]["node"], (slot,), text)
        self.press_equals()
        values = [row_tree.evaluate(self.app.rows[k]["node"]) for k in range(4)]
        self.assertAlmostEqual(values[1], -7.213755992552251, places=9)
        self.assertAlmostEqual(values[2], 45.651861866919695, places=9)
        self.assertAlmostEqual(values[3], 38.438105874367444, places=9)
        self.assertEqual(self.chained_values(1, (0,)), values[0])                            # the gamma box holds Row 1's answer
        self.assertEqual((self.chained_values(3, (0,)), self.chained_values(3, (1,))), (values[1], values[2]))
        self.assertTrue(self.app.results.get("1.0", "end").strip().endswith(row_tree.fmt(values[3])))

    def test_the_relativity_operators_say_when_they_do_not_matter(self):
        for key in ("lorentz_factor", "time_dilation", "length_contraction", "relativistic_momentum", "relativistic_kinetic_energy"):
            node = row_tree.new_node("physics/physics/" + key)
            self.assertIn("negligible below about 1 percent of the speed of light", " ".join(c for _l, c in row_tree.words(node)), key)


    def test_the_answer_of_the_chain_is_the_last_rows_answer(self):
        self.place_chain("geometry/geometry/heron_s_formula", {0: 3, 1: 4, 2: 5})
        text = self.press_equals()
        self.assertIn("→", text)
        self.assertTrue(text.strip().endswith("6"))                           # not 6 + 6 or 6 = 6: the area, the last row's answer

    def test_a_row_may_only_read_an_earlier_row(self):
        from operator_row_math import multirow_specs
        self.assertEqual(multirow_specs.chain_errors(), [])
        saved = dict(multirow_specs.SPECS)
        try:
            multirow_specs.SPECS["bad/later"] = {"title": "x", "joins": ["→"], "rows": [{"op": "_number", "fill": {0: {"chain": 1}}}, {"op": "_number"}]}
            multirow_specs.SPECS["bad/self"] = {"title": "x", "joins": ["→"], "rows": [{"op": "_number"}, {"op": "_number", "fill": {0: {"chain": 1}}}]}
            problems = multirow_specs.chain_errors()
            self.assertEqual(len(problems), 2)
            self.assertTrue(all("earlier row" in p for p in problems))
        finally:
            multirow_specs.SPECS.clear()
            multirow_specs.SPECS.update(saved)

    def test_a_join_key_moves_on_to_the_next_row_so_one_plus_one_is_two(self):
        """1  +  1  =  : after the + the next digits are Row 2's number, not more digits of Row 1's (which made 11)."""
        app = self.app
        app._key("1")
        app._join_key("+")
        app._key("1")
        self.assertEqual(app.rows[0]["node"]["slots"], ["1"])
        self.assertEqual(app.rows[1]["node"]["slots"], ["1"])
        self.assertEqual(app.rows[1]["join"], "+")
        self.assertEqual(app.op_target, 1)
        app._equals()
        self.assertIn("=  2", app.results.get("1.0", "end"))

    def test_a_second_join_key_starts_the_next_row_so_one_plus_one_plus_one_is_three(self):
        app = self.app
        app._key("1")
        app._join_key("+")
        app._key("1")
        app._join_key("+")
        app._key("1")
        self.assertEqual([r["node"]["slots"] for r in app.rows[:3]], [["1"], ["1"], ["1"]])
        self.assertEqual([r["join"] for r in app.rows[:3]], [None, "+", "+"])
        app._equals()
        self.assertIn("=  3", app.results.get("1.0", "end"))
        self.assertEqual(app.rows[3]["is_result"], True)                      # the answer sits in Row 4

    def test_a_join_key_pressed_twice_with_no_number_between_only_changes_the_symbol(self):
        app = self.app
        app._key("1")
        app._join_key("+")
        count = len(app.rows)
        app._join_key("−")
        self.assertEqual(app.rows[1]["join"], "−")
        self.assertEqual(len(app.rows), count)

    def test_the_old_way_still_works_next_row_then_the_join_key(self):
        app = self.app
        app._key("1")
        app._next_row()
        app._key("2")
        app._join_key("×")
        app._equals()
        self.assertIn("=  2", app.results.get("1.0", "end"))                     # 1 x 2
        self.assertEqual(app.rows[0]["node"]["slots"], ["1"])
        self.assertEqual(app.rows[1]["node"]["slots"], ["2"])

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

    def test_math_on_several_lines_is_still_one_row(self):
        """A fraction or an exponent is drawn on several lines, but all of them are Row 1: no extra calculator rows, = calculates the whole of Row 1 and prints in Row 2,
        and Next Row goes from Row 1 to Row 2."""
        app = self.app
        before = len(app.rows)
        app._place_operator_row("physics/physics/gravitation")                # F = G m1 m2 / r^2: a fraction with an exponent
        self.assertEqual(len(app.rows), before)                                # the lines of the fraction are not rows
        self.assertTrue(any(f for f in row_tree.fracs(app.rows[0]["node"])))   # it is drawn as a fraction ...
        self.assertTrue(any(l for l in row_tree.levels(app.rows[0]["node"])))   # ... with an exponent on its own line
        for path, text in zip(self.paths(), ("5", "2", "3", "4")):               # boxes on the different lines are all boxes of Row 1
            self.type_into(path, text)
        app._equals()
        self.assertTrue(app.rows[0]["result"].cget("text").startswith("7.4155"))        # the answer stays on Row 1, in its own answer card right of the =
        self.assertEqual([i for i, r in enumerate(app.rows) if r["is_result"]], [])      # nothing is printed into Row 2
        app._next_row()
        self.assertEqual(app.op_target + 1, 2)                                   # Next Row: Row 1 -> Row 2
        # Row 2 with a join sign: = shows each row's own answer in its own card and the answer for both on Row 3
        app._place_operator_row("math/arithmetic/addition")
        for path, text in zip(self.paths_of(1), ("1", "2")):
            app.rows[1]["sel"] = path
            for ch in text:
                app._key(ch)
        app._join_key("+")
        app._equals()
        self.assertEqual([i for i, r in enumerate(app.rows) if r["is_result"]], [2])    # the joined answer is in Row 3
        self.assertEqual(app.rows[1]["result"].cget("text"), "3")                        # Row 2's own answer stays in Row 2

    def test_a_picture_that_hides_inputs_still_calculates_through_extra_boxes(self):
        app = self.app
        app._place_operator_row("math/abstract_algebra/kernel")
        self.assertEqual([t for k, t, _p in app._cards(0) if k == "op"], ["ker", "with", ","])
        self.assertEqual(len(self.paths()), 3)                          # phi, G, identity


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)

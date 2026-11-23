"""Tests for algebra word problem generator compatibility and safety protections.

Verifies:
1. CLI destination argument enforcement and safety guards against repo writes.
2. Preflight validation of catalog problems and explicit row synchronization specs.
3. Isolated generation byte-for-byte fidelity with the repository for all 479 problems,
   all 479 row modules, JPEG diagrams, and INDEX.md.
4. Correct reproduction of the 4 verified SLOTS mappings for times_as_old_future_sum:
   - age/0001: SLOTS = [0, 1, 0, 2]
   - age/0004: SLOTS = [0, 1, 0, 2]
   - age/0005: SLOTS = [0, 1, 0, 2]
   - age/0007: SLOTS = [1, 0, 1, 2]
"""
import copy
import filecmp
import io
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from operator_keys.make_algebra_word_problem_files import (
    EXPLICIT_ROW_SYNCHRONIZATION,
    LIB,
    ROOT as GEN_ROOT,
    ROWS,
    generate_all,
    is_protected_destination,
    main,
    read_problems,
    row_file,
    slug,
    validate_preflight,
)


class GeneratorSafetyAndCliTests(unittest.TestCase):
    """Test CLI protections, destination checks, and preflight validation."""

    def test_cli_requires_destination(self):
        """main(argv=[]) must exit with status 1 and write error to stderr."""
        stderr_capture = io.StringIO()
        old_stderr = sys.stderr
        try:
            sys.stderr = stderr_capture
            with self.assertRaises(SystemExit) as cm:
                main(argv=[])
            self.assertEqual(cm.exception.code, 1)
            err_msg = stderr_capture.getvalue()
            self.assertIn("Error: An explicit output directory is required.", err_msg)
            self.assertIn("Direct generation into the live repository is prohibited.", err_msg)
        finally:
            sys.stderr = old_stderr

    def test_protected_destination_detection(self):
        """is_protected_destination must flag ROOT, LIB, ROWS, and nested paths."""
        self.assertTrue(is_protected_destination(ROOT))
        self.assertTrue(is_protected_destination(LIB))
        self.assertTrue(is_protected_destination(ROWS))
        self.assertTrue(is_protected_destination(os.path.join(ROOT, "operators_one_algebra_word_problem_per_file")))
        self.assertTrue(is_protected_destination(os.path.join(ROOT, "operator_row_math_for_algebra_word_problems")))
        self.assertTrue(is_protected_destination(os.path.join(LIB, "age", "0001")))
        self.assertTrue(is_protected_destination(os.path.join(ROWS, "age", "0001")))

    def test_generate_all_rejects_empty_or_protected_destinations(self):
        """generate_all must raise ValueError on empty or repo destinations."""
        with self.assertRaises(ValueError):
            generate_all(None)
        with self.assertRaises(ValueError):
            generate_all("")
        with self.assertRaises(ValueError):
            generate_all(ROOT)
        with self.assertRaises(ValueError):
            generate_all(LIB)
        with self.assertRaises(ValueError):
            generate_all(ROWS)

    def test_preflight_passes_on_valid_catalog(self):
        """Preflight must succeed on the untouched catalog and explicit specs."""
        problems = read_problems()
        self.assertEqual(len(problems), 479)
        validate_preflight(problems, EXPLICIT_ROW_SYNCHRONIZATION)

    def test_preflight_detects_mismatched_equation(self):
        """Preflight must fail if equation text in problem does not match spec."""
        problems = read_problems()
        bad_problems = copy.deepcopy(problems)
        for p in bad_problems:
            if p["id"] == "0001" and p["category"] == "Age":
                p["Equation"] = "(x + 5) + (4x + 6) = 105"
                break
        with self.assertRaises(ValueError) as cm:
            validate_preflight(bad_problems, EXPLICIT_ROW_SYNCHRONIZATION)
        self.assertIn("Mismatched equation for age/0001", str(cm.exception))

    def test_preflight_detects_mismatched_repeat_token(self):
        """Preflight must fail if repeat token does not match expected value."""
        bad_specs = copy.deepcopy(EXPLICIT_ROW_SYNCHRONIZATION)
        bad_specs["age/0001"]["expected_token"] = "99"
        problems = read_problems()
        with self.assertRaises(ValueError) as cm:
            validate_preflight(problems, bad_specs)
        self.assertIn("Expected static token", str(cm.exception))

    def test_preflight_detects_invalid_slot_mapping(self):
        """Preflight must fail if slots reference nonexistent underlying slot."""
        bad_specs = copy.deepcopy(EXPLICIT_ROW_SYNCHRONIZATION)
        bad_specs["age/0001"]["slots"] = [0, 1, 0, 5]
        problems = read_problems()
        with self.assertRaises(ValueError) as cm:
            validate_preflight(problems, bad_specs)
        self.assertIn("Invalid slot index", str(cm.exception))

    def test_preflight_detects_missing_underlying_slot(self):
        """Preflight must fail if any underlying slot index is omitted."""
        bad_specs = copy.deepcopy(EXPLICIT_ROW_SYNCHRONIZATION)
        bad_specs["age/0001"]["slots"] = [0, 0, 0, 1]
        problems = read_problems()
        with self.assertRaises(ValueError) as cm:
            validate_preflight(problems, bad_specs)
        self.assertIn("Not all underlying slots represented", str(cm.exception))

    def test_preflight_detects_mismatched_kinds_metadata(self):
        """Preflight must fail if KINDS metadata length does not match DEFAULTS."""
        bad_specs = copy.deepcopy(EXPLICIT_ROW_SYNCHRONIZATION)
        bad_specs["number_puzzle/0576"]["kinds"] = ["number"]  # expected 2
        problems = read_problems()
        with self.assertRaises(ValueError) as cm:
            validate_preflight(problems, bad_specs)
        self.assertIn("Length of KINDS", str(cm.exception))

    def test_preflight_detects_out_of_bounds_box_index(self):
        """Preflight must fail if BOX_INDEX references a nonexistent problem number."""
        bad_specs = copy.deepcopy(EXPLICIT_ROW_SYNCHRONIZATION)
        bad_specs["number_puzzle/0576"]["box_index"] = [0, 99]
        problems = read_problems()
        with self.assertRaises(ValueError) as cm:
            validate_preflight(problems, bad_specs)
        self.assertIn("BOX_INDEX entries out of bounds", str(cm.exception))


class GeneratorReproductionTests(unittest.TestCase):
    """Test full isolated generation and reproduction fidelity."""

    @classmethod
    def setUpClass(cls):
        """Run isolated generation once into a temporary directory."""
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.counts = generate_all(cls.temp_dir.name)
        cls.gen_lib = os.path.join(cls.temp_dir.name, "operators_one_algebra_word_problem_per_file")
        cls.gen_rows = os.path.join(cls.temp_dir.name, "operator_row_math_for_algebra_word_problems")
        cls.problems = read_problems()

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def test_generated_counts(self):
        """Generator counts must match catalog status: 478 Ready, 1 Reference."""
        self.assertEqual(len(self.problems), 479)
        self.assertEqual(self.counts["word_solver"], 463)
        self.assertEqual(self.counts["number_puzzle"], 15)
        self.assertEqual(self.counts[None], 1)
        self.assertEqual(self.counts["word_solver"] + self.counts["number_puzzle"], 478)

    def test_all_problem_files_byte_for_byte_identical(self):
        """All 479 generated problem Python files must match the repository files."""
        mismatches = []
        for p in self.problems:
            cat = slug(p["category"])
            pid = p["id"]
            live_path = os.path.join(LIB, cat, pid, f"{pid}.py")
            gen_path = os.path.join(self.gen_lib, cat, pid, f"{pid}.py")
            if not os.path.exists(gen_path):
                mismatches.append(("missing", f"{cat}/{pid}"))
            elif not filecmp.cmp(live_path, gen_path, shallow=False):
                mismatches.append(("diff", f"{cat}/{pid}"))
        self.assertEqual(mismatches, [], "Problem files with differences: %r" % mismatches)

    def test_all_row_files_byte_for_byte_identical(self):
        """All 479 generated row Python files must match the repository files."""
        mismatches = []
        for p in self.problems:
            cat = slug(p["category"])
            pid = p["id"]
            live_path = os.path.join(ROWS, cat, pid, f"{pid}.py")
            gen_path = os.path.join(self.gen_rows, cat, pid, f"{pid}.py")
            if not os.path.exists(gen_path):
                mismatches.append(("missing", f"{cat}/{pid}"))
            elif not filecmp.cmp(live_path, gen_path, shallow=False):
                mismatches.append(("diff", f"{cat}/{pid}"))
        self.assertEqual(mismatches, [], "Row files with differences: %r" % mismatches)

    def test_index_markdown_byte_for_byte_identical(self):
        """Generated INDEX.md must match the repository INDEX.md byte-for-byte."""
        live_index = os.path.join(LIB, "INDEX.md")
        gen_index = os.path.join(self.gen_lib, "INDEX.md")
        self.assertTrue(filecmp.cmp(live_index, gen_index, shallow=False), "INDEX.md differs")

    def test_all_diagrams_byte_for_byte_identical(self):
        """All 479 problem JPEG diagrams must match the repository files byte-for-byte."""
        mismatches = []
        for p in self.problems:
            cat = slug(p["category"])
            pid = p["id"]
            live_jpg = os.path.join(LIB, cat, pid, f"{pid}.jpg")
            gen_jpg = os.path.join(self.gen_lib, cat, pid, f"{pid}.jpg")
            if not os.path.exists(gen_jpg):
                mismatches.append(("missing", f"{cat}/{pid}.jpg"))
            elif not filecmp.cmp(live_jpg, gen_jpg, shallow=False):
                mismatches.append(("diff", f"{cat}/{pid}.jpg"))
        self.assertEqual(mismatches, [], "JPEG diagrams with differences: %r" % mismatches)

    def test_synchronized_rows_structure(self):
        """Verify the synchronized rows have SLOTS and correct box cards."""
        expected = {
            "age/0001": ([0, 1, 0, 2], [1, 0, 2], ["5", "4", "105"], 4),
            "age/0004": ([0, 1, 0, 2], [1, 0, 2], ["6", "2", "33"], 4),
            "age/0005": ([0, 1, 0, 2], [1, 0, 2], ["10", "3", "68"], 4),
            "age/0007": ([1, 0, 1, 2], [0, 1, 2], ["3", "3", "82"], 4),
            "number_puzzle/0576": ([0, 1, 1], [0, 1], ["3", "43"], 3),
            "number_puzzle/0579": ([0, 1, 1], [0, 1], ["4", "42"], 3),
            "number_puzzle/0591": ([0, 1, 1], [0, 1], ["3", "15"], 3),
            "number_puzzle/0597": ([0, 1, 1], [0, 1], ["3", "38"], 3),
            "number_puzzle/0607": ([0, 1, 1], [0, 1], ["2", "25"], 3),
            "work_rate/0970": ([0, 1, 0], [0, 1], ["4", "12"], 3),
            "work_rate/0972": ([0, 1, 0], [0, 1], ["6", "12"], 3),
            "work_rate/0987": ([0, 1, 0], [0, 1], ["3", "6"], 3),
            "work_rate/0995": ([0, 1, 0], [0, 1], ["3", "4"], 3),
            "work_rate/0997": ([0, 1, 0], [0, 1], ["3", "12"], 3),
            "ratio/0782": ([0, 1, 2, 1, 3, 4], [0, 2, 1, 3, 4], ["3", "12", "5", "1", "7"], 6),
            "ratio/0793": ([0, 1, 2, 1, 3, 4], [0, 2, 1, 3, 4], ["3", "16", "5", "1", "7"], 6),
            "ratio/0802": ([0, 1, 2, 1, 3, 4], [0, 2, 1, 3, 4], ["5", "18", "6", "2", "9"], 6),
            "ratio/0809": ([0, 1, 2, 1, 3, 4], [0, 2, 1, 3, 4], ["6", "16", "5", "4", "7"], 6),
            "distance_average_speed/0115": ([0, 1, 2, 1, 3], [1, 0, 2, 3], ["30", "1", "55", "50"], 5),
            "distance_average_speed/0117": ([0, 1, 2, 1, 3], [1, 0, 2, 3], ["60", "2", "45", "55"], 5),
            "distance_average_speed/0120": ([0, 1, 2, 1, 3], [1, 0, 2, 3], ["30", "2", "75", "45"], 5),
            "distance_average_speed/0121": ([0, 1, 2, 1, 3], [1, 0, 2, 3], ["50", "1", "45", "46"], 5),
            "distance_average_speed/0124": ([0, 1, 2, 1, 3], [1, 0, 2, 3], ["60", "3", "75", "66"], 5),
        }
        for key, (exp_slots, exp_box_index, exp_defaults, exp_box_count) in expected.items():
            cat, pid = key.split("/")
            gen_path = os.path.join(self.gen_rows, cat, pid, f"{pid}.py")
            with open(gen_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn(f"SLOTS = {exp_slots}", content, f"{key} missing SLOTS")
            self.assertIn(f"BOX_INDEX = {exp_box_index}", content, f"{key} BOX_INDEX mismatch")
            self.assertIn(f"DEFAULTS = {exp_defaults}", content, f"{key} DEFAULTS mismatch")
            ns = {"__file__": gen_path}
            exec(content, ns)
            boxes = [c for c in ns["LEFT"] if c[0] == "box"]
            self.assertEqual(len(boxes), exp_box_count, f"{key} must have exactly {exp_box_count} box cards in LEFT")
            self.assertEqual(ns["SLOTS"], exp_slots, f"{key} SLOTS mismatch")
            self.assertEqual(ns["BOX_INDEX"], exp_box_index, f"{key} BOX_INDEX mismatch")
            self.assertEqual(ns["DEFAULTS"], exp_defaults, f"{key} DEFAULTS mismatch")


if __name__ == "__main__":
    unittest.main()

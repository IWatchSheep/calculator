"""Builds the two algebra word problem folders from algebra_word_problems/algebra_word_problems.txt.

    operators_one_algebra_word_problem_per_file/<category>/<id>/<id>.py   the problem, its steps, its answer and compute(...)
    operators_one_algebra_word_problem_per_file/<category>/<id>/<id>.jpg  a diagram of the problem (the equation drawn with number boxes)
    operators_one_algebra_word_problem_per_file/INDEX.md                  one line per problem
    operator_row_math_for_algebra_word_problems/<category>/<id>/<id>.py   how the problem is laid out as a row of cards in the calculator

Safety requirement: An explicit output directory outside the repository is required.
Direct generation into the live repository is prohibited to prevent accidental overwrites.

Run it from the project folder into a target directory (e.g., in a temporary directory or staging build folder):

    .venv\\Scripts\\python.exe operator_keys\\make_algebra_word_problem_files.py <output_directory>
"""
import os
import re
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "algebra_word_problems", "algebra_word_problems.txt")
MATCHER = os.path.join(ROOT, "algebra_word_problems", "algebra_matcher")
LIB = os.path.join(ROOT, "operators_one_algebra_word_problem_per_file")
ROWS = os.path.join(ROOT, "operator_row_math_for_algebra_word_problems")
sys.path.insert(0, MATCHER)

import number_puzzle as NP  # noqa: E402
import word_solver as WS  # noqa: E402

NUMBER = re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?")
BOX = "\u25a1"

EXPLICIT_ROW_SYNCHRONIZATION = {
    "age/0001": {
        "equation": "(x + 5) + (4x + 5) = 105",
        "repeat_token": 10,
        "expected_token": "5",
        "slots": [0, 1, 0, 2],
        "slots_comment": "boxes 0 and 2 share slot 0 (elapsed years)",
        "box_index": [1, 0, 2],
        "defaults": ["5", "4", "105"],
        "inputs": ["number 2", "number 1", "number 3"],
        "kinds": ["number", "number", "number"],
    },
    "age/0004": {
        "equation": "(x + 6) + (2x + 6) = 33",
        "repeat_token": 10,
        "expected_token": "6",
        "slots": [0, 1, 0, 2],
        "slots_comment": "boxes 0 and 2 share slot 0 (elapsed years)",
        "box_index": [1, 0, 2],
        "defaults": ["6", "2", "33"],
        "inputs": ["number 2", "number 1", "number 3"],
        "kinds": ["number", "number", "number"],
    },
    "age/0005": {
        "equation": "(x + 10) + (3x + 10) = 68",
        "repeat_token": 10,
        "expected_token": "10",
        "slots": [0, 1, 0, 2],
        "slots_comment": "boxes 0 and 2 share slot 0 (elapsed years)",
        "box_index": [1, 0, 2],
        "defaults": ["10", "3", "68"],
        "inputs": ["number 2", "number 1", "number 3"],
        "kinds": ["number", "number", "number"],
    },
    "age/0007": {
        "equation": "(x + 3) + (3x + 3) = 82",
        "repeat_token": 10,
        "expected_token": "3",
        "slots": [1, 0, 1, 2],
        "slots_comment": "boxes 0 and 2 share slot 1 (elapsed years); box 1 is slot 0 (multiplier)",
        "box_index": [0, 1, 2],
        "defaults": ["3", "3", "82"],
        "inputs": ["number 1", "number 2", "number 3"],
        "kinds": ["number", "number", "number"],
    },
    "number_puzzle/0576": {
        "equation": "3x − 43 = x + 43",
        "repeat_token": 7,
        "expected_token": "43",
        "slots": [0, 1, 1],
        "slots_comment": "box 0 is slot 0 (multiplier); boxes 1 and 2 share slot 1 (transferred money)",
        "box_index": [0, 1],
        "defaults": ["3", "43"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "number_puzzle/0579": {
        "equation": "4x − 42 = x + 42",
        "repeat_token": 7,
        "expected_token": "42",
        "slots": [0, 1, 1],
        "slots_comment": "box 0 is slot 0 (multiplier); boxes 1 and 2 share slot 1 (transferred money)",
        "box_index": [0, 1],
        "defaults": ["4", "42"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "number_puzzle/0591": {
        "equation": "3x − 15 = x + 15",
        "repeat_token": 7,
        "expected_token": "15",
        "slots": [0, 1, 1],
        "slots_comment": "box 0 is slot 0 (multiplier); boxes 1 and 2 share slot 1 (transferred money)",
        "box_index": [0, 1],
        "defaults": ["3", "15"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "number_puzzle/0597": {
        "equation": "3x − 38 = x + 38",
        "repeat_token": 7,
        "expected_token": "38",
        "slots": [0, 1, 1],
        "slots_comment": "box 0 is slot 0 (multiplier); boxes 1 and 2 share slot 1 (transferred money)",
        "box_index": [0, 1],
        "defaults": ["3", "38"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "number_puzzle/0607": {
        "equation": "2x − 25 = x + 25",
        "repeat_token": 7,
        "expected_token": "25",
        "slots": [0, 1, 1],
        "slots_comment": "box 0 is slot 0 (multiplier); boxes 1 and 2 share slot 1 (transferred money)",
        "box_index": [0, 1],
        "defaults": ["2", "25"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "work_rate/0970": {
        "equation": "4/12 + 4/x = 1",
        "repeat_token": 4,
        "expected_token": "4",
        "slots": [0, 1, 0],
        "slots_comment": "boxes 0 and 2 share slot 0 (working-together time); box 1 is slot 1 (partner alone time)",
        "box_index": [0, 1],
        "defaults": ["4", "12"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "work_rate/0971": {
        "equation": "2/4 + t/4 + t/8 = 1",
        "repeat_token": 6,
        "expected_token": "4",
        "slots": [0, 1, 1, 2],
        "slots_comment": "boxes 1 and 2 share slot 1 (first worker total hours alone)",
        "box_index": [2, 0, 1],
        "defaults": ["2", "4", "8"],
        "inputs": ["number 3", "number 1", "number 2"],
        "kinds": ["number", "number", "number"],
    },
    "work_rate/0974": {
        "equation": "2/5 + t/5 + t/15 = 1",
        "repeat_token": 6,
        "expected_token": "5",
        "slots": [0, 1, 1, 2],
        "slots_comment": "boxes 1 and 2 share slot 1 (first worker total hours alone)",
        "box_index": [2, 0, 1],
        "defaults": ["2", "5", "15"],
        "inputs": ["number 3", "number 1", "number 2"],
        "kinds": ["number", "number", "number"],
    },
    "work_rate/0980": {
        "equation": "2/4 + t/4 + t/12 = 1",
        "repeat_token": 6,
        "expected_token": "4",
        "slots": [0, 1, 1, 2],
        "slots_comment": "boxes 1 and 2 share slot 1 (first worker total hours alone)",
        "box_index": [2, 0, 1],
        "defaults": ["2", "4", "12"],
        "inputs": ["number 3", "number 1", "number 2"],
        "kinds": ["number", "number", "number"],
    },
    "work_rate/0991": {
        "equation": "1/4 + t/4 + t/12 = 1",
        "repeat_token": 6,
        "expected_token": "4",
        "slots": [0, 1, 1, 2],
        "slots_comment": "boxes 1 and 2 share slot 1 (first worker total hours alone)",
        "box_index": [2, 0, 1],
        "defaults": ["1", "4", "12"],
        "inputs": ["number 3", "number 1", "number 2"],
        "kinds": ["number", "number", "number"],
    },
    "work_rate/1000": {
        "equation": "1/12 + t/12 + t/3 = 1",
        "repeat_token": 6,
        "expected_token": "12",
        "slots": [0, 1, 1, 2],
        "slots_comment": "boxes 1 and 2 share slot 1 (first worker total hours alone)",
        "box_index": [2, 0, 1],
        "defaults": ["1", "12", "3"],
        "inputs": ["number 3", "number 1", "number 2"],
        "kinds": ["number", "number", "number"],
    },
    "work_rate/0972": {
        "equation": "6/12 + 6/x = 1",
        "repeat_token": 4,
        "expected_token": "6",
        "slots": [0, 1, 0],
        "slots_comment": "boxes 0 and 2 share slot 0 (working-together time); box 1 is slot 1 (partner alone time)",
        "box_index": [0, 1],
        "defaults": ["6", "12"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "work_rate/0987": {
        "equation": "3/6 + 3/x = 1",
        "repeat_token": 4,
        "expected_token": "3",
        "slots": [0, 1, 0],
        "slots_comment": "boxes 0 and 2 share slot 0 (working-together time); box 1 is slot 1 (partner alone time)",
        "box_index": [0, 1],
        "defaults": ["3", "6"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "work_rate/0995": {
        "equation": "3/4 + 3/x = 1",
        "repeat_token": 4,
        "expected_token": "3",
        "slots": [0, 1, 0],
        "slots_comment": "boxes 0 and 2 share slot 0 (working-together time); box 1 is slot 1 (partner alone time)",
        "box_index": [0, 1],
        "defaults": ["3", "4"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "work_rate/0997": {
        "equation": "3/12 + 3/x = 1",
        "repeat_token": 4,
        "expected_token": "3",
        "slots": [0, 1, 0],
        "slots_comment": "boxes 0 and 2 share slot 0 (working-together time); box 1 is slot 1 (partner alone time)",
        "box_index": [0, 1],
        "defaults": ["3", "12"],
        "inputs": ["number 1", "number 2"],
        "kinds": ["number", "number"],
    },
    "ratio/0782": {
        "equation": "(3k − 12)/(5k + 12) = 1/7",
        "repeat_token": 11,
        "expected_token": "12",
        "slots": [0, 1, 2, 1, 3, 4],
        "slots_comment": "boxes 1 and 3 share slot 1 (transferred marbles)",
        "box_index": [0, 2, 1, 3, 4],
        "defaults": ["3", "12", "5", "1", "7"],
        "inputs": ["number 1", "number 3", "number 2", "number 4", "number 5"],
        "kinds": ["number", "number", "number", "number", "number"],
    },
    "ratio/0793": {
        "equation": "(3k − 16)/(5k + 16) = 1/7",
        "repeat_token": 11,
        "expected_token": "16",
        "slots": [0, 1, 2, 1, 3, 4],
        "slots_comment": "boxes 1 and 3 share slot 1 (transferred marbles)",
        "box_index": [0, 2, 1, 3, 4],
        "defaults": ["3", "16", "5", "1", "7"],
        "inputs": ["number 1", "number 3", "number 2", "number 4", "number 5"],
        "kinds": ["number", "number", "number", "number", "number"],
    },
    "ratio/0802": {
        "equation": "(5k − 18)/(6k + 18) = 2/9",
        "repeat_token": 11,
        "expected_token": "18",
        "slots": [0, 1, 2, 1, 3, 4],
        "slots_comment": "boxes 1 and 3 share slot 1 (transferred marbles)",
        "box_index": [0, 2, 1, 3, 4],
        "defaults": ["5", "18", "6", "2", "9"],
        "inputs": ["number 1", "number 3", "number 2", "number 4", "number 5"],
        "kinds": ["number", "number", "number", "number", "number"],
    },
    "ratio/0809": {
        "equation": "(6k − 16)/(5k + 16) = 4/7",
        "repeat_token": 11,
        "expected_token": "16",
        "slots": [0, 1, 2, 1, 3, 4],
        "slots_comment": "boxes 1 and 3 share slot 1 (transferred marbles)",
        "box_index": [0, 2, 1, 3, 4],
        "defaults": ["6", "16", "5", "4", "7"],
        "inputs": ["number 1", "number 3", "number 2", "number 4", "number 5"],
        "kinds": ["number", "number", "number", "number", "number"],
    },
    "distance_average_speed/0115": {
        "equation": "(30×1 + 55t)/(1 + t) = 50",
        "repeat_token": 10,
        "expected_token": "1",
        "slots": [0, 1, 2, 1, 3],
        "slots_comment": "boxes 1 and 3 share slot 1 (first-leg hours)",
        "box_index": [1, 0, 2, 3],
        "defaults": ["30", "1", "55", "50"],
        "inputs": ["number 2", "number 1", "number 3", "number 4"],
        "kinds": ["number", "number", "number", "number"],
    },
    "distance_average_speed/0117": {
        "equation": "(60×2 + 45t)/(2 + t) = 55",
        "repeat_token": 10,
        "expected_token": "2",
        "slots": [0, 1, 2, 1, 3],
        "slots_comment": "boxes 1 and 3 share slot 1 (first-leg hours)",
        "box_index": [1, 0, 2, 3],
        "defaults": ["60", "2", "45", "55"],
        "inputs": ["number 2", "number 1", "number 3", "number 4"],
        "kinds": ["number", "number", "number", "number"],
    },
    "distance_average_speed/0120": {
        "equation": "(30×2 + 75t)/(2 + t) = 45",
        "repeat_token": 10,
        "expected_token": "2",
        "slots": [0, 1, 2, 1, 3],
        "slots_comment": "boxes 1 and 3 share slot 1 (first-leg hours)",
        "box_index": [1, 0, 2, 3],
        "defaults": ["30", "2", "75", "45"],
        "inputs": ["number 2", "number 1", "number 3", "number 4"],
        "kinds": ["number", "number", "number", "number"],
    },
    "distance_average_speed/0121": {
        "equation": "(50×1 + 45t)/(1 + t) = 46",
        "repeat_token": 10,
        "expected_token": "1",
        "slots": [0, 1, 2, 1, 3],
        "slots_comment": "boxes 1 and 3 share slot 1 (first-leg hours)",
        "box_index": [1, 0, 2, 3],
        "defaults": ["50", "1", "45", "46"],
        "inputs": ["number 2", "number 1", "number 3", "number 4"],
        "kinds": ["number", "number", "number", "number"],
    },
    "distance_average_speed/0124": {
        "equation": "(60×3 + 75t)/(3 + t) = 66",
        "repeat_token": 10,
        "expected_token": "3",
        "slots": [0, 1, 2, 1, 3],
        "slots_comment": "boxes 1 and 3 share slot 1 (first-leg hours)",
        "box_index": [1, 0, 2, 3],
        "defaults": ["60", "3", "75", "66"],
        "inputs": ["number 2", "number 1", "number 3", "number 4"],
        "kinds": ["number", "number", "number", "number"],
    },
    "rational_equation/0813": {
        "equation": "1590/(p + 40) = 1350/(p − 40)",
        "repeat_token": 13,
        "expected_token": "40",
        "slots": [0, 1, 2, 1],
        "slots_comment": "boxes 1 and 3 share slot 1 (wind speed)",
        "box_index": [0, 1, 2],
        "defaults": ["1590", "40", "1350"],
        "inputs": ["number 1", "number 2", "number 3"],
        "kinds": ["number", "number", "number"],
    },
    "distance_round_trip/0143": {
        "equation": "60/s + 60/(s + 15) = 10/3",
        "repeat_token": 4,
        "expected_token": "60",
        "slots": [0, 0, 1, 2, 3],
        "slots_comment": "boxes 0 and 1 share slot 0 (distance)",
        "box_index": [0, 1, 2, 3],
        "defaults": ["60", "15", "10", "3"],
        "inputs": ["number 1", "number 2", "number 3", "number 4"],
        "kinds": ["number", "number", "number", "number"],
    },
    "mixture/0533": {
        "equation": "0.25x + 0.5(100 − x) = 0.39(100)",
        "repeat_token": 12,
        "expected_token": "100",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (total mixture volume)",
        "box_index": [2],
        "defaults": ["100"],
        "inputs": ["number 3"],
        "kinds": ["number"],
    },
    "mixture/0544": {
        "equation": "0.1x + 0.5(20 − x) = 0.16(20)",
        "repeat_token": 12,
        "expected_token": "20",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (total mixture weight)",
        "box_index": [2],
        "defaults": ["20"],
        "inputs": ["number 3"],
        "kinds": ["number"],
    },
    "mixture/0547": {
        "equation": "0.6x + 0.7(40 − x) = 0.65(40)",
        "repeat_token": 12,
        "expected_token": "40",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (total mixture volume)",
        "box_index": [2],
        "defaults": ["40"],
        "inputs": ["number 3"],
        "kinds": ["number"],
    },
    "mixture/0561": {
        "equation": "0.5x + 0.6(30 − x) = 0.54(30)",
        "repeat_token": 12,
        "expected_token": "30",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (total mixture volume)",
        "box_index": [2],
        "defaults": ["30"],
        "inputs": ["number 3"],
        "kinds": ["number"],
    },
    "mixture/0566": {
        "equation": "0.1x + 0.9(20 − x) = 0.54(20)",
        "repeat_token": 12,
        "expected_token": "20",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (total mixture weight)",
        "box_index": [2],
        "defaults": ["20"],
        "inputs": ["number 3"],
        "kinds": ["number"],
    },
    "mixture/0535": {
        "equation": "0.3(4) = 0.05(4 + w)",
        "repeat_token": 7,
        "expected_token": "4",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (original solution volume)",
        "box_index": [0],
        "defaults": ["4"],
        "inputs": ["number 1"],
        "kinds": ["number"],
    },
    "mixture/0541": {
        "equation": "0.8(6) = 0.12(6 + w)",
        "repeat_token": 7,
        "expected_token": "6",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (concentrate batch volume)",
        "box_index": [0],
        "defaults": ["6"],
        "inputs": ["number 1"],
        "kinds": ["number"],
    },
    "mixture/0536": {
        "equation": "0.06(30) = 0.15(30 − e)",
        "repeat_token": 7,
        "expected_token": "30",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (original salt water volume)",
        "box_index": [0],
        "defaults": ["30"],
        "inputs": ["number 1"],
        "kinds": ["number"],
    },
    "mixture/0538": {
        "equation": "0.3(4) + x = 0.8(4 + x)",
        "repeat_token": 9,
        "expected_token": "4",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (initial antifreeze volume)",
        "box_index": [0],
        "defaults": ["4"],
        "inputs": ["number 1"],
        "kinds": ["number"],
    },
    "mixture/0539": {
        "equation": "0.5(20 − x) + x = 0.7(20)",
        "repeat_token": 11,
        "expected_token": "20",
        "slots": [0, 0],
        "slots_comment": "boxes 0 and 1 share slot 0 (radiator capacity)",
        "box_index": [0],
        "defaults": ["20"],
        "inputs": ["number 1"],
        "kinds": ["number"],
    },
}


def is_protected_destination(path):
    """True if path resolves to or is inside any protected repository directory (ROOT, LIB, ROWS)."""
    if not path:
        return False
    target = os.path.realpath(os.path.abspath(path))
    for protected in (LIB, ROWS, ROOT):
        prot_real = os.path.realpath(os.path.abspath(protected))
        if target == prot_real:
            return True
        try:
            rel = os.path.relpath(target, prot_real)
            if not rel.startswith("..") and rel != ".":
                return True
        except ValueError:
            pass
        try:
            rel = os.path.relpath(prot_real, target)
            if not rel.startswith("..") and rel != ".":
                return True
        except ValueError:
            pass
    return False


def validate_preflight(problems, explicit_specs):
    """Validate all catalog problems and explicit specifications BEFORE any file is created or written."""
    if len(problems) != 479:
        raise ValueError("Expected 479 problems, found %d" % len(problems))
    problems_by_key = {"%s/%s" % (slug(p["category"]), p["id"]): p for p in problems}
    for key, spec in explicit_specs.items():
        if key not in problems_by_key:
            raise ValueError("Explicit synchronization key %r not found in catalog." % key)
        p = problems_by_key[key]
        if p["Equation"] != spec["equation"]:
            raise ValueError("Mismatched equation for %s: expected %r, found %r" % (key, spec["equation"], p["Equation"]))
        template, numbers = template_of(p["Problem"])
        cards, orig_box_index, pattern, levels, fracs = row_cards(equation_plan(p["Equation"], numbers))
        rep_idx = spec["repeat_token"]
        if rep_idx >= len(cards):
            raise ValueError("Repeat token index %d out of range for %s" % (rep_idx, key))
        kind, val = cards[rep_idx]
        if kind != "op" or val != spec["expected_token"]:
            raise ValueError("Expected static token ('op', %r) at index %d for %s, found %r" % (spec["expected_token"], rep_idx, key, (kind, val)))
        if not all(0 <= idx < len(numbers) for idx in spec["box_index"]):
            raise ValueError("BOX_INDEX entries out of bounds for %s (%d text numbers)" % (key, len(numbers)))
        if spec["box_index"] != orig_box_index:
            raise ValueError("Mismatched BOX_INDEX for %s: expected %r, found %r" % (key, spec["box_index"], orig_box_index))
        expected_defaults = [numbers[i] for i in spec["box_index"]]
        if spec["defaults"] != expected_defaults:
            raise ValueError("Mismatched DEFAULTS for %s: expected %r, found %r" % (key, spec["defaults"], expected_defaults))
        if len(spec["inputs"]) != len(spec["defaults"]):
            raise ValueError("Length of INPUTS must match DEFAULTS for %s" % key)
        kinds = spec.get("kinds", ["number"] * len(spec["defaults"]))
        if len(kinds) != len(spec["defaults"]):
            raise ValueError("Length of KINDS (%d) must match DEFAULTS (%d) for %s" % (len(kinds), len(spec["defaults"]), key))
        if not (len(spec["box_index"]) == len(spec["defaults"]) == len(spec["inputs"]) == len(kinds)):
            raise ValueError("Metadata length invariant len(BOX_INDEX) == len(DEFAULTS) == len(INPUTS) == len(KINDS) violated for %s" % key)
        slots = spec["slots"]
        expected_box_count = sum(1 for k, _ in cards if k == "box") + 1
        if len(slots) != expected_box_count:
            raise ValueError("Length of SLOTS (%d) must match total box cards (%d) for %s" % (len(slots), expected_box_count, key))
        if not all(0 <= s < len(spec["defaults"]) for s in slots):
            raise ValueError("Invalid slot index in %r for %s" % (slots, key))
        if set(slots) != set(range(len(spec["defaults"]))):
            raise ValueError("Not all underlying slots represented in %r for %s" % (slots, key))
        if len(spec["defaults"]) < 1:
            raise ValueError("Expected at least 1 underlying slot for %s, found %d" % (key, len(spec["defaults"])))


def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def read_problems():
    with open(SOURCE, encoding="utf-8") as f:
        text = f.read()
    out = []
    for block in re.split(r"\n-{20,}\n", text):
        m = re.search(r"^#(\d{4}) \[([^\]]+)\]\n(.*)", block, flags=re.S | re.M)       # (the first block also holds the file's header)
        if not m:
            continue
        fields = {}
        for line in m.group(3).splitlines():
            k, _, v = line.partition(": ")
            if k in ("Problem", "Let", "Equation", "Solve", "Answer"):
                fields[k] = v.strip()
        if len(fields) == 5:
            out.append({"id": m.group(1), "category": m.group(2), **fields})
    return out


def template_of(problem):
    """The problem text with every number replaced by {0}, {1}, ...; also the numbers as written."""
    numbers, parts, last = [], [], 0
    for m in NUMBER.finditer(problem):
        parts.append(problem[last:m.start()].replace("{", "{{").replace("}", "}}"))
        parts.append("{%d}" % len(numbers))
        numbers.append(m.group(0).replace(",", ""))
        last = m.end()
    parts.append(problem[last:].replace("{", "{{").replace("}", "}}"))
    return "".join(parts), numbers


def equation_plan(equation, numbers):
    """The equation as tokens: ('txt', text) or ('num', text, i).  A number of the equation is a BOX only when it is one of the numbers written in the problem text
    (same value, matched left to right, each text number used once); i is that number's place in the text.  Any other number (the 1 and 2 of x + (x + 1) + (x + 2),
    a 0.75 that stands for 75%) stays plain text: it is not blue in the picture and not a box in the row.  Text numbers that no equation number matches (the 3 in
    "the sum of 3 consecutive integers") are not boxes either: compute() keeps them as written."""
    used, out, last = set(), [], 0

    def add(kind, text, index=None):
        if kind == "txt" and out and out[-1][0] == "txt":
            out[-1] = ("txt", out[-1][1] + text)
        elif kind == "txt":
            out.append(("txt", text))
        else:
            out.append(("num", text, index))

    for m in NUMBER.finditer(equation):
        if equation[last:m.start()]:
            add("txt", equation[last:m.start()])
        value = Fraction(m.group(0).replace(",", ""))
        i = next((j for j, n in enumerate(numbers) if j not in used and Fraction(n) == value), None)
        if i is None:
            add("txt", m.group(0))
        else:
            used.add(i)
            add("num", m.group(0), i)
        last = m.end()
    if equation[last:]:
        add("txt", equation[last:])
    return out


def equation_parts(plan):
    """The plan cut at each ';' (an equation with several parts is drawn one part per line)."""
    parts = [[]]
    for tok in plan:
        if tok[0] == "txt" and ";" in tok[1]:
            pieces = tok[1].split(";")
            parts[-1].append(("txt", pieces[0]))
            for piece in pieces[1:]:
                parts.append([("txt", piece)])
        else:
            parts[-1].append(tok)
    out = []
    for part in parts:
        part = [t for t in part]
        if part and part[0][0] == "txt":
            part[0] = ("txt", part[0][1].lstrip())
        if part and part[-1][0] == "txt":
            part[-1] = ("txt", part[-1][1].rstrip())
        part = [t for t in part if t[0] == "num" or t[1]]
        if part:
            out.append(part)
    return out


def solver_of(problem):
    """('word_solver', family) / ('number_puzzle', 'number_puzzle') / (None, None): who answers this problem today."""
    r = WS.solve(problem)
    if r is not None:
        return "word_solver", r.family
    if NP.solve(problem) is not None:
        return "number_puzzle", "number_puzzle"
    return None, None


# ------------------------------------------------------------------------------------------------------------
# the picture
# ------------------------------------------------------------------------------------------------------------
def make_picture(path, p, numbers):
    from PIL import Image, ImageDraw, ImageFont
    font_dir = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")

    def font(name, size):
        for candidate in (os.path.join(font_dir, name), os.path.join(font_dir, "arial.ttf")):
            try:
                return ImageFont.truetype(candidate, size)
            except OSError:
                continue
        return ImageFont.load_default()

    f_title, f_text, f_small, f_num, f_bold = font("segoeui.ttf", 16), font("segoeui.ttf", 21), font("segoeui.ttf", 17), font("segoeuib.ttf", 21), font("segoeuib.ttf", 21)
    width, pad = 900, 28
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))

    def wrap(text, fnt, limit):
        lines, cur = [], ""
        for word in text.split(" "):
            trial = (cur + " " + word).strip()
            if probe.textlength(trial, font=fnt) <= limit or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
        return lines

    problem_lines = wrap(p["Problem"], f_text, width - 2 * pad)
    let_lines = wrap("Let: " + p["Let"], f_small, width - 2 * pad)
    answer_lines = wrap("Answer: " + p["Answer"], f_bold, width - 2 * pad)
    equations = equation_parts(equation_plan(p["Equation"], numbers))

    sys.path.insert(0, ROOT)
    from operator_row_math.row_builder import _plan

    def stacked_part(tokens):
        """One part of the equation on a grid exactly like the row's: a fraction has its numerator above the bar and its denominator below, an exponent is one row up.
        Returns (grid rows, [(grid row, column, kind, text, pixel width)], [(grid row, first column, last column)] of the bars, column widths)."""
        cards, _, _, levels, fracs = row_cards(tokens)
        texts = [t[1] for t in tokens if t[0] == "num"]
        shown_texts, k = [], 0
        for kind, text in cards:
            if kind == "box":
                shown_texts.append(texts[k])
                k += 1
            else:
                shown_texts.append(text)
        placed, bars, _end = _plan(len(cards), levels, fracs)
        ncols = max([c for r, c in placed.values()] + [0]) + 1
        colw = [0] * (ncols + 1)
        for i, (r, c) in placed.items():
            w = probe.textlength(shown_texts[i], font=f_num if cards[i][0] == "box" else f_text) + (22 if cards[i][0] == "box" else 6)
            colw[c] = max(colw[c], w)
        for r, c, w in bars:
            for cc in range(c, c + w):
                colw[cc] = max(colw[cc], 14)
        top = min([r for r, c in placed.values()] + [r for r, c, w in bars])
        bottom = max([r for r, c in placed.values()] + [r for r, c, w in bars])
        items = [(r - top, c, cards[i][0], shown_texts[i]) for i, (r, c) in placed.items()]
        return bottom - top + 1, items, [(r - top, c, c + w - 1) for r, c, w in bars], colw

    eq_blocks = [stacked_part(e) for e in equations]
    need = max([sum(blk[3]) + 10 * len(blk[3]) for blk in eq_blocks] + [width - 2 * pad]) + 2 * pad
    width = max(width, int(need))
    cell = 46
    height = pad + 24 + 14 + 30 * len(problem_lines) + 10 + 24 * len(let_lines) + 18
    height += sum(cell * blk[0] + 16 for blk in eq_blocks) + 14 + 32 * len(answer_lines) + pad - 6

    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)
    y = pad - 8
    d.text((pad, y), "Algebra word problem %s   \u00b7   %s" % (p["id"], p["category"]), font=f_title, fill="#777777")
    y += 30
    d.line((pad, y, width - pad, y), fill="#dddddd")
    y += 14
    for line in problem_lines:
        d.text((pad, y), line, font=f_text, fill="#222222")
        y += 30
    y += 10
    for line in let_lines:
        d.text((pad, y), line, font=f_small, fill="#4a5a78")
        y += 24
    y += 18
    for nrows, items, bars, colw in eq_blocks:
        xs, x = [], pad
        for w in colw:
            xs.append(x)
            x += w + 10
        for r, c, kind, text in items:
            w, cy = colw[c], y + r * cell + 20
            if kind == "box":
                bw = probe.textlength(text, font=f_num) + 22
                x0 = xs[c] + (w - bw) / 2
                d.rounded_rectangle((x0 + 2, cy - 20, x0 + bw - 2, cy + 20), radius=5, fill="#d6e6fb", outline="#2a6ec9", width=2)
                d.text((x0 + bw / 2, cy), text, font=f_num, fill="#1b3f7a", anchor="mm")
            else:
                d.text((xs[c] + w / 2, cy), text, font=f_text, fill="#222222", anchor="mm")
        for r, c0, c1 in bars:
            by = y + r * cell + 20
            d.line((xs[c0], by, xs[c1] + colw[c1], by), fill="#222222", width=2)
        y += cell * nrows + 16
    y += 14
    for line in answer_lines:
        d.text((pad, y), line, font=f_bold, fill="#2a6a20")
        y += 32
    img.save(path, "JPEG", quality=82, optimize=True)


# ------------------------------------------------------------------------------------------------------------
# the files
# ------------------------------------------------------------------------------------------------------------
def py_str(text):
    return repr(text)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def problem_file(p, key, template, numbers, solver, family):
    status = ("ready: %s answers it (compute(...) solves it with any numbers the solver accepts)" % family) if solver else "reference only: no solver answers it yet (compute(...) raises)"
    return '''"""Algebra word problem %(id)s   [%(category)s]

Problem : %(problem)s
Let     : %(let)s
Equation: %(equation)s
Solve   : %(solve)s
Answer  : %(answer)s

Status  : %(status)s
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = %(id_r)s
KEY = %(key_r)s
NAME = %(name_r)s
CATEGORY = %(category_r)s
PROBLEM = %(problem_r)s
LET = %(let_r)s
EQUATION = %(equation_r)s
SOLVE = %(solve_r)s
ANSWER = %(answer_r)s
# who answers it today:  \"word_solver\" (a family in algebra_word_problems/algebra_matcher/word_solver.py), \"number_puzzle\", or None (reference only)
SOLVER = %(solver_r)s
FAMILY = %(family_r)s
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = %(template_r)s
NUMBERS = %(numbers_r)s


def compute(*numbers):
    \"\"\"Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers).\"\"\"
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
''' % {
        "id": p["id"], "category": p["category"], "problem": p["Problem"], "let": p["Let"], "equation": p["Equation"], "solve": p["Solve"], "answer": p["Answer"],
        "status": status, "id_r": py_str(p["id"]), "key_r": py_str(key), "name_r": py_str("%s %s" % (p["category"], p["id"])), "category_r": py_str(p["category"]),
        "problem_r": py_str(p["Problem"]), "let_r": py_str(p["Let"]), "equation_r": py_str(p["Equation"]), "solve_r": py_str(p["Solve"]), "answer_r": py_str(p["Answer"]),
        "solver_r": py_str(solver), "family_r": py_str(family), "template_r": py_str(template), "numbers_r": py_str(numbers)}


TOKEN = re.compile(NUMBER.pattern + r"|[A-Za-z]{2,}|\S")      # a word of 2+ letters (pay) is ONE card, never p a y


def row_cards(plan):
    """The row's cards from the plan, ONE TOKEN PER CARD (a card's centre shows one symbol): a blue box is a box card; a number that is not a box, a letter, + - x / = ( ) ;
    each is an operator card of its own; an exponent or subscript is its own card one grid row up or down.  Returns (cards, box_index, pattern, levels)."""
    sys.path.insert(0, ROOT)
    from operator_row_math.layout import level_of, shown
    cards, box_index, pattern, levels = [], [], [], []
    for tok in plan:
        if tok[0] == "txt":
            for m in TOKEN.finditer(tok[1]):
                cards.append(("op", shown(m.group(0))))
                levels.append(level_of(m.group(0)))
                pattern.append(m.group(0))
        else:
            cards.append(("box", ""))
            levels.append(0)
            box_index.append(tok[2])
            pattern.append(BOX)
    from operator_row_math.layout import group_fractions
    return cards, box_index, " ".join(pattern), levels, group_fractions(cards, levels)


def row_file(p, key, numbers, solver):
    cards, box_index, pattern, levels, fracs = row_cards(equation_plan(p["Equation"], numbers))
    spec = EXPLICIT_ROW_SYNCHRONIZATION.get(key)
    if spec is not None:
        rep_idx = spec["repeat_token"]
        cards[rep_idx] = ("box", "")
        pattern_tokens = pattern.split(" ")
        pattern_tokens[rep_idx] = BOX
        pattern = " ".join(pattern_tokens)
        from operator_row_math.layout import group_fractions
        fracs = group_fractions(cards, levels)
        slots_line = "SLOTS = %s    # box cards to input slots: %s\n" % (spec["slots"], spec["slots_comment"])
        inputs_r = py_str(spec["inputs"])
        box_index_r = py_str(spec["box_index"])
        defaults_r = py_str(spec["defaults"])
        kinds_r = py_str(["number"] * len(spec["defaults"]))
    else:
        slots_line = ""
        inputs_r = py_str(["number %d" % (i + 1) for i in box_index])
        box_index_r = py_str(box_index)
        defaults_r = py_str([numbers[i] for i in box_index])
        kinds_r = py_str(["number"] * len(box_index))

    boxes = pattern
    left = repr(cards)
    return '''"""Row for the algebra word problem: %(category)s %(id)s

Picture:      %(boxes)s   (the equation of the problem; each box is a number of the problem text; the answer is right of =)
Calculation:  %(calc_text)s
Try it:       python operator_row_math_for_algebra_word_problems/preview.py %(key)s
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = %(name_r)s
KEY = %(key_r)s
LIBRARY_KEY = %(key_r)s    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = %(pattern_r)s
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = %(calc_r)s
INPUTS = %(inputs_r)s    # what each box (left to right, as in the equation) is: which number of the problem text it holds
BOX_INDEX = %(box_index_r)s    # the place of each box's number in the problem text (NUMBERS of the problem file); the other text numbers stay as written
DEFAULTS = %(defaults_r)s    # the boxes' numbers as written in the stored problem
%(slots_line)sKINDS = %(kinds_r)s    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
FRAC = %(frac_r)s    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
LEVELS = %(levels_r)s    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript (one row down), 0 = on the line
LEFT = %(left)s      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=LEVELS, fracs=FRAC)
''' % {
        "category": p["category"], "id": p["id"], "name": "%s %s" % (p["category"], p["id"]), "boxes": boxes, "box": BOX, "key": key,
        "calc_text": "ready - fill the boxes, press = and the answer appears right of =" if solver else "reference - the problem is stored; no solver answers it yet",
        "name_r": py_str("%s %s" % (p["category"], p["id"])), "key_r": py_str(key),
        "pattern_r": py_str("%s  ->  answer %s" % (pattern, BOX)), "calc_r": py_str("ready" if solver else "reference"),
        "inputs_r": inputs_r, "box_index_r": box_index_r, "defaults_r": defaults_r,
        "slots_line": slots_line,
        "kinds_r": kinds_r, "left": left, "levels_r": py_str(levels), "frac_r": py_str([[list(e) for e in f] for f in fracs])}


def generate_all(dest_dir):
    """Generate all 479 problem files, diagrams, row files, and index into dest_dir.
    dest_dir must be an explicit, safe path outside the live repository."""
    if not dest_dir:
        raise ValueError("Explicit output directory required. Direct generation into the repository is prohibited.")
    if is_protected_destination(dest_dir):
        raise ValueError("Destination %r resolves to or overlaps with protected repository directories." % dest_dir)

    problems = read_problems()
    validate_preflight(problems, EXPLICIT_ROW_SYNCHRONIZATION)

    out_lib = os.path.join(dest_dir, "operators_one_algebra_word_problem_per_file")
    out_rows = os.path.join(dest_dir, "operator_row_math_for_algebra_word_problems")
    if is_protected_destination(out_lib) or is_protected_destination(out_rows):
        raise ValueError("Derived output directories overlap with protected repository directories.")

    index = {}
    counts = {"word_solver": 0, "number_puzzle": 0, None: 0}
    for n, p in enumerate(problems, 1):
        cat = slug(p["category"])
        key = "%s/%s" % (cat, p["id"])
        template, numbers = template_of(p["Problem"])
        solver, family = solver_of(p["Problem"])
        counts[solver] += 1
        folder = os.path.join(out_lib, cat, p["id"])
        write(os.path.join(folder, p["id"] + ".py"), problem_file(p, key, template, numbers, solver, family))
        make_picture(os.path.join(folder, p["id"] + ".jpg"), p, numbers)
        write(os.path.join(out_rows, cat, p["id"], p["id"] + ".py"), row_file(p, key, numbers, solver))
        index.setdefault(p["category"], []).append((p, key, solver, family))
        if n % 100 == 0:
            print("%d / %d" % (n, len(problems)))

    lines = ["# Algebra word problem index", "",
             "One folder per problem, holding `<id>.py` (the problem, its steps, its answer and `compute(...)`) and `<id>.jpg` (a diagram of the problem).",
             "**Ready** = a solver answers it today (`compute(...)` works); **Reference** = the problem and its steps are stored, no solver answers it yet.",
             "Written by `operator_keys/make_algebra_word_problem_files.py`; the solver column comes from `algebra_word_problems/algebra_matcher/word_solver.py`.",
             "One wording is stored once. Further numbers for that wording are a slider on the unknown, not another stored problem.", "",
             "%d problems: %d ready (%d word_solver, %d number_puzzle), %d reference." % (
                 len(problems), counts["word_solver"] + counts["number_puzzle"], counts["word_solver"], counts["number_puzzle"], counts[None]), ""]
    for category in sorted(index):
        lines += ["## %s" % category, "", "| Id | Problem | Answer | Status | Solver | Folder |", "|---|---|---|---|---|---|"]
        for p, key, solver, family in index[category]:
            prob = p["Problem"].replace("|", "\\|")
            lines.append("| %s | %s | %s | %s | %s | `%s/` |" % (p["id"], prob, p["Answer"].replace("|", "\\|"), "Ready" if solver else "Reference", family or "", key))
        lines.append("")
    write(os.path.join(out_lib, "INDEX.md"), "\n".join(lines))
    return counts


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Error: An explicit output directory is required.", file=sys.stderr)
        print("Usage: python make_algebra_word_problem_files.py <output_directory>", file=sys.stderr)
        print("Direct generation into the live repository is prohibited.", file=sys.stderr)
        sys.exit(1)
    dest_dir = argv[0]
    counts = generate_all(dest_dir)
    print("done:", counts)


if __name__ == "__main__":
    main()

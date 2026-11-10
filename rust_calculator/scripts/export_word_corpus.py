"""Writes rust_calculator/tests/word_corpus.jsonl: the parity corpus for the Rust word solver.

    python rust_calculator/scripts/export_word_corpus.py

It runs the Python test suite of the word solver with the solver wrapped, so EVERY problem text the tests feed it (the 1,000 generated problems, all the fresh
sets, the unit-test phrasings, the declines) is recorded.  For each text it stores what every family function returns, what solve() returns, and what
number_puzzle.solve() returns, so the Rust port can be compared with Python family by family:

    {"p": text, "fam": [[function name, family label, [values as "n/d"], equation, reading], ...], "solve": [name, [values]] | null, "np": [answer, equation, reading] | null}

Values are exact fractions written "n/d" (or "n").  Run again whenever word_solver.py changes.
"""
import io
import json
import os
import sys
import unittest
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MATCHER = os.path.join(ROOT, "algebra_word_problems", "algebra_matcher")
OUT = os.path.join(ROOT, "rust_calculator", "tests", "word_corpus.jsonl")
sys.path.insert(0, MATCHER)
sys.path.insert(0, os.path.join(ROOT, "operator_keys"))
os.chdir(MATCHER)

import number_puzzle as NP  # noqa: E402
import word_solver as WS  # noqa: E402

SEEN = {}


def fraction_text(v):
    v = Fraction(v)
    return str(v.numerator) if v.denominator == 1 else "%d/%d" % (v.numerator, v.denominator)


def record(problem):
    if isinstance(problem, str):
        SEEN[problem] = True


def wrap(fn):
    def inner(problem, *args, **kwargs):
        record(problem)
        return fn(problem, *args, **kwargs)
    inner.__name__ = fn.__name__
    return inner


# record every problem handed to solve(), to a family function or to the number-puzzle reader
for i, fam in enumerate(WS.FAMILIES):
    wrapped = wrap(fam)
    WS.FAMILIES[i] = wrapped
    setattr(WS, fam.__name__, wrapped)
_original_solve = WS.solve
WS.solve = wrap(_original_solve)
NP.solve = wrap(NP.solve)

suite = unittest.defaultTestLoader.loadTestsFromNames(["test_word_solver", "test_number_puzzle"])
result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
if not result.wasSuccessful():
    raise SystemExit("the Python tests fail; fix them first")

# the 1,000 generated problems too (the tests read them, but be sure)
import make_algebra_word_problem_files as G  # noqa: E402

for p in G.read_problems():
    record(p["Problem"])

problems = sorted(SEEN, key=lambda s: (len(s), s))
lines = []
for p in problems:
    if "\n" in p or "\t" in p or "\r" in p:
        continue
    fams = []
    for fam in WS.FAMILIES:
        try:
            r = fam(p)
        except (ZeroDivisionError, ValueError, KeyError, IndexError):
            r = None
        if r is not None:
            fams.append([fam.__name__, r.family, [fraction_text(v) for v in r.values], r.equation, r.reading])
    solved = _original_solve(p)
    np_ = NP.solve(p)
    lines.append(json.dumps({
        "p": p,
        "fam": fams,
        "solve": None if solved is None else [solved.family, [fraction_text(v) for v in solved.values]],
        "np": None if np_ is None else [fraction_text(np_.answer), np_.equation, np_.reading],
    }, ensure_ascii=False))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines) + "\n")
claimed = sum(1 for l in lines if json.loads(l)["fam"])
print("wrote %s: %d problems, %d claimed by some family, %d by number_puzzle" % (os.path.relpath(OUT, ROOT), len(lines), claimed, sum(1 for l in lines if json.loads(l)["np"])))

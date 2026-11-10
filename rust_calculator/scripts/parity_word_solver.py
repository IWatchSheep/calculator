"""Compare Rust word_solver::solve to Python word_solver.solve on sample problems.

Run from repo root after `cargo build --release`:
  python rust_calculator/scripts/parity_word_solver.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MATCHER = os.path.join(ROOT, "algebra_word_problems", "algebra_matcher")
sys.path.insert(0, MATCHER)

import word_solver as WS  # noqa: E402

SAMPLES = [
    "The sum of two numbers is 235 and their difference is 103. Find the numbers.",
    "The sum of 3 consecutive even integers is 84. What are the integers?",
    "Elena can clean the house in 4 hours. Vera can do it in 6 hours. How long will it take them working together?",
    "A TV is marked down 25% to $450. What was the original price?",
    "If 5 pens cost $12.50, how much do 12 pens cost?",
    "Five less than twice a number is 31. Find it.",
]


def py_values(problem: str):
    r = WS.solve(problem)
    if r is None:
        return None
    return [str(Fraction(v)) for v in r.values]


def main() -> int:
    bin_path = os.path.join(ROOT, "rust_calculator", "target", "release", "word_solver_cli.exe")
    alt = os.path.join(ROOT, "rust_calculator", "target", "release", "word_solver_cli")
    exe = bin_path if os.path.exists(bin_path) else alt
    if not os.path.exists(exe):
        print("Build the word_solver_cli example/bin first; skipping Rust side.")
        for p in SAMPLES:
            print(p, "->", py_values(p))
        return 0
    bad = 0
    for p in SAMPLES:
        py = py_values(p)
        out = subprocess.check_output([exe, p], text=True).strip()
        rust = None if out == "None" else json.loads(out)
        if py != rust:
            bad += 1
            print("MISMATCH:", p)
            print("  py  ", py)
            print("  rust", rust)
        else:
            print("ok:", py)
    print("mismatches:", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

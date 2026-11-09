"""Prints what the word solver does NOT yet claim among the 1,000 generated problems, grouped by category and by wording shape.

Run from this folder:   python todo_report.py            (the full list)
                        python todo_report.py --counts   (only the numbers: claimed / wrong / unclaimed)

A "wording shape" is a problem with its numbers replaced by # and its names by N, so every generated template shows up once with how many problems use it.
The text file algebra_word_problems_status.txt in the main project folder keeps the same list as its appendix: regenerate the appendix with this script
whenever a family is added (see the UPDATE PROTOCOL at the top of that file).
"""
import collections
import re
import sys
from fractions import Fraction

import word_solver as WS
from test_number_puzzle import load_problems

NAMES = set("Ava Ben Carla Dev Elena Finn Grace Hiro Isla Jamal Kira Leo Maya Noah Omar Priya Quinn Rosa Sam Tara Umar Vera Wes Xena Yusuf Zoe Aiden Bea Caleb Dana Emeka "
            "Fatima Gus Hana Ivan Jade Kofi Lena Mateo Nia Oscar Pablo Rhea Sofia Theo Uma Victor Wren Yara Zane".split())


def shape(text):
    text = re.sub(r"\$?[\d,]+(?:\.\d+)?", "#", text)
    return " ".join("N" if w.strip(".,?!;:'") in NAMES else w for w in text.split())[:90]


def main():
    problems = load_problems()
    claimed, wrong = 0, 0
    groups = collections.OrderedDict()
    for p in problems:
        r = WS.solve(p["problem"])
        if r is None:
            g = groups.setdefault((p["cat"], shape(p["problem"])), [0, p["id"], p["problem"]])
            g[0] += 1
        else:
            claimed += 1
    print("generated problems: %d   claimed by the word solver: %d   unclaimed: %d   distinct unclaimed wording shapes: %d   families: %d"
          % (len(problems), claimed, len(problems) - claimed, len(groups), len(WS.FAMILIES)))
    print("(the number of WRONG claims is checked by test_word_solver.py: GroundTruth.test_never_wrong_on_generated_problems, it must stay 0)")
    if "--counts" in sys.argv:
        return
    by_cat = collections.Counter()
    for (cat, _), g in groups.items():
        by_cat[cat] += g[0]
    print()
    print("UNCLAIMED BY CATEGORY (problems):")
    for cat, n in sorted(by_cat.items(), key=lambda kv: (-kv[1], kv[0])):
        print("  %3d  %s" % (n, cat))
    print()
    print("UNCLAIMED WORDING SHAPES (category | problems | first id | example):")
    for (cat, _), g in sorted(groups.items(), key=lambda kv: (kv[0][0], -kv[1][0])):
        print("  %s | %d | %s | %s" % (cat, g[0], g[1], g[2][:120]))


if __name__ == "__main__":
    main()

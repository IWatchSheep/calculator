"""Writes archive_families.json: a solver family for every wording the word archive proved, when it can be made safe.

    python make_archive_families.py

For each proven wording (word_archive.json, written by word_archive.py) this
  1. gives every number written in the equation a role that is the SAME in every problem of the wording: the i-th number of the problem, N[i], or a fixed number;
     a wording where a role is ambiguous (two problem numbers are equal in every problem), or one number of the problem is used nowhere, is left alone;
  2. solves the equation exactly for every stored problem (archive_families.roots) and takes the root that is one of the stored answer's numbers;
  3. gives every number of the stored answer (in the order it is written) a recipe in that root and the problem's numbers, the same in every problem of the wording:
     x, a number of the problem, x + c, x - c, c - x, c x, x / c, c / x, or c x + d (c and d fixed numbers or numbers of the problem);
  4. runs the finished family on every problem of the wording and keeps it only when each one returns exactly its stored answer (what test_word_solver compares).
A wording that fails any step is written to archive_families_skipped.txt with the reason; nothing is guessed.  Run word_archive.py first if the problems changed.
"""
import collections
import itertools
import json
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import archive_families as AF  # noqa: E402
import word_archive as WA  # noqa: E402

NUMRE = r"\d+(?:\.\d+)?"
OUT = os.path.join(HERE, "archive_families.json")
SKIPPED = os.path.join(HERE, "archive_families_skipped.txt")


def answer_values(text):
    """The numbers of a stored answer in the order they are written, as test_word_solver.GroundTruth.numbers_of reads a plain answer."""
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"(?<=\d),(?=\d{3})", "", text)
    return [Fraction(x) for x in re.findall(r"-?\d+(?:\.\d+)?(?:/\d+)?", text)]


def plain_answer(text):
    """True when numbers_of would use the plain rule for this answer (the special cases of the older families are not this file's business)."""
    return not re.search(r"\$[\d,.]+ each|\$[\d,.]+ at \d|^\d+ (?:weeks|months|days) \(each will have|\d\s?(?:lb|kg) at \$|\d\s?(?:L|kg) of|^x = -?\d", text) \
        and len(re.findall(r"(\d+(?:\.\d+)?)\s+(?:[a-z]+\s+)?at\s+[$\d]", text)) != 2


def literal_roles(norms, number_lists):
    """Per written number of the equation: ('idx', i), ('fixed', value), or None when the roles are not the same in every problem / are ambiguous."""
    counts = {len(re.findall(NUMRE, n)) for n in norms}
    if len(counts) != 1:
        return None, "the equations do not have the same numbers"
    roles = []
    for j in range(counts.pop()):
        possible, values = None, set()
        for norm, numbers in zip(norms, number_lists):
            literal = Fraction(re.findall(NUMRE, norm)[j])
            values.add(literal)
            here = {i for i, n in enumerate(numbers) if Fraction(n.replace(",", "")) == literal}
            possible = here if possible is None else possible & here
        if possible:
            if len(possible) > 1:
                return None, "ambiguous role (problem numbers %s are equal in every problem)" % sorted(possible)
            if len(values) == 1 and len(norms) > 1:
                return None, "ambiguous role (the number %s is the same in every stored problem, so it could be a fixed number)" % next(iter(values))
            roles.append(("idx", next(iter(possible))))
        elif len(values) == 1:
            roles.append(("fixed", next(iter(values))))
        else:
            return None, "a number of the equation is not a number of the problem and not fixed"
    return roles, None


def expression(norm, roles, start):
    """The normalised equation side with each written number replaced by N[i] / F('c'); returns (text, next role index)."""
    parts, j = [], start
    for piece in re.findall(NUMRE + r"|[^\d]+", norm):
        if re.fullmatch(NUMRE, piece):
            kind, v = roles[j]
            j += 1
            parts.append("N[%d]" % v if kind == "idx" else "F('%s')" % v)
        else:
            parts.append(piece)
    return "".join(parts), j


def display_template(original, roles):
    """The stored equation with each number that is a problem number written as {i}."""
    j = [0]

    def sub(m):
        kind, v = roles[j[0]]
        j[0] += 1
        return "{%d}" % v if kind == "idx" else m.group(0)
    return re.sub(NUMRE, sub, original)


def forms(x_values, n_lists, a_values):
    """Recipes (text) that give a_values[p] for every problem p, simplest first."""
    P = range(len(x_values))
    n_count = len(n_lists[0])

    def consistent(const_of):
        """const_of(p) -> needed constant; returns an expression text for it ('N[i]' / 'F(c)') when the same in every problem, else None."""
        needed = [const_of(p) for p in P]
        if any(c is None for c in needed):
            return None
        for i in range(n_count):
            if all(n_lists[p][i] == needed[p] for p in P):
                return "N[%d]" % i
        if len(set(needed)) == 1:
            return "F('%s')" % needed[0]
        return None

    out = []
    if all(x_values[p] == a_values[p] for p in P):
        out.append("X")
    for i in range(n_count):
        if all(n_lists[p][i] == a_values[p] for p in P):
            out.append("N[%d]" % i)
    c = consistent(lambda p: a_values[p] - x_values[p])
    if c:
        out.append("X+%s" % c)
    c = consistent(lambda p: x_values[p] - a_values[p])
    if c:
        out.append("X-%s" % c)
    c = consistent(lambda p: a_values[p] + x_values[p])
    if c:
        out.append("%s-X" % c)
    c = consistent(lambda p: a_values[p] / x_values[p] if x_values[p] else None)
    if c:
        out.append("%s*X" % c)
    c = consistent(lambda p: x_values[p] / a_values[p] if a_values[p] else None)
    if c:
        out.append("X/%s" % c)
    c = consistent(lambda p: a_values[p] * x_values[p])
    if c:
        out.append("%s/X" % c)
    return out


def derive(group):
    """(entry, None) for a wording that can be made into a family, else (None, reason)."""
    first = group[0]
    var, _ = WA._literals(WA._normalize(first.EQUATION))
    if var is None:
        return None, "the equation is not one letter"
    if not all(plain_answer(p.ANSWER) for p in group):
        return None, "the answer is one of the special cases of an older family"
    norms = [WA._normalize(p.EQUATION) for p in group]
    if any(n.count("=") != 1 for n in norms):
        return None, "not one equation"
    roles, why = literal_roles(norms, [p.NUMBERS for p in group])
    if roles is None:
        return None, why
    left, j = expression(norms[0].split("=")[0], roles, 0)
    right, _ = expression(norms[0].split("=")[1], roles, j)
    left, right = left.replace(var, "X"), right.replace(var, "X")
    n_lists = [[Fraction(n.replace(",", "")) for n in p.NUMBERS] for p in group]
    # the root that is one of the stored answer's numbers
    xs, answers = [], []
    for p, numbers in zip(group, n_lists):
        a = answer_values(p.ANSWER)
        rs = [r for r in AF.roots(left, right, numbers) if r in a]
        if len(rs) != 1:
            return None, "no single root of the equation is a number of the stored answer (%d)" % len(rs)
        xs.append(rs[0])
        answers.append(a)
    if len({len(a) for a in answers}) != 1:
        return None, "the stored answers do not all have the same count of numbers"
    values = []
    for k in range(len(answers[0])):
        found = forms(xs, n_lists, [a[k] for a in answers])
        if not found:
            return None, "no recipe for answer number %d" % (k + 1)
        values.append(found[0])
    used = set(i for t in [left, right] + values for i in map(int, re.findall(r"N\[(\d+)\]", t)))
    if used != set(range(len(n_lists[0]))):
        return None, "a number of the problem has no role (unused: %s)" % sorted(set(range(len(n_lists[0]))) - used)
    # the sanity checks every stored answer passes
    def flags(vals):
        return {"positive": all(v > 0 for v in vals), "whole": all(v.denominator == 1 for v in vals)}
    unknown_flags = flags(xs)
    value_flags = [flags([Fraction(AF.evaluate(values[k], n_lists[p], xs[p])) for p in range(len(group))]) for k in range(len(values))]
    # the wording as a pattern
    template = AF._clean(first.TEMPLATE)
    pattern = re.escape(template)
    for i in range(len(first.NUMBERS)):
        pattern = pattern.replace(re.escape("{%d}" % i), "(" + NUMRE + ")")
    entry = {
        "id": "archive_%s_%d" % (re.sub(r"[^a-z]+", "_", first.CATEGORY.lower()).strip("_"), 0),
        "category": first.CATEGORY,
        "wording": first.TEMPLATE,
        "pattern": "^" + pattern + "$",
        "n": len(first.NUMBERS),
        "var": var,
        "left": left,
        "right": right,
        "equation": display_template(first.EQUATION, roles),
        "unknown_flags": unknown_flags,
        "values": [{"expr": v, "flags": f} for v, f in zip(values, value_flags)],
        "problems": [p.ID for p in group],
    }
    return entry, None


def check(entry, group):
    """Run the family on every problem of its wording: each must return exactly its stored answer."""
    fam = AF.make_family(entry)
    for p in group:
        r = fam(p.PROBLEM)
        want = sorted(answer_values(p.ANSWER))
        if r is None:
            return "the family declines problem %s" % p.ID
        got = sorted(r.values)
        if not (len(got) == len(want) and all(abs(a - b) <= Fraction(1, 200) for a, b in zip(got, want))):
            return "problem %s gives %s, stored %s" % (p.ID, [float(v) for v in got], [float(v) for v in want])
    return None


def main():
    with open(WA.ARCHIVE, encoding="utf-8") as handle:
        archive = json.load(handle)
    proven = {k for k, v in archive["templates"].items() if v["proven"]}
    groups = collections.defaultdict(list)
    for p in WA.load_problems():
        if p.TEMPLATE in proven:
            groups[p.TEMPLATE].append(p)           # includes problems a family from an earlier run already answers: the wording is the same
    entries, skipped = [], []
    counter = collections.Counter()
    for wording in sorted(groups, key=lambda w: groups[w][0].ID):
        group = sorted(groups[wording], key=lambda p: p.ID)
        entry, why = derive(group)
        if entry is not None:
            why = check(entry, group)
        if entry is None or why is not None:
            skipped.append("%s  %s  %s\n    %s" % (group[0].ID, group[0].CATEGORY, why, wording))
            continue
        base = re.sub(r"_0$", "", entry["id"])
        counter[base] += 1
        entry["id"] = "%s_%d" % (base, counter[base])
        entries.append(entry)
    with open(OUT, "w", encoding="utf-8") as handle:
        json.dump({"families": entries}, handle, indent=1, ensure_ascii=False)
    with open(SKIPPED, "w", encoding="utf-8") as handle:
        handle.write("Proven wordings the archive could not turn into a family, and why (written by make_archive_families.py).\n\n" + "\n".join(skipped) + "\n")
    print("families written: %d (problems covered: %d); proven wordings left alone: %d" % (len(entries), sum(len(e["problems"]) for e in entries), len(skipped)))


if __name__ == "__main__":
    main()

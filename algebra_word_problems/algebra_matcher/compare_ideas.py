"""Do the chess-program ideas help the algebra matcher?  A measured comparison.

Run from this folder:   python compare_ideas.py            (writes compare_results.txt too)
                        python compare_ideas.py --selftest (checks the number reader and the scoring)

Nothing in algebra_matcher.py is changed.  This file adds two ideas on top of the matcher's own ranking and
measures each one, and both together, against the plain matcher:

  IDEA A  "staged number fit"   (the chess strategy stages: foundation / progress / completion)
          For each candidate type, check in stages how well the NUMBERS in the problem fit that type:
            stage 1  the kinds of numbers (plain, $, %, degrees, fractions, ratios) and how many there are
            stage 2  the sizes of the numbers against the sizes the type's templates use
          A candidate's stage score is added to the matcher's own log-confidence.

  IDEA B  "archive of confirmed matches"   (the chess archive + List 3 lookups)
          Every problem a user confirms is stored with its type.  A new problem is compared with the stored
          ones; a type that has a similar stored problem gets a boost (an identical wording scores 1.0).

How the test stays honest
  * set A (60 problems) is the set the matcher was tuned on: it is used here to choose the two weights.
  * set B (40 problems) is the never-tuned set: it is only used to report, never to choose anything.
  * the archive test for B stores only set A's problems (what a user could have confirmed earlier).
"""
import collections
import math
import os
import re
import sys

import algebra_matcher as AM

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------------------------------------
# Reading the numbers in a problem, in the order they appear
# ---------------------------------------------------------------------------------------------------------
_WORD_VALUE = {w: float(i) for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
    "seventeen eighteen nineteen twenty".split())}
_WORD_VALUE.update({"thirty": 30.0, "forty": 40.0, "fifty": 50.0, "sixty": 60.0, "seventy": 70.0,
                    "eighty": 80.0, "ninety": 90.0, "hundred": 100.0, "thousand": 1000.0})
_PLAIN_WORDS = sorted(AM.NUMBER_WORDS - AM.KEEP_NUMBER_WORDS, key=len, reverse=True)
_NUMBER_RE = re.compile(
    r"(?P<EXPR>\([^()]*[a-z]\s*[+−-][^()]*\)|\b\d+(?:\.\d+)?[a-z]\b)"
    r"|(?P<MONEY>\$\s?\d[\d,]*(?:\.\d+)?)"
    r"|(?P<PCT>\d[\d,]*(?:\.\d+)?\s?%)"
    r"|(?P<DEG>\d+(?:\.\d+)?\s?°)"
    r"|(?P<FRAC>\b\d+\s?/\s?\d+\b)"
    r"|(?P<RATIO>\d+:\d+(?::\d+)?|\b\d+ to \d+(?: to \d+)?\b)"
    r"|(?P<NUM>\d[\d,]*(?:\.\d+)?)"
    r"|(?P<WORD>\b(?:" + "|".join(_PLAIN_WORDS) + r")\b)", re.I)


def numbers_in(text):
    """[(kind, value)] in reading order.  kind: NUM MONEY PCT DEG FRAC RATIO EXPR; value may be None."""
    out = []
    for m in _NUMBER_RE.finditer(AM.apply_synonyms(text)):
        kind, raw = m.lastgroup, m.group(0)
        value = None
        try:
            if kind in ("MONEY", "PCT", "DEG", "NUM"):
                value = float(re.sub(r"[^\d.]", "", raw))
            elif kind == "FRAC":
                a, b = re.split(r"\s?/\s?", raw)
                value = float(a) / float(b) if float(b) else None
            elif kind == "WORD":
                kind, value = "NUM", _WORD_VALUE.get(raw.lower())
        except ValueError:
            value = None
        out.append((kind, value))
    return out


# ---------------------------------------------------------------------------------------------------------
# IDEA A: staged number fit
# ---------------------------------------------------------------------------------------------------------
class NumberFit:
    SHARE = 0.02          # a number layout counts as "normal" for a type if at least 2% of its problems have it

    def __init__(self, rows):
        shapes = collections.defaultdict(collections.Counter)      # type -> Counter(sorted kinds tuple)
        counts = collections.defaultdict(collections.Counter)      # type -> Counter(len)
        size = {}                                                  # (type, kind, rank) -> [lo, hi]
        total = collections.Counter()
        for r in rows:
            nums = numbers_in(r["text"])
            t = r["type"]
            total[t] += 1
            shapes[t][tuple(sorted(k for k, _ in nums))] += 1
            counts[t][len(nums)] += 1
            seen = collections.Counter()
            for kind, v in nums:
                rank = seen[kind]
                seen[kind] += 1
                if v is not None and v > 0:
                    lo_hi = size.setdefault((t, kind, rank), [v, v])
                    lo_hi[0], lo_hi[1] = min(lo_hi[0], v), max(lo_hi[1], v)
        self.shapes, self.counts, self.size, self.total = shapes, counts, size, total

    def stage1(self, t, nums):
        """1.0: this exact mix of number kinds is normal for the type; 0.4: only the count is; 0: neither."""
        n = max(self.total[t], 1)
        if self.shapes[t][tuple(sorted(k for k, _ in nums))] / n >= self.SHARE:
            return 1.0
        if self.counts[t][len(nums)] / n >= self.SHARE:
            return 0.4
        return 0.0

    def stage2(self, t, nums):
        """Share of the numbers whose size is inside the range the type's templates use (a 2x margin)."""
        seen, scored, ok = collections.Counter(), 0, 0.0
        for kind, v in nums:
            rank = seen[kind]
            seen[kind] += 1
            if v is None or v <= 0:
                continue
            rng = self.size.get((t, kind, rank))
            scored += 1
            if rng is None:
                ok += 0.0
            elif rng[0] / 2 <= v <= rng[1] * 2:
                ok += 1.0
        return ok / scored if scored else 1.0

    def score(self, t, nums):
        """Stage scores combined; stage 2 counts double, like the later chess stages count for more."""
        return (self.stage1(t, nums) + 2 * self.stage2(t, nums)) / 3


# ---------------------------------------------------------------------------------------------------------
# IDEA B: archive of confirmed matches
# ---------------------------------------------------------------------------------------------------------
class Archive:
    def __init__(self):
        self.items = []                      # (feature set, normalised key, type)

    def add(self, text, t):
        self.items.append((frozenset(AM.features(text)), tuple(AM.normalise(text)), t))

    def boost(self, text):
        """type -> best similarity (0..1) to a stored problem of that type; an identical wording gives 1.0."""
        feats, key = frozenset(AM.features(text)), tuple(AM.normalise(text))
        best = {}
        for f, k, t in self.items:
            sim = 1.0 if k == key else (len(feats & f) / len(feats | f) if feats | f else 0.0)
            if sim > best.get(t, 0.0):
                best[t] = sim
        return best


# ---------------------------------------------------------------------------------------------------------
# Ranking with the ideas switched on or off
# ---------------------------------------------------------------------------------------------------------
class Ranker:
    def __init__(self, matcher, fit):
        self.m, self.fit = matcher, fit
        self.types = list(matcher.logp)
        self._base = {}
        self._nums = {}

    def base(self, text):
        """The plain matcher's confidence for every type (cached)."""
        if text not in self._base:
            res, _ = self.m.predict(text, len(self.types))
            self._base[text] = {r["type"]: r["confidence"] for r in res}
        return self._base[text]

    def rank(self, text, w_fit=0.0, w_arch=0.0, archive=None):
        """[(type, probability)] best first.  w_fit / w_arch = 0 gives exactly the plain matcher."""
        base = self.base(text)
        if text not in self._nums:
            self._nums[text] = numbers_in(text)
        nums = self._nums[text]
        boost = archive.boost(text) if (archive is not None and w_arch) else {}
        s = {}
        for t in self.types:
            v = math.log(max(base.get(t, 0.0), 1e-9))
            if w_fit:
                v += w_fit * self.fit.score(t, nums)
            if w_arch:
                v += w_arch * boost.get(t, 0.0)
            s[t] = v
        top = max(s.values())
        z = sum(math.exp(v - top) for v in s.values())
        return sorted(((t, math.exp(v - top) / z) for t, v in s.items()), key=lambda kv: -kv[1])


def label_for(ranker, text, ok):
    """What a user would confirm: the best-ranked right answer among the matcher's top 5, else any right one."""
    for t, _p in ranker.rank(text)[:5]:
        if t in ok:
            return t
    return sorted(ok)[0]


def metrics(ranker, testset, w_fit=0.0, w_arch=0.0, archive_for=None):
    """top-1 / top-3 / top-5 hit counts, and how the confident picks (>= 0.8) did."""
    hits = collections.Counter()
    sure = sure_ok = 0
    for i, (text, ok) in enumerate(testset):
        res = ranker.rank(text, w_fit, w_arch, archive_for(i) if archive_for else None)
        types = [t for t, _ in res]
        for k in (1, 3, 5):
            hits[k] += any(t in ok for t in types[:k])
        if res[0][1] >= AM.Matcher.CONFIDENT:
            sure += 1
            sure_ok += types[0] in ok
    return {"n": len(testset), "top1": hits[1], "top3": hits[3], "top5": hits[5], "sure": sure, "sure_ok": sure_ok}


def line(label, r):
    n = r["n"]
    conf = "%d/%d right" % (r["sure_ok"], r["sure"]) if r["sure"] else "none"
    return "  %-46s top-1 %5.1f%%  top-3 %5.1f%%  top-5 %5.1f%%   confident picks: %s" % (
        label, 100 * r["top1"] / n, 100 * r["top3"] / n, 100 * r["top5"] / n, conf)


# ---------------------------------------------------------------------------------------------------------
def selftest():
    assert numbers_in("Pens cost 50 cents and 3 pencils cost $1.20 and 15% of 2/3 at 90°") == [
        ("NUM", 50.0), ("NUM", 3.0), ("MONEY", 1.2), ("PCT", 15.0), ("FRAC", 2 / 3), ("DEG", 90.0)]
    assert numbers_in("Five less than twice a number is 31.") == [("NUM", 5.0), ("NUM", 31.0)]
    assert numbers_in("(3x + 10)° and 3x") == [("EXPR", None), ("EXPR", None)]
    assert [k for k, _ in numbers_in("ratio 2:3:5, 150 beads")] == ["RATIO", "NUM"]
    rows = [{"type": "a", "text": "A has 10 cats and 20 dogs"}, {"type": "a", "text": "A has 12 cats and 30 dogs"},
            {"type": "b", "text": "Pay $5 for 3 hats"}]
    fit = NumberFit(rows)
    two = numbers_in("Sam has 11 cats and 25 dogs")
    assert fit.stage1("a", two) == 1.0 and fit.stage1("b", two) == 0.4 and fit.stage1("b", numbers_in("7")) == 0.0
    assert fit.stage2("a", two) == 1.0 and fit.stage2("a", numbers_in("7 cats and 900 dogs")) == 0.5
    assert fit.score("a", two) > fit.score("b", two)
    ar = Archive()
    ar.add("Tom is 3 years older than Jo.", "age")
    assert ar.boost("Tom is 3 years older than Jo.") == {"age": 1.0}
    assert 0 < ar.boost("Ann is 5 years older than Bo; find Bo's age")["age"] < 1
    print("selftest ok")


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    selftest()
    if not os.path.exists(AM.DATA):
        AM.build()
    rows = AM.load_rows()
    matcher = AM.Matcher.load()
    ranker = Ranker(matcher, NumberFit(rows))
    A, B = AM.HAND_TEST, AM.FRESH_TEST
    out = []
    p = out.append

    p("Do the chess ideas help the algebra matcher?   (matcher: %d types, trained on %d generated problems)" % (len(ranker.types), len(rows)))
    p("Set A = 60 problems the matcher was tuned on (used only to choose the two weights).  Set B = 40 never-tuned problems (report only).\n")

    # ---- choose the weights on A only
    grid = [0, 0.25, 0.5, 1, 2, 4, 8]
    fit_scores = {w: metrics(ranker, A, w_fit=w) for w in grid}
    best_w = max(grid, key=lambda w: (fit_scores[w]["top1"] + fit_scores[w]["top3"], -w))
    p("Choosing the staged-number-fit weight on set A:")
    for w in grid:
        r = fit_scores[w]
        p("  weight %-4s top-1 %2d/%d  top-3 %2d/%d" % (w, r["top1"], r["n"], r["top3"], r["n"]))
    p("  chosen: %s  (best top-1 + top-3 on A; the smaller weight wins a tie)\n" % best_w)

    labels_A = [label_for(ranker, t, ok) for t, ok in A]

    def archive_loo_A(skip):
        ar = Archive()
        for j, (t, _ok) in enumerate(A):
            if j != skip:
                ar.add(t, labels_A[j])
        return ar

    arch_scores = {w: metrics(ranker, A, w_arch=w, archive_for=archive_loo_A) for w in grid}
    best_b = max(grid, key=lambda w: (arch_scores[w]["top1"] + arch_scores[w]["top3"], -w))
    p("Choosing the archive weight on set A (each problem is tested against an archive of the OTHER 59):")
    for w in grid:
        r = arch_scores[w]
        p("  weight %-4s top-1 %2d/%d  top-3 %2d/%d" % (w, r["top1"], r["n"], r["top3"], r["n"]))
    p("  chosen: %s\n" % best_b)

    archive_A = Archive()
    for (t, _ok), lab in zip(A, labels_A):
        archive_A.add(t, lab)
    arch_fixed = lambda _i: archive_A

    p("RESULT on the never-tuned set B (40 problems); the archive holds the 60 problems of set A:")
    base = metrics(ranker, B)
    fit_only = metrics(ranker, B, w_fit=best_w)
    arch_only = metrics(ranker, B, w_arch=best_b, archive_for=arch_fixed)
    both = metrics(ranker, B, w_fit=best_w, w_arch=best_b, archive_for=arch_fixed)
    p(line("1. plain matcher", base))
    p(line("2. + staged number fit (weight %s)" % best_w, fit_only))
    p(line("3. + archive (weight %s)" % best_b, arch_only))
    p(line("4. + both", both))

    p("\nSame comparison on set A (set A was used to choose the weights, so this is NOT a fair test):")
    p(line("plain matcher", metrics(ranker, A)))
    p(line("+ staged number fit", fit_scores[best_w]))
    p(line("+ archive (the other 59)", arch_scores[best_b]))

    # ---- the archive the other way round, and across all 100 (each against the other 99)
    labels_B = [label_for(ranker, t, ok) for t, ok in B]
    archive_B = Archive()
    for (t, _ok), lab in zip(B, labels_B):
        archive_B.add(t, lab)
    p("\nArchive the other way round (archive = set B's 40, tested on set A's 60):")
    p(line("plain matcher", metrics(ranker, A)))
    p(line("+ archive", metrics(ranker, A, w_arch=best_b, archive_for=lambda _i: archive_B)))

    allp = A + B
    labels_all = labels_A + labels_B

    def archive_loo_all(skip):
        ar = Archive()
        for j, (t, _ok) in enumerate(allp):
            if j != skip:
                ar.add(t, labels_all[j])
        return ar

    p("\nAll 100 problems, each against an archive of the other 99 (similar problems by the same author, so optimistic):")
    p(line("plain matcher", metrics(ranker, allp)))
    p(line("+ archive", metrics(ranker, allp, w_arch=best_b, archive_for=archive_loo_all)))
    p(line("+ staged number fit + archive", metrics(ranker, allp, w_fit=best_w, w_arch=best_b, archive_for=archive_loo_all)))

    # ---- sensitivity: the weights above were chosen on A alone; here is every weight on B, for information only
    p("\nFor information only (NOT used to choose anything): every weight tried on set B, top-1 / top-3 of 40:")
    p("  weight   staged number fit    archive of set A")
    for w in grid:
        f = metrics(ranker, B, w_fit=w)
        a = metrics(ranker, B, w_arch=w, archive_for=arch_fixed)
        p("  %-7s  %2d / %2d              %2d / %2d" % (w, f["top1"], f["top3"], a["top1"], a["top3"]))

    # ---- does the archive mechanism work at all?  An archive that already holds the problem must find it.
    leak = Archive()
    for (t, _ok), lab in zip(B, labels_B):
        leak.add(t, lab)
    r = metrics(ranker, B, w_arch=4, archive_for=lambda _i: leak)
    p("\nMechanism check: archive that already contains each set-B problem (confirmed earlier), weight 4:")
    p(line("repeat wording answered from the archive", r))

    # ---- the four problems the plain matcher misses in set B's top 3
    p("\nWhat happened to the plain matcher's misses in set B (rank of the right type, plain -> with both):")
    for text, ok in B:
        plain = [t for t, _ in ranker.rank(text)]
        new = [t for t, _ in ranker.rank(text, best_w, best_b, archive_A)]
        rp = min(plain.index(t) for t in ok if t in plain) + 1
        rn = min(new.index(t) for t in ok if t in new) + 1
        if rp > 3 or rn != rp:
            p("  %-70s %2d -> %2d" % (text[:70], rp, rn))
    text = "\n".join(out)
    print(text)
    with open(os.path.join(HERE, "compare_results.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()

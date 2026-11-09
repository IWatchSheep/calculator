# -*- coding: utf-8 -*-
"""How well does simple text matching identify an algebra word problem's type?

Leave-one-WORDING-out: when classifying a problem, every problem that has the same wording (the same sentences
once the numbers are masked) is removed from the reference set, so the matcher only sees problems worded
differently from the one it is classifying.  Both the category and the *equation shape* are scored.
"""
import math, re, collections, sys, random

txt = open(r"C:\Users\I_wat\PycharmProjects\calculator\algebra_word_problems.txt", encoding="utf-8").read()
blocks = re.split(r"\n-{20,}\n", txt)
E = []
for b in blocks:
    m = re.search(r"#(\d{4}) \[(.+?)\]\nProblem: (.*?)\nLet: (.*?)\nEquation: (.*?)\nSolve: (.*?)\nAnswer: (.*)", b, re.S)
    if m:
        E.append(dict(id=m[1], cat=m[2], problem=m[3].strip(), let=m[4].strip(), eq=m[5].strip(), ans=m[7].strip()))

NUM = re.compile(r"\$?\d+(?:,\d{3})*(?:\.\d+)?%?")


def mask_numbers(s):
    return NUM.sub("#", s)


def eq_shape(eq):
    s = NUM.sub("#", eq)
    s = re.sub(r"\b[a-zA-Z]\b", "v", s)           # a lone letter is a variable
    return re.sub(r"\s+", " ", s).strip()


# names: capitalised words whose lower-case form is rare in the corpus
low = collections.Counter()
cap = collections.Counter()
for e in E:
    for w in re.findall(r"[A-Za-z']+", e["problem"]):
        (cap if w[0].isupper() else low)[w.lower()] += 1
NAMES = {w for w in cap if low[w] < 3 and cap[w] > 0}


def tokens(s):
    s = mask_numbers(s)
    toks = []
    for w in re.findall(r"#|[A-Za-z']+", s):
        lw = w.lower()
        toks.append("<name>" if lw in NAMES and w[0].isupper() else lw)
    return toks


STOP = set("a an the of to in on at is are was were be been it its and or for with as by that this each how what many much".split())


def feats(s):
    t = [w for w in tokens(s) if w not in STOP]
    f = collections.Counter(t)
    for a, b in zip(t, t[1:]):
        f[a + "_" + b] += 1
    return f


for e in E:
    e["tok"] = tokens(e["problem"])
    e["feat"] = feats(e["problem"])
    e["skel"] = " ".join(e["tok"])
    e["shape"] = eq_shape(e["eq"])
    e["nnum"] = len(NUM.findall(e["problem"]))

df = collections.Counter()
for e in E:
    for k in e["feat"]:
        df[k] += 1
N = len(E)
idf = {k: math.log((N + 1) / (c + 1)) + 1 for k, c in df.items()}
for e in E:
    v = {k: (1 + math.log(c)) * idf[k] for k, c in e["feat"].items()}
    n = math.sqrt(sum(x * x for x in v.values())) or 1
    e["vec"] = {k: x / n for k, x in v.items()}


def cos(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(k, 0) for k, x in a.items())


def classify(e, ref, k=1):
    scored = sorted(((cos(e["vec"], r["vec"]), r) for r in ref), key=lambda x: -x[0])
    return scored[:k]


print("problems:", len(E), " categories:", len({e['cat'] for e in E}),
      " distinct wordings:", len({e['skel'] for e in E}), " distinct equation shapes:", len({e['shape'] for e in E}))

by_skel = collections.defaultdict(list)
for e in E:
    by_skel[e["skel"]].append(e)

# --- A: leave-one-out, same wording allowed (the easy case: a problem worded like one already stored)
okc = oks = 0
for e in E:
    ref = [r for r in E if r is not e]
    (s, r), = classify(e, ref)
    okc += r["cat"] == e["cat"]
    oks += r["shape"] == e["shape"]
print("\nA) same wording may be in the archive (leave one out)")
print("   category right: %.1f%%   equation shape right: %.1f%%" % (100 * okc / N, 100 * oks / N))

# --- B: leave-one-wording-out (the honest case: a new wording of a known type)
okc = oks = okc3 = oks3 = 0
conf = []
tested = 0
for e in E:
    ref = [r for r in E if r["skel"] != e["skel"]]
    top = classify(e, ref, 3)
    (s, r) = top[0]
    tested += 1
    okc += r["cat"] == e["cat"]
    oks += r["shape"] == e["shape"]
    okc3 += any(t[1]["cat"] == e["cat"] for t in top)
    oks3 += any(t[1]["shape"] == e["shape"] for t in top)
    conf.append((s, r["cat"] == e["cat"], r["shape"] == e["shape"]))
print("\nB) the exact wording is NOT in the archive (leave one wording out)")
print("   category right (best match): %.1f%%   in the best 3: %.1f%%" % (100 * okc / tested, 100 * okc3 / tested))
print("   equation shape right (best match): %.1f%%   in the best 3: %.1f%%" % (100 * oks / tested, 100 * oks3 / tested))

# how much does confidence tell us?  (a low score = ask the user, a high score = trust it)
conf.sort(reverse=True)
for frac in (0.25, 0.5, 0.75, 1.0):
    part = conf[: int(len(conf) * frac)]
    print("   most confident %3d%% of the matches: category right %.1f%%, shape right %.1f%%  (score >= %.2f)" % (
        frac * 100, 100 * sum(c for _, c, _ in part) / len(part), 100 * sum(s for _, _, s in part) / len(part), part[-1][0]))

# --- C: robustness - the user types the problem with different numbers and a few words dropped/changed
random.seed(7)
okc = oks = n = 0
for e in E:
    words = e["problem"].split()
    keep = [w for w in words if random.random() > 0.15]            # drop ~15% of the words
    noisy = NUM.sub(lambda m: str(random.randint(2, 99)), " ".join(keep))   # new numbers
    v = {k: (1 + math.log(c)) * idf.get(k, 1) for k, c in feats(noisy).items()}
    nn = math.sqrt(sum(x * x for x in v.values())) or 1
    q = {"vec": {k: x / nn for k, x in v.items()}}
    ref = [r for r in E if r["skel"] != e["skel"]]
    (s, r), = classify(q, ref)
    n += 1
    okc += r["cat"] == e["cat"]
    oks += r["shape"] == e["shape"]
print("\nC) new wording + 15%% of the words dropped + different numbers")
print("   category right: %.1f%%   equation shape right: %.1f%%" % (100 * okc / n, 100 * oks / n))

# --- D: which categories are confused (worst five) under B
bad = collections.Counter()
tot = collections.Counter()
for e in E:
    ref = [r for r in E if r["skel"] != e["skel"]]
    (s, r), = classify(e, ref)
    tot[e["cat"]] += 1
    if r["cat"] != e["cat"]:
        bad[(e["cat"], r["cat"])] += 1
print("\nD) most common wrong category matches under B (true -> matched):")
for (a, b), c in bad.most_common(8):
    print("   %-28s -> %-28s %d of %d" % (a, b, c, tot[a]))
print("\nnumbers per problem: avg %.2f; problems with >=5 numbers: %d" % (sum(e['nnum'] for e in E) / N, sum(e['nnum'] >= 5 for e in E)))

# --- B2: split B into "a new wording of a type the archive already knows" and "a type the archive has never seen"
known = []     # (problem, ref) where the same (category, equation shape) is still in the reference set
unknown = 0
for e in E:
    ref = [r for r in E if r["skel"] != e["skel"]]
    if any(r["cat"] == e["cat"] and r["shape"] == e["shape"] for r in ref):
        known.append((e, ref))
    else:
        unknown += 1
print("\nB2) leave one wording out, split by whether the archive still holds that problem TYPE (category + equation shape)")
print("   type still in the archive (a new wording of a known type): %d problems" % len(known))
print("   type NOT in the archive (never seen): %d problems" % unknown)
okc = oks = okt = 0
conf2 = []
for e, ref in known:
    top = classify(e, ref, 1)
    s, r = top[0]
    okc += r["cat"] == e["cat"]
    oks += r["shape"] == e["shape"]
    okt += r["cat"] == e["cat"] and r["shape"] == e["shape"]
    conf2.append((s, r["cat"] == e["cat"] and r["shape"] == e["shape"]))
n = len(known)
print("   for the known-type group: category right %.1f%%, equation shape right %.1f%%, both right %.1f%%" % (100 * okc / n, 100 * oks / n, 100 * okt / n))
conf2.sort(reverse=True)
for frac in (0.25, 0.5, 0.75, 1.0):
    part = conf2[: int(len(conf2) * frac)]
    print("   most confident %3d%% (score >= %.2f): type right %.1f%%" % (frac * 100, part[-1][0], 100 * sum(c for _, c in part) / len(part)))

"""Write rust_calculator/tests/parity_values.tsv: the REAL Python compute() run on typed inputs.

Run from the project root (after make_operator_keys.py):   python operator_keys/make_value_grid.py

For every Ready operator whose boxes are not all plain numbers (lists, matrices, sets, graphs, functions ...) or
whose answer is not a plain number, this builds inputs the way a person types them in the Advanced Input window
(`1, 2, 3`   `1 2; 3 4`   `x**2 + 3*x`   `A: B, C; B: C`), turns the text into Python values with the program's own
`operator_row_math.advanced_input.parse`, calls the real `compute()`, and records the answer.

Line format:  key <TAB> JSON list of the typed texts <TAB> ERR | JSON answer
Answers use plain JSON plus tags for Python types JSON lacks (see rust_calculator/src/valuejson.rs):
{"t": [..]} tuple, {"s": [..]} set, {"d": [[k, v], ..]} dict, {"c": [re, im]} complex, {"f": "inf"} special float.
The Rust test (tests/parity_values.rs) must give the same answer, or an error on exactly the same inputs.
"""
import importlib.util
import json
import math
import os
import random
import signal
import sys
import threading

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from operator_row_math import advanced_input as AI  # noqa: E402

OPS = os.path.join(ROOT, "operators_one_operator_per_file")
OUT = os.path.join(ROOT, "rust_calculator", "tests", "parity_values.tsv")

NUMBERS = ["0", "1", "2", "3", "4", "0.5", "-1", "10", "2.5", "-2", "5", "7", "0.1", "100"]
SMALL = ["1", "2", "3", "0", "-1", "0.5", "4", "2.5", "10"]
LISTS = {
    1: ["5", "0", "-2", "2.5"],
    2: ["1, 2", "3 4", "0, 1", "2, -1", "1.5 2.5", "0 0"],
    3: ["1, 2, 3", "4 5 6", "1 0 0", "0, 1, 0", "2, -1, 3", "1.5 2.5 3.5", "3, 4, 12", "0 0 0"],
    4: ["1 2 3 4", "2, 4, 6, 8", "4 3 2 1", "1, 3, 3, 1"],
    5: ["1 2 3 4 5", "2, 3, 5, 7, 11", "5 4 3 2 1", "1, 1, 2, 3, 5"],
}
MATS = {
    (1, 1): ["5", "2", "0"],
    (2, 2): ["1 2; 3 4", "2 0; 0 3", "4 1; 2 3", "1 0; 0 1", "0 1; 1 0", "2 1; 1 2", "1 2; 2 4"],
    (3, 3): ["1 2 3; 4 5 6; 7 8 10", "2 1 0; 1 3 1; 0 1 4", "4 1 2; 1 3 0; 2 0 5", "1 0 0; 0 1 0; 0 0 1", "2 0 0; 0 3 0; 0 0 4"],
    (2, 3): ["1 2 3; 4 5 6", "1 0 2; 0 1 3"],
    (3, 2): ["1 2; 3 4; 5 6", "1 0; 0 1; 1 1"],
    (3, 1): ["1; 2; 3"],
}
SETS = ["1, 2, 3", "2, 3, 4", "1, 2", "3", "0, 1, 2, 3, 4", "a, b, c", "b, c", "0, 1, 2, 3, 4, 5", "1, 2, 3, 4, 5, 6", "2, 4", "1, 3, 5"]
SETFAMILIES = ["{1,2}, {2,3}, {1,2,3}, {}", "{1}, {2}, {1,2}, {}", "{1,2,3}, {1}, {2}, {1,2}, {}", "{1,2}, {3}, {1,2,3}, {}", "{1,2}, {2,3}"]
ITEMS = ["A", "B", "C", "1", "2", "0", "3", "a", "b"]
GRAPHS = ["A: B, C; B: C; C: A", "0: 1, 2; 1: 2; 2: 0; 3:", "A: B; B: A, C; C: B", "A: B; B: C; C: D; D: A",
          "A: B, C, D; B: A, C; C: A, B, D; D: A, C", "0: 1; 1: 2; 2:"]
WGRAPHS = ["A: B=4, C=1; B: C=2; C:", "A: B=1, C=5; B: C=2, D=6; C: D=1; D:", "A: B=3; B: C=4; C: A=5", "A: B=2, C=3; B: A=2, C=1; C: A=3, B=1"]
PAIRS = ["(0,1), (1,2), (2,0)", "(0,1), (1,2)", "(0,1), (0,2), (1,2), (2,3)", "(0,1), (1,2), (2,3), (3,0)"]
FUNCS = ["x**2", "x**3 - 2*x - 5", "sin(x)", "exp(x)", "2*x + 1", "x**2 - 4", "cos(x)", "1/(x**2 + 1)", "x**2 + 3*x",
         "x**3", "x**2 - 2", "log(x)", "abs(x)", "sqrt(x)"]
FUNCS_G = ["x**2", "x**2 - 1", "2*x", "x + 1", "sin(x)", "x**3 - x"]
MULTI = ["x**2 + y**2", "x*y", "x**2*y + y", "sin(x)*y", "x**2 + y**2 + z**2", "x*y*z", "[2*x, 2*y]", "[y, -x]",
         "[x*y, x + y]", "[x**2, y**2]", "x + y", "(x + y) % 6", "(x*y) % 7", "[x, y]", "x - y", "x*y - 1", "[y, x]"]
PREDICATES = ["x > 2", "x % 2 == 0", "x < 0", "x >= 1", "x != 3", "x*x < 10"]
TEXTS = ["(x+1)(x-1)", "x^2 - 1", "x^2 + 5x + 6", "2x + 4", "(x+2)(x+3)", "x^2 - 5x + 6", "(x-1)^2", "3x^2 - 12", "x^3 - x", "x + x"]
# number-only operators whose answer is a list / matrix / complex pair (the number grid cannot hold it)
STRUCT_RESULT = {"prime_factorization", "identity_matrix", "characteristic_equation"}


def pick(rng, kind, ctx):
    """One typed text for an input of this kind; ctx remembers a list length / matrix size to keep inputs compatible."""
    if kind == "number":
        return rng.choice(NUMBERS if rng.random() < 0.5 else SMALL)
    if kind == "list":
        n = ctx.get("n") if rng.random() < 0.75 else None
        n = n or rng.choice([2, 3, 3, 3, 4, 5, 1])
        t = rng.choice(LISTS[min(n, 5)])
        ctx.setdefault("n", len(AI.parse("list", t)))
        return t
    if kind == "matrix":
        n = ctx.get("n")
        if n and rng.random() < 0.75:
            shapes = [s for s in MATS if s[0] == n and s[1] == n] or list(MATS)
        else:
            shapes = [s for s in MATS if s[0] == s[1]] * 3 + list(MATS)
        shape = rng.choice(shapes)
        t = rng.choice(MATS[shape])
        ctx.setdefault("n", shape[0])
        return t
    if kind == "set":
        return rng.choice(SETS)
    if kind == "setfamily":
        return rng.choice(SETFAMILIES)
    if kind == "item":
        return rng.choice(ITEMS)
    if kind == "graph":
        return rng.choice(GRAPHS)
    if kind == "wgraph":
        return rng.choice(WGRAPHS)
    if kind == "pairs":
        return rng.choice(PAIRS)
    if kind == "function":
        return rng.choice(FUNCS)
    if kind == "multi":
        return rng.choice(MULTI)
    if kind == "predicate":
        return rng.choice(PREDICATES)
    if kind == "text":
        return rng.choice(TEXTS)
    raise ValueError(kind)


# Inputs that random picking would hardly ever make fit together (a group, its operation and a map between groups ...).
# They are tried first for these operators so the "it works" path is checked, not only the "error" path.
SPECIAL = {
    "homomorphism": [["x % 3", "0, 1, 2, 3, 4, 5", "(x + y) % 6", "(x + y) % 3"], ["x", "0, 1, 2", "(x + y) % 3", "(x + y) % 3"],
                     ["2*x", "0, 1, 2", "(x + y) % 3", "(x + y) % 3"], ["x*x", "0, 1, 2", "(x + y) % 3", "(x + y) % 3"]],
    "image": [["x % 3", "0, 1, 2, 3, 4, 5"], ["x*x", "1, 2, 3"], ["2*x + 1", "0, 1, 2"]],
    "isomorphism": [["x", "0, 1, 2", "0, 1, 2", "(x + y) % 3", "(x + y) % 3"], ["(2*x) % 3", "0, 1, 2", "0, 1, 2", "(x + y) % 3", "(x + y) % 3"],
                    ["x % 3", "0, 1, 2, 3, 4, 5", "0, 1, 2", "(x + y) % 6", "(x + y) % 3"], ["x", "0, 1", "0, 1", "(x + y) % 2", "(x + y) % 2"]],
    "kernel": [["x % 3", "0, 1, 2, 3, 4, 5", "0"], ["x % 2", "0, 1, 2, 3", "0"], ["x*x", "0, 1, 2", "1"]],
    "order_of_element": [["2", "(x + y) % 6", "0"], ["1", "(x + y) % 5", "0"], ["3", "(x*y) % 7", "1"], ["0", "(x + y) % 4", "0"]],
    "curl": [["[y, -x, 0]", "1, 2, 3"], ["[y*z, x*z, x*y]", "1, 2, 3"], ["[x*y, y*z, z*x]", "1 2 3"], ["[x, y, z]", "0.5, 1, 2"]],
    "line_integral": [["[-y, x]", "[cos(t), sin(t)]", "0", "6.283185307179586"], ["[y, x]", "[t, t**2]", "0", "1"], ["[x, y]", "[t, t]", "0", "2"]],
    "tangent_vector": [["[cos(t), sin(t)]", "1"], ["[t**2, t**3]", "2"], ["[t, 2*t, 3]", "0.5"]],
    "cyclic_group": [["1", "(x + y) % 5", "0"], ["2", "(x + y) % 6", "0"], ["3", "(x*y) % 7", "1"], ["4", "(x + y) % 8", "0"]],
    "divergence": [["[x*y, y*z, z*x]", "1, 2, 3"], ["[x, y]", "1, 2"], ["[x**2, y**2, z**2]", "1, 2, 3"], ["[sin(x), cos(y)]", "0.5, 1"]],
    "lie_bracket": [["[y, x]", "[x, -y]", "1, 2"], ["[x*y, y]", "[x, x*y]", "1, 2"], ["[x, y]", "[y, x]", "1 2"]],
    "path": [["A: B, C; B: D; C: D; D:", "A", "D"], ["0: 1, 2; 1: 3; 2: 3; 3:", "0", "3"], ["A: B; B: C", "A", "C"], ["A: B; B: A, C; C: B", "C", "A"]],
    "bisection_method": [["x**2 - 4", "0", "5"], ["x**3 - 2*x - 5", "2", "3"], ["cos(x)", "0", "3"], ["x - 1", "-2", "4"]],
    "newton_s_method": [["x**2 - 2", "2*x", "1"], ["x**3 - 2*x - 5", "3*x**2 - 2", "2"], ["cos(x)", "-sin(x)", "1"]],
    "spline": [["0, 1, 2, 3", "0, 1, 8, 27", "1.5"], ["0 1 2", "1 3 2", "0.5"], ["0, 2, 4, 6", "1, 3, 2, 5", "3"], ["0 1 2 3 4", "0 1 4 9 16", "2.5"]],
    "axiom_of_choice": [["{1,2}, {3}, {4,5}"], ["{a,b}, {c}"], ["{10,2}, {7}"]],
    "open_ball": [["(x[0]-y[0])**2 + (x[1]-y[1])**2", "0, 0", "1, 1", "3"], ["abs(x[0]-y[0])", "0, 0", "1, 1", "0.5"]],
}


class Skip(Exception):
    pass


class Timeout(Skip):
    pass


def tojson(v, depth=0):
    if depth > 12:
        raise Skip()
    if isinstance(v, bool):
        return v
    if isinstance(v, int):
        if abs(v) > 10 ** 15:
            raise Skip()
        return v
    if isinstance(v, float):
        if math.isnan(v):
            return {"f": "nan"}
        if math.isinf(v):
            return {"f": "inf" if v > 0 else "-inf"}
        return v
    if isinstance(v, complex):
        if not (math.isfinite(v.real) and math.isfinite(v.imag)):
            raise Skip()
        return {"c": [v.real, v.imag]}
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return [tojson(x, depth + 1) for x in v]
    if isinstance(v, tuple):
        return {"t": [tojson(x, depth + 1) for x in v]}
    if isinstance(v, (set, frozenset)):
        return {"s": sorted((tojson(x, depth + 1) for x in v), key=lambda j: json.dumps(j, sort_keys=True))}
    if isinstance(v, dict):
        return {"d": [[tojson(k, depth + 1), tojson(x, depth + 1)] for k, x in v.items()]}
    if hasattr(v, "numerator") and hasattr(v, "denominator"):
        return float(v)
    raise Skip()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def call_with_timeout(fn, args, seconds=3.0):
    """Run fn(*args) in a thread; give up after a few seconds (a runaway loop is recorded as 'skip')."""
    box = {}

    def run():
        try:
            box["v"] = fn(*args)
        except BaseException as e:      # noqa: B902 - every Python error is just "ERR"
            box["e"] = e

    t = threading.Thread(target=run, daemon=True)
    t.start()
    t.join(seconds)
    if t.is_alive():
        raise Timeout()
    if "e" in box:
        raise box["e"]
    return box["v"]


def guard(fn):
    """Wrap a typed function so a runaway integer (x**3 applied again and again) is dropped, not computed forever."""
    if not callable(fn):
        return fn

    def big(v):
        if isinstance(v, int) and not isinstance(v, bool) and abs(v) > 10 ** 15:
            raise Skip()
        if isinstance(v, (list, tuple)):
            for x in v:
                big(x)

    def g(*a):
        r = fn(*a)
        big(r)
        return r

    g.text = getattr(fn, "text", "")
    return g


def wanted(r):
    if r["status"] != "Ready":
        return False
    kinds = r["input_kinds"]
    if kinds and set(kinds) == {"number"} and r["key"].rsplit("/", 1)[1] not in STRUCT_RESULT:
        return False                                  # plain number operators are covered by parity_differential.tsv
    return True


def run_one(r, fh):
    """Run one operator on a grid of typed inputs and append the lines to fh."""
    import zlib
    rng = random.Random(20261109 + zlib.crc32(r["key"].encode()))
    kinds = r["input_kinds"]
    group, sub, leaf = r["key"].split("/")
    mod = load(os.path.join(OPS, group, sub, leaf, leaf + ".py"), "val_" + leaf)
    cap = 14 if set(kinds) & {"function", "multi", "predicate"} else 40
    seen, wrote, hung = set(), 0, 0
    special = list(SPECIAL.get(leaf, []))
    for _attempt in range(300 + len(special)):
        if wrote >= cap + len(special):
            break
        ctx = {}
        texts = special.pop(0) if special else [pick(rng, k, ctx) for k in kinds]
        tkey = tuple(texts)
        if tkey in seen:
            if len(seen) > 120:
                break
            continue
        seen.add(tkey)
        try:
            args = [guard(AI.parse(k, t)) for k, t in zip(kinds, texts)]
        except ValueError:
            continue                                  # the program itself would refuse this input
        try:
            out = tojson(call_with_timeout(mod.compute, args))
        except Timeout:
            hung += 1
            if hung >= 2:
                break
            continue
        except Skip:
            continue
        except BaseException:                         # noqa: B902
            out = "ERR"
        fh.write("%s\t%s\t%s\n" % (r["key"], json.dumps(texts, ensure_ascii=False),
                                   out if out == "ERR" else json.dumps(out, ensure_ascii=False)))
        fh.flush()
        wrote += 1
    return wrote


def main():
    import subprocess
    cat = json.load(open(os.path.join(ROOT, "operator_keys", "operator_keys.json"), encoding="utf-8"))["operators"]
    sys.setrecursionlimit(3000)
    ops = [r for r in cat if wanted(r)]
    if "--op" in sys.argv:                            # child process: one operator, appended to the file
        key = sys.argv[sys.argv.index("--op") + 1]
        with open(OUT, "a", encoding="utf-8", newline="\n") as fh:
            run_one(next(r for r in ops if r["key"] == key), fh)
        return
    done = set()
    if "--resume" in sys.argv and os.path.exists(OUT):
        rows = [r for r in open(OUT, encoding="utf-8").read().split("\n") if r]
        last = rows[-1].split("\t")[0] if len(rows) > 1 else None
        rows = [r for r in rows if r.split("\t")[0] != last]       # the last operator may have been cut off: redo it
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(rows) + "\n")
        done = {r.split("\t")[0] for r in rows if not r.startswith("#")}
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("# key<TAB>typed inputs (JSON)<TAB>ERR|answer (JSON)   (real Python compute(); generated by operator_keys/make_value_grid.py)\n")
    only = [x for x in sys.argv[1:] if not x.startswith("--")]
    for r in ops:
        if r["key"] in done or (only and only[0] not in r["key"]):
            continue
        print(r["key"], file=sys.stderr, flush=True)
        try:
            # a separate process per operator: a runaway loop is killed instead of slowing everything else down
            subprocess.run([sys.executable, "-I", os.path.abspath(__file__), "--op", r["key"]], timeout=240)
        except subprocess.TimeoutExpired:
            print("  gave up (runs too long)", file=sys.stderr, flush=True)
    total = sum(1 for line in open(OUT, encoding="utf-8") if not line.startswith("#"))
    print("value cases written:", total)


if __name__ == "__main__":
    main()

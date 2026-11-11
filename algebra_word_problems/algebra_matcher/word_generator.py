"""Generated lines for the word archive: arithmetic trees over a sentence's numbers.  No stored equation is read.

A generated line is a tree with + - * / over
    the numbers of the sentence, named by their place: N0, N1, ...   (every one at least once; a number may be written twice)
    the fixed numbers 1, 2 and 100
    one cue constant, only when its cue word is in the sentence: interior 180, exterior 360
Its size is the count of its leaves.  "((N0 - N2) * N1) / (N0 + N1)" has size 5.

A wording is swept one size at a time, smallest first.  A tree is played on every stored problem of the wording at once and
compared with the stored answers.  Two trees that give the same number on every stored problem are one line, and only the
first is kept.  When the answer asks for several numbers, the line is one tree for each of them, and all must hit.

The search is exact.  Numbers are kept as residues modulo a large prime, so equal fractions are equal residues, and a tree
that hits is checked again with exact fractions before it is called a win.

    sweep(numbers, targets, words, max_size)   ->   {"line": [tree, ...] or None, "size": n, "fixed": [...], "open": [...]}
    evaluate(tree_text, numbers)               ->   Fraction

Standard library only.
"""
import ast
import itertools
import re
from fractions import Fraction

VERSION = 1                       # a change to the trees that are generated must change this: it voids every loss record
FIXED = (1, 2, 100)
CUE_FIXED = {"interior": 180, "exterior": 360}
MAX_SIZE = 6
_P = (1 << 61) - 1


def fixed_numbers(words):
    """The fixed numbers a sentence with these words may use."""
    return list(FIXED) + [value for cue, value in sorted(CUE_FIXED.items()) if cue in words]


def _residue(value):
    value = Fraction(value)
    return value.numerator % _P * pow(value.denominator % _P, -1, _P) % _P


def _inverse(vector):
    if 0 in vector:
        return None
    return tuple(pow(v, -1, _P) for v in vector)


def _splits(leaves):
    """Every way to cut a sorted tuple of leaves into two non-empty parts, each unordered pair once."""
    n, seen = len(leaves), set()
    for mask in range(1, (1 << n) - 1):
        a = tuple(leaves[i] for i in range(n) if mask >> i & 1)
        b = tuple(leaves[i] for i in range(n) if not mask >> i & 1)
        if (len(a), a) > (len(b), b):
            a, b = b, a
        if (a, b) not in seen:
            seen.add((a, b))
            yield a, b


class _Wording:
    """The trees of one wording: every value vector a multiset of leaves can make, with one tree for each."""

    def __init__(self, number_rows, fixed):
        self.k = len(number_rows[0])
        self.leaf = {}
        for i in range(self.k):
            self.leaf["N%d" % i] = tuple(_residue(Fraction(row[i])) for row in number_rows)
        for value in fixed:
            self.leaf[str(value)] = tuple(_residue(value) for _row in number_rows)
        self.pool = sorted(self.leaf)
        self.made = {}                                    # leaves -> {vector: tree}
        self.inverse = {}                                 # leaves -> {vector: inverse vector or None}

    def reach(self, leaves):
        if leaves in self.made:
            return self.made[leaves]
        out = {}
        if len(leaves) == 1:
            out[self.leaf[leaves[0]]] = leaves[0]
        else:
            for a, b in _splits(leaves):
                left, right = self.reach(a), self.reach(b)
                inv_left, inv_right = self.inverses(a), self.inverses(b)
                for va in left:
                    ia = inv_left[va]
                    for vb in right:
                        ib = inv_right[vb]
                        out.setdefault(tuple((x + y) % _P for x, y in zip(va, vb)), ("+", a, va, b, vb))
                        out.setdefault(tuple(x * y % _P for x, y in zip(va, vb)), ("*", a, va, b, vb))
                        if va == vb:
                            continue                      # x - x and x / x only hide a number: not a role for it
                        out.setdefault(tuple((x - y) % _P for x, y in zip(va, vb)), ("-", a, va, b, vb))
                        out.setdefault(tuple((y - x) % _P for x, y in zip(va, vb)), ("-", b, vb, a, va))
                        if ib is not None:
                            out.setdefault(tuple(x * y % _P for x, y in zip(va, ib)), ("/", a, va, b, vb))
                        if ia is not None:
                            out.setdefault(tuple(x * y % _P for x, y in zip(vb, ia)), ("/", b, vb, a, va))
        self.made[leaves] = out
        return out

    def inverses(self, leaves):
        if leaves not in self.inverse:
            self.inverse[leaves] = {v: _inverse(v) for v in self.reach(leaves)}
        return self.inverse[leaves]

    def text(self, leaves, vector):
        node = self.reach(leaves)[vector]
        if isinstance(node, str):
            return node
        op, a, va, b, vb = node
        return "(%s %s %s)" % (self.text(a, va), op, self.text(b, vb))

    def multisets(self, size, may_skip_one=False):
        """Sorted leaf tuples of this size that hold every number of the sentence at least once.  With may_skip_one, also
        those that leave exactly one number out (for an answer that asks for several numbers: see sweep)."""
        numbers = ["N%d" % i for i in range(self.k)]
        bases = [numbers]
        if may_skip_one and self.k >= 2:
            bases += [numbers[:i] + numbers[i + 1:] for i in range(self.k)]
        seen = set()
        for base in bases:
            if size < len(base):
                continue
            pool = self.pool if base is numbers else [leaf for leaf in self.pool if not leaf.startswith("N") or leaf in base]
            for extra in itertools.combinations_with_replacement(pool, size - len(base)):
                leaves = tuple(sorted(base + list(extra)))
                if leaves not in seen:
                    seen.add(leaves)
                    yield leaves

    def hits(self, size, target, may_skip_one=False):
        """Every tree of this size whose value on every stored problem is the target, as text."""
        found = set()
        inv_target = _inverse(target)
        for leaves in self.multisets(size, may_skip_one):
            if size == 1:
                if self.leaf[leaves[0]] == target:
                    found.add(leaves[0])
                continue
            for a, b in _splits(leaves):
                if len(self.reach(a)) > len(self.reach(b)):
                    a, b = b, a
                other = self.reach(b)
                for va, ia in self.inverses(a).items():
                    probes = [
                        (tuple((t - x) % _P for t, x in zip(target, va)), "+", True),          # a + b = T
                        (tuple((x - t) % _P for t, x in zip(target, va)), "-", True),          # a - b = T
                        (tuple((t + x) % _P for t, x in zip(target, va)), "-", False),         # b - a = T
                        (tuple(t * x % _P for t, x in zip(target, va)), "/", False),           # b / a = T
                    ]
                    if ia is not None:
                        probes.append((tuple(t * x % _P for t, x in zip(target, ia)), "*", True))      # a * b = T
                    if inv_target is not None:
                        probes.append((tuple(x * t % _P for x, t in zip(va, inv_target)), "/", True))  # a / b = T
                    for vb, op, a_first in probes:
                        if vb in other and not (vb == va and op in "-/"):
                            if op == "/" and (0 in (vb if a_first else va)):
                                continue
                            ta, tb = self.text(a, va), self.text(b, vb)
                            found.add("(%s %s %s)" % ((ta, op, tb) if a_first else (tb, op, ta)))
        return found


def evaluate(tree, numbers):
    """The exact value of a tree for these numbers.  Raises ZeroDivisionError or ValueError."""
    def go(node):
        if isinstance(node, ast.Expression):
            return go(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return Fraction(node.value)
        if isinstance(node, ast.Name) and re.match(r"N\d+$", node.id):
            return Fraction(numbers[int(node.id[1:])])
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            a, b = go(node.left), go(node.right)
            if isinstance(node.op, ast.Add):
                return a + b
            if isinstance(node.op, ast.Sub):
                return a - b
            if isinstance(node.op, ast.Mult):
                return a * b
            return a / b
        raise ValueError("not a generated tree: %r" % tree)

    return go(ast.parse(tree, mode="eval"))


def size_of(tree):
    return len(re.findall(r"N\d+|\d+", tree))


def _has_roles(tree, row):
    """Every number written in the tree changes its value: "((1 + (N0 + N1)) - N1)" has no role for N1."""
    try:
        base = evaluate(tree, row)
        for name in set(re.findall(r"N\d+", tree)):
            i = int(name[1:])
            moved = [list(row), list(row)]
            moved[0][i] = Fraction(row[i]) + 1
            moved[1][i] = Fraction(row[i]) * 3 + 2
            same = 0
            for other in moved:
                try:
                    same += evaluate(tree, other) == base
                except ZeroDivisionError:
                    pass
            if same == 2:
                return False
    except ZeroDivisionError:
        return False
    return True


def _wins(tree, number_rows, wanted):
    try:
        if not all(evaluate(tree, row) == Fraction(want) for row, want in zip(number_rows, wanted)):
            return False
    except ZeroDivisionError:
        return False
    return _has_roles(tree, number_rows[0])


def sweep(number_rows, targets, words, max_size=MAX_SIZE):
    """Sweep one wording.

    number_rows   the numbers of every stored problem of the wording, in sentence order
    targets       for each asked number of the answer, its value in every stored problem
    words         the lower-case words of the sentence (for the cue constants)

    Every number of the sentence must have a role.  When one number is asked, its tree holds every number.  When several
    are asked, one tree may leave one number out ("the first is N0 - N2"), and the trees together must hold every number.

    Returns the smallest winning tree for each asked number (None where no tree up to the size reached hits), the last
    size that was finished, the fixed numbers used, and the asked numbers still open.  "line" is None unless every asked
    number has a tree and every number of the sentence has a role."""
    fixed = fixed_numbers(words)
    wording = _Wording(number_rows, fixed)
    k = wording.k
    several = len(targets) > 1
    line = [None] * len(targets)
    first = max(1, k - 1 if several else k)
    size = first - 1
    for size in range(first, max_size + 1):
        for j, wanted in enumerate(targets):
            if line[j] is not None:
                continue
            vector = tuple(_residue(Fraction(w)) for w in wanted)
            good = [t for t in wording.hits(size, vector, several) if _wins(t, number_rows, wanted)]
            if good:
                line[j] = min(good, key=lambda t: (len(t), t))
        if all(t is not None for t in line):
            break
    whole = all(t is not None for t in line)
    used = set(re.findall(r"N\d+", " ".join(t for t in line if t)))
    roles = whole and len(used) == k
    return {"line": line if roles else None, "partial": line, "size": size, "fixed": fixed,
            "open": [j for j, t in enumerate(line) if t is None], "number_without_role": whole and not roles}

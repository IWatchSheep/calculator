"""Typed math -> an operator tree for a row (the "Mathematical Templates" panel).

The user types some math, for example

    (□ + 3) × 2            empty box, plus 3, all times 2
    sqrt(16) + abs(-3)     operators written by name
    Time dilation(1, □)    any operator in the library, with its inputs in the brackets
    sin(pi / 2)            pi and e are constants

and gets the same kind of tree the Operators pop-up builds, so it can be put into a row.

What can be typed
  numbers          3   2.5   .5   1.5e-3
  empty box        □   ?   _   or a bare letter such as  x  (each one is its own box)
  symbols          +  −  ×  ÷  ^  %   and  *  /  -   (^ binds tightest, then × ÷ %, then + −)
  brackets         ( ... ) group; name( a, b ) calls an operator
  operator names   by name ("Square root", square_root), by short name (sqrt, sin, ln, abs, ...)
                   or by folder name.  Spaces, capitals, apostrophes and underscores don't matter.

Nothing here uses eval().  Errors are ValueError with a message a person can read.
"""
import json
import os
import re

import operator_row_math as rows
from operator_row_math import row_tree

SYMBOL_OPS = {
    "+": "math/arithmetic/addition", "-": "math/arithmetic/subtraction", "−": "math/arithmetic/subtraction",
    "*": "math/arithmetic/multiplication", "×": "math/arithmetic/multiplication",
    "·": "math/arithmetic/multiplication", "/": "math/arithmetic/division", "÷": "math/arithmetic/division",
    "%": "math/arithmetic/modulo", "^": "math/algebra/power",
}
NEGATE = "math/arithmetic/negate"

# short names people expect  ->  the operator's folder name
ALIASES = {
    "sin": "sine", "cos": "cosine", "tan": "tangent", "csc": "cosecant", "sec": "secant", "cot": "cotangent",
    "asin": "inverse_sine", "acos": "inverse_cosine", "atan": "inverse_tangent",
    "atan2": "two_argument_arctangent", "sinh": "hyperbolic_sine", "cosh": "hyperbolic_cosine",
    "tanh": "hyperbolic_tangent", "asinh": "inverse_hyperbolic_sine", "acosh": "inverse_hyperbolic_cosine",
    "atanh": "inverse_hyperbolic_tangent", "sqrt": "square_root", "cbrt": "cube_root", "abs": "absolute_value",
    "ln": "natural_log", "log": "log_base_10", "log10": "log_base_10", "exp": "exponential",
    "floor": "round_down", "ceil": "round_up", "round": "round_nearest", "min": "minimum", "max": "maximum",
    "det": "determinant", "fact": "factorial", "e": "euler_s_number", "recip": "reciprocal",
    "deg": "degrees_to_radians", "rad": "radians_to_degrees",
    "gcd": "greatest_common_divisor", "lcm": "least_common_multiple", "mod": "modulo",
}

_TOKEN = re.compile(r"""\s*(?:
    (?P<num>\d+(?:\.\d*)?(?:[eE][+-]?\d+)?|\.\d+)
  | (?P<box>[□?]|_(?![\w]))
  | (?P<word>[^\W\d][\w'’]*)
  | (?P<sym>[-+−*×·/÷^%(),])
)""", re.VERBOSE)

_INDEX = None


def _norm(text):
    return re.sub(r"[^a-z0-9]", "", text.lower().replace("’", "'"))


def _index():
    """normalised name -> operator key, built once (math operators win when two share a name)."""
    global _INDEX
    if _INDEX is None:
        idx = {}
        for key in sorted(rows.keys(), key=lambda k: (not k.startswith("math/"), k)):
            mod = rows.get(key)
            for name in {key.split("/")[-1], mod.NAME, mod.NAME.split(" (")[0]}:
                idx.setdefault(_norm(name), key)
        for alias, ident in ALIASES.items():
            idx[_norm(alias)] = idx[_norm(ident)]
        _INDEX = idx
    return _INDEX


def find_operator(name):
    """Operator key for a typed name, or None."""
    return _index().get(_norm(name))


def _box_count(key):
    return sum(1 for kind, _ in rows.get(key).LEFT if kind == "box")


def _tokens(text):
    out, pos = [], 0
    text = text.strip()
    while pos < len(text):
        m = _TOKEN.match(text, pos)
        if not m or m.end() == pos:
            bad = text[pos:].strip()[:1] or text[pos:pos + 1]
            raise ValueError("I don't understand %r in the math." % bad)
        pos = m.end()
        kind = m.lastgroup
        out.append((kind, m.group(kind)))
    return out


class _Parser:
    def __init__(self, text):
        self.toks = _tokens(text)
        self.i = 0

    # -- token helpers
    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else (None, None)

    def take(self):
        tok = self.peek()
        self.i += 1
        return tok

    def accept(self, *syms):
        kind, val = self.peek()
        if kind == "sym" and val in syms:
            self.i += 1
            return val
        return None

    # -- values: ("num", "5") | ("box", "") | an operator node
    @staticmethod
    def slot(value):
        if isinstance(value, tuple):
            return value[1]
        return value

    def make(self, key, *args):
        node = row_tree.new_node(key)
        if len(node["slots"]) != len(args):
            raise ValueError("%s needs %d input(s) but was given %d." % (node["mod"].NAME, len(node["slots"]), len(args)))
        node["slots"] = [self.slot(a) for a in args]
        return node

    def parse(self):
        if not self.toks:
            raise ValueError("Type some math first.")
        value = self.expr()
        if self.peek()[0] is not None:
            kind, val = self.peek()
            if kind in ("num", "word", "box") or val == "(":
                raise ValueError("Put an operator between %r and what comes before it (for example %s × %s)."
                                 % (val, "2", val))
            raise ValueError("Unexpected %r." % val)
        if isinstance(value, tuple):
            raise ValueError("A template needs at least one operator, for example (□ + 3) × 2.")
        return value

    def expr(self):
        left = self.term()
        while True:
            op = self.accept("+", "-", "−")
            if not op:
                return left
            left = self.make(SYMBOL_OPS[op], left, self.term())

    def term(self):
        left = self.unary()
        while True:
            op = self.accept("*", "×", "·", "/", "÷", "%")
            if not op:
                return left
            left = self.make(SYMBOL_OPS[op], left, self.unary())

    def unary(self):
        kind, val = self.peek()
        if kind == "sym" and val in "-−":
            self.i += 1
            nxt_kind, _ = self.peek()
            after = self.toks[self.i + 1] if self.i + 1 < len(self.toks) else (None, None)
            if nxt_kind == "num" and after != ("sym", "^"):         # -5 is the number minus five
                return ("num", "-" + self.take()[1])
            return self.make(NEGATE, self.unary())
        if kind == "sym" and val == "+":
            self.i += 1
            return self.unary()
        return self.power()

    def power(self):
        base = self.atom()
        if self.accept("^"):
            return self.make(SYMBOL_OPS["^"], base, self.unary())     # right-associative: 2^3^2 = 2^(3^2)
        return base

    def atom(self):
        kind, val = self.peek()
        if kind == "num":
            self.i += 1
            return ("num", val)
        if kind == "box":
            self.i += 1
            return ("box", "")
        if kind == "sym" and val == "(":
            self.i += 1
            inner = self.expr()
            if not self.accept(")"):
                raise ValueError("A bracket ( is never closed.")
            return inner
        if kind == "word":
            words = []
            while self.peek()[0] == "word":
                words.append(self.take()[1])
            name = " ".join(words)
            if self.accept("("):
                return self.call(name)
            if len(words) > 1:
                raise ValueError("Write %r with its inputs in brackets, like %s( ... )." % (name, name))
            key = find_operator(name)
            if key is not None and _box_count(key) == 0:
                return self.make(key)                              # a constant such as pi
            return ("box", "")                                     # any other bare letter is an empty box
        if val is None:
            raise ValueError("The math ends too soon: something is missing at the end.")
        raise ValueError("Unexpected %r." % val)

    def call(self, name):
        key = find_operator(name)
        if key is None:
            raise ValueError("There is no operator called %r. Try its name from the Operators list, "
                             "or a short name such as sqrt, sin, ln." % name)
        args = []
        if not self.accept(")"):
            while True:
                args.append(self.expr())
                if self.accept(")"):
                    break
                if not self.accept(","):
                    raise ValueError("Expected , or ) in %s( ... )." % name)
        need = _box_count(key)
        if len(args) != need:
            raise ValueError("%s needs %d input(s) but was given %d." % (rows.get(key).NAME, need, len(args)))
        return self.make(key, *args)


def parse_math(text):
    """The operator tree for typed math.  Raises ValueError with a readable message."""
    return _Parser(text).parse()


def describe(node):
    """How the template reads, with brackets around nested parts, e.g.  '(2 + □) × 4'  (□ = an empty box)."""
    parts, j = [], 0
    for kind, text in node["mod"].LEFT:
        if kind == "box":
            slot = node["slots"][j]
            j += 1
            if isinstance(slot, dict):
                inner = describe(slot)
                first = slot["mod"].LEFT[0]
                parts.append(inner if first[0] == "op" and first[1].endswith("(") else "(" + inner + ")")
            else:
                parts.append(slot if slot else "□")
        else:
            parts.append(text)
    return " ".join(parts)


def empty_boxes(node):
    """How many boxes are still empty."""
    return sum(1 for kind, t, _path in row_tree.flatten(node) if kind == "box" and not t)


# ---------------------------------------------------------------- saved templates (a small JSON file)
def load_templates(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return [t for t in data if isinstance(t, str) and t.strip()]
    except (OSError, ValueError, TypeError):
        return []


def save_templates(path, templates):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(list(templates), f, ensure_ascii=False, indent=2)

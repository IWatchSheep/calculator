"""Shared numeric helpers used by several operator files (matrices, calculus, graphs, polynomials).

Not an operator: it has no folder of its own.  Operator files import it as
    from operators_one_operator_per_file import _helpers as H
"""
import ast
import cmath
import itertools
import math
from collections import deque
from fractions import Fraction


# ---------------------------------------------------------------- matrices
def fmat(A):
    return [[float(v) for v in row] for row in A]


def transpose(A):
    return [list(r) for r in zip(*A)]


def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def rref(A, tol=1e-10):
    """Reduced row echelon form -> (matrix, pivot columns)."""
    M = fmat(A)
    rows, cols = len(M), len(M[0])
    pivots, r = [], 0
    for c in range(cols):
        if r >= rows:
            break
        p = max(range(r, rows), key=lambda i: abs(M[i][c]))
        if abs(M[p][c]) < tol:
            continue
        M[r], M[p] = M[p], M[r]
        M[r] = [v / M[r][c] for v in M[r]]
        for i in range(rows):
            if i != r and abs(M[i][c]) > 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        pivots.append(c)
        r += 1
    return M, pivots


def nullspace(A):
    R, piv = rref(A)
    cols = len(R[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [0.0] * cols
        v[f] = 1.0
        for r, p in enumerate(piv):
            v[p] = -R[r][f]
        basis.append(v)
    return basis


def jacobi_eigen(S, sweeps=100):
    """Eigenvalues of a symmetric matrix (Jacobi rotations)."""
    A = fmat(S)
    n = len(A)
    for _ in range(sweeps):
        off = sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-22:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-300:
                    continue
                th = (A[q][q] - A[p][p]) / (2 * A[p][q])
                t = (1 if th >= 0 else -1) / (abs(th) + math.sqrt(th * th + 1))
                c = 1 / math.sqrt(t * t + 1)
                s = t * c
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p], A[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k], A[q][k] = c * apk - s * aqk, s * apk + c * aqk
    return sorted((A[i][i] for i in range(n)), reverse=True)


# ---------------------------------------------------------------- calculus
def simpson(f, a, b, n=1000):
    n += n % 2
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def shifted(point, i, d):
    return [p + d if j == i else p for j, p in enumerate(point)]


def partial(f, point, i, h=1e-5):
    return (f(*shifted(point, i, h)) - f(*shifted(point, i, -h))) / (2 * h)


def partial2(f, point, i, j, h=1e-4):
    return (partial(f, shifted(point, j, h), i, h) - partial(f, shifted(point, j, -h), i, h)) / (2 * h)


def as_vector(v):
    return [float(x) for x in v] if isinstance(v, (list, tuple)) else [float(v)]


def rk4(f, x0, y0, x_end, steps=1000):
    """Solve y' = f(x, y) from x0 to x_end (y may be a number or a list)."""
    h = (x_end - x0) / steps
    x, y = x0, y0
    vec = isinstance(y0, (list, tuple))
    add = (lambda a, b, s: [p + s * q for p, q in zip(a, b)]) if vec else (lambda a, b, s: a + s * b)
    for _ in range(steps):
        k1 = f(x, y)
        k2 = f(x + h / 2, add(y, k1, h / 2))
        k3 = f(x + h / 2, add(y, k2, h / 2))
        k4 = f(x + h, add(y, k3, h))
        if vec:
            y = [yi + h / 6 * (a + 2 * b + 2 * c + d) for yi, a, b, c, d in zip(y, k1, k2, k3, k4)]
        else:
            y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
    return y


def circle_integral(f, center, radius, n=2000):
    """Counter-clockwise contour integral of f(z) dz over a circle."""
    total = 0
    for k in range(n):
        t = 2 * math.pi * (k + 0.5) / n
        z = center + radius * cmath.exp(1j * t)
        total += f(z) * 1j * radius * cmath.exp(1j * t) * (2 * math.pi / n)
    return total


# ---------------------------------------------------------------- graphs
class _NeighbourSet(set):
    """The neighbours of a vertex, kept in the order they were met (a plain set lists letters in a
    different order every run, which changed which path / cycle the graph operators found).
    The Rust version keeps the same order."""

    def __init__(self):
        super().__init__()
        self._order = {}

    def add(self, x):
        self._order[x] = None
        super().add(x)

    def __iter__(self):
        return iter(self._order)


def undirected(graph):
    adj = {}
    for u, nbrs in graph.items():
        adj.setdefault(u, _NeighbourSet())
        for v in nbrs:
            v = v[0] if isinstance(v, tuple) else v
            adj.setdefault(v, _NeighbourSet())
            adj[u].add(v)
            adj[v].add(u)
    return adj


def components(adj):
    seen, comps = set(), []
    for s in adj:
        if s in seen:
            continue
        comp, q = set([s]), deque([s])
        seen.add(s)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    comp.add(v)
                    q.append(v)
        comps.append(comp)
    return comps


def edge_count(adj):
    return sum(len(n) for n in adj.values()) // 2 + sum(1 for u in adj if u in adj[u]) // 2


# ---------------------------------------------------------------- polynomials (text -> coefficients)
def poly_parse(text):
    """'(x+1)(x-1)' or 'x^2 - 1' -> {power: Fraction coefficient}."""
    text = text.replace("^", "**").replace("−", "-").replace("×", "*").replace("·", "*")
    # implicit multiplication:  )(  ->  )*(   ,   2x -> 2*x   ,   )x -> )*x   ,   x( -> x*(
    out = []
    for i, ch in enumerate(text):
        if out and ch in "(x" and (out[-1].isdigit() or out[-1] in ")x"):
            out.append("*")
        out.append(ch)
    tree = ast.parse("".join(out).strip(), mode="eval")

    def mul(a, b):
        r = {}
        for i, ca in a.items():
            for j, cb in b.items():
                r[i + j] = r.get(i + j, 0) + ca * cb
        return r

    def add(a, b, s=1):
        r = dict(a)
        for j, cb in b.items():
            r[j] = r.get(j, 0) + s * cb
        return r

    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return {0: Fraction(str(n.value))}
        if isinstance(n, ast.Name) and n.id == "x":
            return {1: Fraction(1)}
        if isinstance(n, ast.UnaryOp):
            v = ev(n.operand)
            return {k: -c for k, c in v.items()} if isinstance(n.op, ast.USub) else v
        if isinstance(n, ast.BinOp):
            a, b = ev(n.left), ev(n.right)
            if isinstance(n.op, ast.Add):
                return add(a, b)
            if isinstance(n.op, ast.Sub):
                return add(a, b, -1)
            if isinstance(n.op, ast.Mult):
                return mul(a, b)
            if isinstance(n.op, ast.Div) and list(b) == [0]:
                return {k: c / b[0] for k, c in a.items()}
            if isinstance(n.op, ast.Pow) and list(b) == [0] and b[0].denominator == 1 and b[0] >= 0:
                r = {0: Fraction(1)}
                for _ in range(int(b[0])):
                    r = mul(r, a)
                return r
        raise ValueError("Only polynomials in x with + - * / ** can be handled here.")

    return {k: c for k, c in ev(tree).items() if c != 0}


def poly_str(p):
    if not p:
        return "0"
    sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    out = []
    for k in sorted(p, reverse=True):
        c = p[k]
        mag = abs(c)
        num = str(mag.numerator) if mag.denominator == 1 else "%s/%s" % (mag.numerator, mag.denominator)
        body = (num if (mag != 1 or k == 0) else "") + ("" if k == 0 else "x" + (str(k).translate(sup) if k > 1 else ""))
        out.append(("-" if c < 0 else "+", body))
    s = ("-" if out[0][0] == "-" else "") + out[0][1]
    for sign, body in out[1:]:
        s += " %s %s" % (sign, body)
    return s


def poly_eval(p, x):
    return sum(float(c) * x ** k for k, c in p.items())


def poly_divide_linear(p, r):
    """Divide polynomial p (dict) by (x - r) with r a Fraction; returns the quotient."""
    deg = max(p)
    coeffs = [p.get(k, Fraction(0)) for k in range(deg, -1, -1)]
    q, carry = [], Fraction(0)
    for c in coeffs:
        carry = c + carry * r
        q.append(carry)
    rem = q.pop()
    assert rem == 0
    return {deg - 1 - i: c for i, c in enumerate(q) if c != 0}


def poly_factor(p):
    """Factor over the rationals using rational roots; returns a string."""
    if not p:
        return "0"
    p = dict(p)
    common = Fraction(1)
    lead = p[max(p)]
    factors = []
    while p and max(p) >= 1:
        lowest = min(p)
        if lowest > 0:
            factors.append("x")
            p = {k - 1: c for k, c in p.items()}
            continue
        found = None
        a0, an = abs(p[0]), abs(p[max(p)])
        num = Fraction(a0).limit_denominator(10 ** 6)
        den = Fraction(an).limit_denominator(10 ** 6)
        if num.denominator == 1 and den.denominator == 1:
            def divisors(n):
                n = int(n)
                return [d for d in range(1, abs(n) + 1) if n % d == 0][:400] if n else [1]
            for pn in divisors(num.numerator):
                for qd in divisors(den.numerator):
                    for sgn in (1, -1):
                        r = Fraction(sgn * pn, qd)
                        if sum(c * r ** k for k, c in p.items()) == 0:
                            found = r
                            break
                    if found is not None:
                        break
                if found is not None:
                    break
        if found is None:
            break
        p = poly_divide_linear(p, found)
        factors.append("x" if found == 0 else "(x %s %s)" % ("-" if found > 0 else "+", abs(found)))
    rest = poly_str(p) if p else "1"
    if p and not (len(p) == 1 and 0 in p and p[0] == 1):
        factors.insert(0, "(" + rest + ")" if len(p) > 1 or max(p) > 0 else rest)
    return " ".join(factors) if factors else rest

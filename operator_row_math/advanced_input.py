"""Advanced Input: values the number pad can't type - lists, matrices, functions, sets, graphs.

KINDS lists what can be entered (title, help text, example).  parse(kind, text) turns what the user
typed into a python value that an operator's compute() accepts.  Nothing here uses eval() on raw text:
functions are checked against a small whitelist of syntax and names first.
"""
import ast
import cmath
import math
import re

# id, title, how to type it, example
KINDS = [
    ("number", "Number", "One number.", "3.5"),
    ("list", "List / vector of numbers", "Numbers separated by commas or spaces.", "1, 2, 3, 4"),
    ("matrix", "Matrix", "Rows separated by ;  (or a new line). Numbers in a row separated by spaces or commas.",
     "1 2; 3 4"),
    ("function", "Function of x", "Type it with x.  + - * / ** %   sin cos tan sqrt exp log abs pi e",
     "x**2 + 3*x"),
    ("multi", "Function of several variables (x, y, z)",
     "Use x, y, z in that order.  For a gradient, give a list: [2*x, 2*y].", "x**2 + y**2"),
    ("predicate", "True / false test on x", "A test using x:  >  <  >=  <=  ==  !=  and  or  not", "x > 2"),
    ("set", "Set / group of items", "Items separated by commas. Numbers or names.", "1, 2, 3"),
    ("pairs", "List of pairs (edges)", "Pairs in brackets, separated by commas.", "(0,1), (1,2), (2,0)"),
    ("graph", "Graph (each vertex and its neighbours)", "Vertex: neighbours, one vertex per ;",
     "A: B, C; B: C; C: A"),
    ("wgraph", "Weighted graph (neighbour=weight)", "Vertex: neighbour=weight, one vertex per ;",
     "A: B=4, C=1; B: C=2; C:"),
    ("text", "Text (a formula to rewrite)", "A polynomial in x written normally.", "(x+1)(x-1)"),
    ("setfamily", "Several sets", "Each set in braces, separated by commas.", "{1,2}, {2,3}, {1,2,3}, {}"),
    ("item", "A number or a name", "One number or one name (a vertex, a group element).", "A"),
]
KIND_IDS = [k[0] for k in KINDS]

# what an input usually is, by the name of compute()'s parameter
NAME_KIND = {
    "f": "function", "g": "function", "fprime": "function", "gprime": "function", "grad_f": "multi",
    "predicate": "predicate", "op": "multi", "d": "multi",
    "data": "list", "terms": "list", "values": "list", "probs": "list", "elements": "list",
    "resistors": "list", "xs": "list", "ys": "list", "derivs": "list", "observed": "list",
    "expected": "list", "fixed_counts": "list", "point": "list", "x": "list", "y": "list", "X": "list",
    "v": "list", "A": "matrix", "B": "matrix", "b": "list", "graph": "graph", "edges": "pairs",
    "start": "item", "n": "number", "k": "number", "z": "number", "identity": "item", "g_": "item",
    "domain": "set", "codomain": "set", "universe": "set", "s": "set", "a": "list", "H": "set", "G": "set",
    "x0": "number", "y0": "number", "h": "number", "steps": "number", "i": "number", "r": "number",
    "p": "number", "lr": "number",
}
# operator-specific corrections (folder name -> kind of each input, in order)
OP_KINDS = {
    "shortest_path_dijkstra": ["wgraph", "item"],
    "vertex_degree": ["graph", "item"],
    "order_of_element": ["item", "multi", "item"],
    "coset": ["item", "set", "multi"],
    "element_of": ["item", "set"], "not_element_of": ["item", "set"],
    "complement": ["set", "set"], "cardinality": ["set"], "union": ["set", "set"],
    "intersection": ["set", "set"], "set_difference": ["set", "set"], "subset_or_equal": ["set", "set"],
    "proper_subset": ["set", "set"], "cartesian_product": ["set", "set"], "power_set": ["set"],
    "direct_product": ["set", "set"], "order_of_group": ["set"],
    "injective": ["function", "set"], "surjective": ["function", "set", "set"],
    "bijective": ["function", "set", "set"],
    "for_all": ["predicate", "set"], "there_exists": ["predicate", "set"],
    "matrix_add": ["matrix", "matrix"], "matrix_subtract": ["matrix", "matrix"],
    "matrix_multiply": ["matrix", "matrix"], "scalar_multiply": ["number", "matrix"],
    "solve_ax_b": ["matrix", "list"], "gaussian_elimination": ["matrix", "list"],
    "gauss_seidel_iteration": ["matrix", "list"], "jacobi_iteration": ["matrix", "list"],
    "gradient": ["multi", "list"], "partial_derivative": ["multi", "list", "number"],
    "gradient_descent": ["multi", "list"],
    "definite_integral": ["function", "number", "number"], "derivative": ["function", "number"],
    "second_derivative": ["function", "number"], "lagrange_interpolation": ["list", "list", "number"],
    "newton_interpolation": ["list", "list", "number"], "euler_s_method": ["multi", "number", "number", "number", "number"],
    "runge_kutta_rk4": ["multi", "number", "number", "number", "number"],
    "open_ball": ["multi", "list", "list", "number"], "z_transform": ["list", "number"],
    "norm": ["list"], "percentile": ["list", "number"], "lipschitz_ratio": ["function", "number", "number"],
    "riemannstieltjes_sum": ["function", "function", "list"],
    "maclaurin_series": ["list", "number"], "taylor_series": ["list", "number", "number"],
    "adjacency_matrix": ["number", "pairs"], "lp_norm": ["function", "number", "number"],
    "bisection_method": ["function", "number", "number"], "secant_method": ["function", "number", "number"],
    "simpson_s_rule": ["function", "number", "number"], "trapezoid_rule": ["function", "number", "number"],
    "convolution": ["list", "list"],
    "mean_value_theorem": ["function", "number", "number"], "riemann_sum": ["function", "number", "number", "number"],
}


try:
    from operator_row_math.kinds_extra import EXTRA
    OP_KINDS.update(EXTRA)
except ImportError:
    pass


def kinds_for(folder_name, input_names):
    """Kind id for each input of an operator, in order."""
    if OP_KINDS.get(folder_name):
        return list(OP_KINDS[folder_name])
    return [NAME_KIND.get(n, "list") for n in input_names]


def kind_title(kind):
    return next((t for i, t, _h, _e in KINDS if i == kind), kind)


# ------------------------------------------------------------------ parsing
def _num(tok):
    tok = tok.strip()
    try:
        return int(tok)
    except ValueError:
        return float(tok)


def _item(tok):
    tok = tok.strip()
    try:
        return _num(tok)
    except ValueError:
        return tok.strip("'\"")


def _split(text):
    return [t for t in text.replace(",", " ").replace("[", " ").replace("]", " ").split() if t]


_FUNCS = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "asin": math.asin, "acos": math.acos,
          "atan": math.atan, "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh, "sqrt": math.sqrt,
          "exp": math.exp, "log": math.log, "ln": math.log, "log10": math.log10, "abs": abs,
          "floor": math.floor, "ceil": math.ceil, "min": min, "max": max}
_CFUNCS = dict(_FUNCS, **{n: getattr(cmath, n) for n in
                          ("sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "tanh", "sqrt", "exp", "log", "log10")})
_CFUNCS["ln"] = cmath.log
_CONST = {"pi": math.pi, "e": math.e}
_VARS = ["x", "y", "z", "t", "u", "w"]
_OK = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.BoolOp, ast.Compare, ast.Call, ast.Name, ast.Constant,
       ast.Load, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.FloorDiv, ast.USub, ast.UAdd,
       ast.And, ast.Or, ast.Not, ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.List, ast.Tuple,
       ast.Subscript, ast.IfExp)


def make_function(expr):
    """Turn text like 'x**2 + 3*x' into a callable.  Variables x, y, z, t... take the arguments in order."""
    expr = expr.strip().replace("^", "**").replace("×", "*").replace("÷", "/").replace("−", "-")
    if expr.lower().startswith("lambda"):
        raise ValueError("Just type the expression, for example  x**2 + 3*x")
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError:
        raise ValueError("I can't read that function. Example:  x**2 + 3*x")
    used = []
    for n in ast.walk(tree):
        if not isinstance(n, _OK):
            raise ValueError("That function uses something not allowed here.")
        if isinstance(n, ast.Call):
            if not (isinstance(n.func, ast.Name) and n.func.id in _FUNCS) or n.keywords:
                raise ValueError("Allowed functions: " + ", ".join(sorted(_FUNCS)))
        if isinstance(n, ast.Name) and n.id not in _FUNCS and n.id not in _CONST:
            if n.id not in _VARS:
                raise ValueError("Unknown name '%s'. Use x, y, z, t (variables), pi or e." % n.id)
            if n.id not in used:
                used.append(n.id)
    code = compile(tree, "<function>", "eval")
    names = sorted(used, key=_VARS.index)

    def fn(*args):
        if len(args) == 1 and isinstance(args[0], (list, tuple)) and len(names) > 1:
            args = tuple(args[0])
        env = dict(_CFUNCS if any(isinstance(a, complex) for a in args) else _FUNCS, **_CONST)
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            env.update({"x": args[0]})            # x[0], x[1] style
        elif len(args) == 1 and len(names) == 1:
            env[names[0]] = args[0]               # a one-variable function: z, t ... work too
        else:
            for nm, v in zip(_VARS, args):
                env[nm] = v
        missing = [n for n in names if n not in env]
        if missing:
            raise ValueError("The function needs %s but only %d value(s) were given." % (", ".join(missing), len(args)))
        return eval(code, {"__builtins__": {}}, env)       # noqa: S307  (syntax + names checked above)
    fn.text = expr
    return fn


def parse(kind, text):
    """Typed text -> python value.  Raises ValueError with a friendly message."""
    text = text.strip()
    if not text:
        raise ValueError("Type something first (see the example).")
    try:
        if kind == "number":
            return _num(text)
        if kind == "list":
            return [_num(t) for t in _split(text)]
        if kind == "matrix":
            rows = [r for r in text.replace("[", " ").replace("]", " ").replace("\n", ";").split(";") if r.strip()]
            m = [[_num(t) for t in r.replace(",", " ").split()] for r in rows]
            if len({len(r) for r in m}) != 1:
                raise ValueError("Every row of the matrix needs the same number of entries.")
            return m
        if kind in ("function", "multi", "predicate"):
            return make_function(text)
        if kind == "set":
            return set(_item(t) for t in text.strip("{}").split(",") if t.strip())
        if kind == "pairs":
            body = text if text.startswith("[") else "[" + text + "]"
            v = ast.literal_eval(body)
            return [tuple(p) for p in v]
        if kind in ("graph", "wgraph"):
            g = {}
            for part in text.split(";"):
                if not part.strip():
                    continue
                head, _, rest = part.partition(":")
                nbrs = []
                for tok in rest.split(","):
                    if not tok.strip():
                        continue
                    if kind == "wgraph":
                        name, _, w = tok.partition("=")
                        nbrs.append((_item(name), _num(w)))
                    else:
                        nbrs.append(_item(tok))
                g[_item(head)] = nbrs
            return g
        if kind == "item":
            return _item(text)
        if kind == "text":
            return text
        if kind == "setfamily":
            groups = re.findall(r"\{([^{}]*)\}", text)
            if not groups:
                raise ValueError("Put each set in braces, e.g. {1,2}, {2,3}")
            return [frozenset(_item(t) for t in g.split(",") if t.strip()) for g in groups]
    except ValueError as e:
        if str(e).startswith("Every row") or str(e).startswith("Type"):
            raise
        raise ValueError("I can't read that as a %s. Example: %s" % (kind_title(kind).lower(), example(kind)))
    except (SyntaxError, TypeError):
        raise ValueError("I can't read that as a %s. Example: %s" % (kind_title(kind).lower(), example(kind)))
    raise ValueError("Unknown input type.")


def example(kind):
    return next((e for i, _t, _h, e in KINDS if i == kind), "")


def short_label(text, width=10):
    """What shows inside the card for an advanced value."""
    t = " ".join(text.split())
    return t if len(t) <= width else t[:width - 1] + "…"

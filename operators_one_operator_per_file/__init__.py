"""Operator library: one operator (formula) per file.

Layout:  operators_one_operator_per_file/<category>/<subcategory>/<operator>/<operator>.py
                                                                  and <operator>.jpg (diagram)

Every operator file defines NAME, SYMBOL, CATEGORY, SUBCATEGORY, FORMULA and a
compute(...) function.  Operators marked "reference only" in INDEX.md document
the formula but do not calculate anything yet.

Nothing in the calculator imports these yet.  When you are ready:

    from operators_one_operator_per_file import load_all, get
    ops = load_all()
    get("math/algebra/quadratic_formula").compute(1, -3, 2)
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))


def _load(path):
    spec = importlib.util.spec_from_file_location("op_" + str(abs(hash(path))), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_all():
    """Return {"math/algebra/quadratic_formula": module, ...}, one entry per operator folder."""
    ops = {}
    for folder, _dirs, files in os.walk(_ROOT):
        name = os.path.basename(folder)
        if name + ".py" in files:
            key = os.path.relpath(folder, _ROOT).replace(os.sep, "/")
            ops[key] = _load(os.path.join(folder, name + ".py"))
    return ops


def get(key):
    """Load one operator by key, e.g. get("math/algebra/quadratic_formula")."""
    folder = os.path.join(_ROOT, *key.split("/"))
    return _load(os.path.join(folder, os.path.basename(folder) + ".py"))


def diagram_path(key):
    """Path of the operator's JPEG diagram (small-square drawing)."""
    folder = os.path.join(_ROOT, *key.split("/"))
    return os.path.join(folder, os.path.basename(folder) + ".jpg")

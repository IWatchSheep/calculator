"""One folder per operator, each holding a python file that places the operator inside a row.

Layout:  operator_row_math/<category>/<subcategory>/<operator>/<operator>.py
(the same keys as operators_one_operator_per_file, e.g. "math/arithmetic/addition")

Each operator file defines NAME, KEY, PATTERN, LEFT, RIGHT and
    place(parent, stacked=False) -> tk.Frame
Try one:  python operator_row_math/preview.py math/arithmetic/addition
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))


def get(key):
    """Load one operator's row module by key, e.g. get("math/arithmetic/addition")."""
    folder = os.path.join(_ROOT, *key.split("/"))
    path = os.path.join(folder, os.path.basename(folder) + ".py")
    spec = importlib.util.spec_from_file_location("row_" + key.replace("/", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def keys():
    """Every operator key that has a row folder."""
    out = []
    for folder, _dirs, files in os.walk(_ROOT):
        n = os.path.basename(folder)
        if n + ".py" in files:
            out.append(os.path.relpath(folder, _ROOT).replace(os.sep, "/"))
    return sorted(out)

"""One folder per algebra word problem, each holding a python file that places the problem inside a row of the calculator.

Layout:  operator_row_math_for_algebra_word_problems/<category>/<id>/<id>.py
(the same keys as operators_one_algebra_word_problem_per_file, e.g. "savings/0848")

Each file defines NAME, KEY, LIBRARY_KEY, PATTERN, CALC, INPUTS, DEFAULTS, KINDS, LEFT, RIGHT and
    place(parent, stacked=False) -> tk.Frame
The row is   Savings 0848( [] , [] , [] , [] ) = []   : one box for every number in the problem, and the answer in the box right of "=".
Try one:  python operator_row_math_for_algebra_word_problems/preview.py savings/0848
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))


def get(key):
    """Load one problem's row module by key, e.g. get("savings/0848")."""
    category, pid = key.split("/")
    path = os.path.join(_ROOT, category, pid, pid + ".py")
    spec = importlib.util.spec_from_file_location("wprow_" + key.replace("/", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def keys():
    """Every problem key that has a row folder."""
    out = []
    for category in sorted(os.listdir(_ROOT)):
        folder = os.path.join(_ROOT, category)
        if os.path.isdir(folder) and not category.startswith("__"):
            for pid in sorted(os.listdir(folder)):
                if os.path.exists(os.path.join(folder, pid, pid + ".py")):
                    out.append(category + "/" + pid)
    return out

"""Algebra word problem library: one problem per file, with a diagram of the problem.

Layout:  operators_one_algebra_word_problem_per_file/<category>/<id>/<id>.py
                                                                  and <id>.jpg (diagram)
e.g.     operators_one_algebra_word_problem_per_file/savings/0848/0848.py   key "savings/0848"

Every problem file defines ID, KEY, NAME, CATEGORY, PROBLEM, LET, EQUATION, SOLVE, ANSWER, SOLVER, FAMILY, TEMPLATE, NUMBERS and compute(*numbers).
SOLVER says who answers the problem today ("word_solver", "number_puzzle" or None = reference only); see INDEX.md.  The files are written by
operator_keys/make_algebra_word_problem_files.py from algebra_word_problems/algebra_word_problems.txt (1,000 problems).

    from operators_one_algebra_word_problem_per_file import get, keys
    get("savings/0848").compute()                  # 16, the stored numbers
    get("savings/0848").compute(200, 15, 350, 5)   # your own numbers, in the order of NUMBERS
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))


def _load(path):
    spec = importlib.util.spec_from_file_location("wp_" + str(abs(hash(path))), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def keys():
    """Every problem key, e.g. "savings/0848", in order."""
    out = []
    for category in sorted(os.listdir(_ROOT)):
        folder = os.path.join(_ROOT, category)
        if os.path.isdir(folder) and not category.startswith("__"):
            for pid in sorted(os.listdir(folder)):
                if os.path.exists(os.path.join(folder, pid, pid + ".py")):
                    out.append(category + "/" + pid)
    return out


def get(key):
    """Load one problem by key, e.g. get("savings/0848")."""
    category, pid = key.split("/")
    return _load(os.path.join(_ROOT, category, pid, pid + ".py"))


def load_all():
    """{key: module} for every problem (loads 1,000 small files)."""
    return {k: get(k) for k in keys()}

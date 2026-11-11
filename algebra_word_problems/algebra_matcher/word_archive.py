"""Find algebra word-problem answers the way the chess program uses its four lists and its archive.

A problem is a position. A legal move is one reading of its stored equation: each number in the
equation is one of the problem's numbers, or a fixed number such as the 1 in "= 1". The move is
kept only when solving that equation gives the stored answer. A wrong number is never kept.

List 1  the equation shape of this problem (the variable, the operations). It does not read the archive.
List 2  the ways to attach the problem's numbers to the equation, the match first.
List 3  what past runs did with the same wording: proven, tried, or never tried.
List 4  the result those past runs actually got. Empty until a run has matched.

A wording is proven only when the same reading matches every stored problem of that wording, and
there are at least two of them. One match is only a candidate. = on a new sentence is not this file.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROBLEMS = os.path.join(ROOT, "operators_one_algebra_word_problem_per_file")
ARCHIVE = os.path.join(HERE, "word_archive.json")


def _normalize(equation):
    equation = equation.replace("×", "*").replace("−", "-").replace("–", "-").replace("·", "*")
    previous = None
    while previous != equation:
        previous = equation
        equation = re.sub(r"(\d)\s*([A-Za-z])", r"\1*\2", equation)
        equation = re.sub(r"(\d)\s*\(", r"\1*(", equation)
        equation = re.sub(r"([A-Za-z])\s*\(", r"\1*(", equation)
        equation = re.sub(r"\)\s*(\d)", r")*\1", equation)
        equation = re.sub(r"\)\s*([A-Za-z])", r")*\1", equation)
        equation = re.sub(r"\)\s*\(", r")*(", equation)
    return equation


def _answer_number(text):
    match = re.search(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    return float(match.group(0)) if match else None


def _literals(equation):
    """Numbers written in the equation, left to right, and the one letter that is the unknown."""
    letters = set(re.findall(r"[A-Za-z]", equation))
    if len(letters) != 1:
        return None, []
    return letters.pop(), [float(n) for n in re.findall(r"\d+(?:\.\d+)?", equation)]


def solve_equation(equation):
    """The unknown in a school equation with one letter, or None when this reader cannot take it."""
    if any(mark in equation for mark in ";≥≤<>%√π^"):
        return None
    equation = _normalize(equation)
    sides = equation.split("=")
    if len(sides) != 2:
        return None
    variable, _ = _literals(equation)
    if variable is None:
        return None
    expression = "(%s)-(%s)" % (sides[0], sides[1])

    def f(x):
        return eval(expression, {"__builtins__": {}}, {variable: float(x)})

    for start in (0.0, 1.0, 2.0, 0.5, 10.0, 0.25, 5.0, -2.0, 20.0, 50.0, 8.0, 100.0, -10.0):
        x = float(start)
        good = True
        for _ in range(50):
            try:
                y = f(x)
                y2 = f(x + 1e-6)
            except Exception:
                good = False
                break
            slope = (y2 - y) / 1e-6
            if abs(slope) < 1e-14:
                good = False
                break
            nxt = x - y / slope
            if abs(nxt - x) < 1e-9:
                x = nxt
                break
            x = nxt
        if not good:
            continue
        try:
            if abs(f(x)) < 1e-5:
                return round(x, 8)
        except Exception:
            continue
    return None


def _bind(literals, numbers):
    """Each equation number is the index of a problem number, or None when it is a fixed number."""
    pool = [float(n) for n in numbers]
    binding = []
    for literal in literals:
        found = None
        for i, number in enumerate(pool):
            if abs(number - literal) <= 1e-9 * max(1.0, abs(literal)):
                found = i
                break
        binding.append(found)
    return binding


def load_problems():
    """Every generated problem: reference ones and ready ones."""
    import importlib.util
    found = []
    for folder, _dirs, files in os.walk(PROBLEMS):
        name = os.path.basename(folder)
        if name + ".py" not in files:
            continue
        path = os.path.join(folder, name + ".py")
        spec = importlib.util.spec_from_file_location("prob_" + name + "_" + str(len(found)), path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        found.append(module)
    return found


def lists_for(problem):
    """The four lists for one problem. List 3 and List 4 read the archive file when it exists."""
    equation = problem.EQUATION
    variable, literals = _literals(_normalize(equation))
    numbers = list(problem.NUMBERS)
    binding = _bind(literals, numbers) if variable else []
    solved = solve_equation(equation)
    answer = _answer_number(problem.ANSWER)
    matched = solved is not None and answer is not None and abs(solved - answer) <= 1e-4 * max(1.0, abs(answer))
    archive = _read_archive()
    row = archive.get("templates", {}).get(problem.TEMPLATE, {})
    list1 = [{
        "variable": variable,
        "operations": [mark for mark in "+-*/()" if mark in _normalize(equation)],
        "shape": "one letter" if variable else "not one letter",
    }]
    list2 = [{
        "binding": binding,
        "solved": solved,
        "stored_answer": answer,
        "matched": matched,
    }]
    list3 = [{
        "wording": problem.TEMPLATE,
        "status": "proven" if row.get("proven") else ("tried" if row.get("tried") else "never tried"),
        "tried": row.get("tried", 0),
        "matched": row.get("matched", 0),
    }]
    list4 = []
    if row.get("proven"):
        list4.append({"pattern": row.get("pattern"), "played": row.get("matched", 0)})
    return {"list1": list1, "list2": list2, "list3": list3, "list4": list4}


def _read_archive():
    if not os.path.isfile(ARCHIVE):
        return {"templates": {}}
    with open(ARCHIVE, encoding="utf-8") as handle:
        return json.load(handle)


def run(reference_only=True):
    """Play one game for every problem: solve its equation and keep the game when the answer matches.

    Returns the archive. A wording with two or more problems is proven only when every one matches.
    """
    groups = {}
    for problem in load_problems():
        if reference_only and problem.SOLVER is not None:
            continue
        info = lists_for(problem)
        groups.setdefault(problem.TEMPLATE, []).append(info["list2"][0])
    templates = {}
    proven = candidates = skipped = 0
    for wording, games in groups.items():
        matched = [g for g in games if g["matched"]]
        record = {
            "tried": len(games),
            "matched": len(matched),
            "pattern": wording,
            "proven": len(games) >= 2 and len(matched) == len(games),
        }
        templates[wording] = record
        if record["proven"]:
            proven += 1
        elif matched:
            candidates += 1
        else:
            skipped += 1
    archive = {"templates": templates, "proven_wordings": proven, "candidate_wordings": candidates, "unmatched_wordings": skipped}
    with open(ARCHIVE, "w", encoding="utf-8") as handle:
        json.dump(archive, handle, indent=1)
    return archive


if __name__ == "__main__":
    result = run()
    print("proven wordings: %d" % result["proven_wordings"])
    print("candidate wordings (one matching problem): %d" % result["candidate_wordings"])
    print("unmatched wordings: %d" % result["unmatched_wordings"])

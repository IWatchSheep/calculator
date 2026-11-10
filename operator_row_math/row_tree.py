"""A row's left side as a tree: an operator whose boxes ("slots") can each hold a number or another operator.

    node = {"key": "math/arithmetic/addition", "mod": <row module>, "slots": [slot, slot, ...]}
    slot = a number typed as text (a str, "" while empty)  or  another node

The k-th box of the operator's LEFT cards is slot k.  Expanding a box replaces the slot with a new node.
"""
import math
import types

import operator_row_math
import operator_row_math_for_algebra_word_problems as word_rows
import operators_one_algebra_word_problem_per_file as word_library
import operators_one_operator_per_file as library

WORD_PREFIX = "word:"      # a node key "word:savings/0848" is an algebra word problem, not an operator


# a plain number used as a whole row (e.g. the "× □" after a bracket)
NUMBER = types.SimpleNamespace(NAME="Number", KEY="_number", PATTERN="□", CALC="ready", INPUTS=["value"],
                               KINDS=["number"], LEFT=[("box", "")], RIGHT=[])

JOINS = {
    "+": lambda a, b: a + b, "−": lambda a, b: a - b, "×": lambda a, b: a * b, "÷": lambda a, b: a / b,
    "=": lambda a, b: abs(a - b) <= 1e-3 * max(1.0, abs(a), abs(b)),   # numerical results: close enough
    "≠": lambda a, b: abs(a - b) > 1e-3 * max(1.0, abs(a), abs(b)),
    "<": lambda a, b: a < b, ">": lambda a, b: a > b, "≤": lambda a, b: a <= b, "≥": lambda a, b: a >= b,
}


def join(symbol, a, b):
    """Combine two row results with a join symbol; raises ValueError for things like ÷ 0."""
    if isinstance(a, (list, tuple, set, frozenset, dict)) or isinstance(b, (list, tuple, set, frozenset, dict)):
        raise ValueError("Can't join those two results with %s: a list of answers can't be joined (Python would repeat or glue the lists)." % symbol)
    try:
        return JOINS[symbol](a, b)
    except ZeroDivisionError:
        raise ValueError("Division by zero.")
    except TypeError:
        raise ValueError("Can't join those two results with %s." % symbol)


def build_node(spec):
    """A row's operator with its boxes pre-filled from spec = {"op": key, "fill": {box number: value | spec}}."""
    node = new_node(spec["op"])
    for j, v in spec.get("fill", {}).items():
        node["slots"][j] = build_node(v) if isinstance(v, dict) else str(v)
    return node


def slot_map(mod):
    """For each box card of the row's LEFT cards (left to right): which input (slot) it shows.  A formula that writes a variable twice, like the r in
    A = pi r (r + l), has two box cards for one input: mod.SLOTS = [0, 0, 1].  Without SLOTS the k-th box is slot k."""
    n = sum(1 for kind, _ in mod.LEFT if kind == "box")
    return list(getattr(mod, "SLOTS", None) or range(n))


def slot_count(mod):
    """How many inputs the operator has (the number of distinct slots, not of box cards)."""
    m = slot_map(mod)
    return max(m) + 1 if m else 0


def inputs_in_box_order(mod):
    """The operator's input names in the order its boxes appear on the row (a repeated variable is named once)."""
    names, seen = [], set()
    for j in slot_map(mod):
        if j not in seen and j < len(mod.INPUTS):
            seen.add(j)
            names.append(mod.INPUTS[j])
    return names


def clear_outputs(node):
    """Forget the answers shown in the answer boxes (something was changed)."""
    if isinstance(node, dict) and "mod" in node:
        node.pop("out", None)
        for slot in node["slots"]:
            clear_outputs(slot)


def new_node(key):
    if key == "_number":
        return {"key": key, "mod": NUMBER, "slots": [""]}
    mod = word_rows.get(key[len(WORD_PREFIX):]) if key.startswith(WORD_PREFIX) else operator_row_math.get(key)
    count = slot_count(mod)
    # a word problem starts with its own numbers in the boxes (change them and press =); an operator starts empty
    slots = [str(d) for d in mod.DEFAULTS] if key.startswith(WORD_PREFIX) and len(getattr(mod, "DEFAULTS", [])) == count else [""] * count
    return {"key": key, "mod": mod, "slots": slots}


def flatten(node, path=()):
    """Cards left to right: [(kind, text, path)].  Box cards carry the path of the slot they show."""
    out, smap, b, seen, o = [], slot_map(node["mod"]), 0, set(), 0
    for kind, text in node["mod"].LEFT:
        if kind == "box":
            j = smap[b]
            b += 1
            slot = node["slots"][j]
            if j in seen:                     # the same variable written again: a copy of the box, it shows (and selects) the same slot
                if isinstance(slot, dict) and "adv" in slot:
                    out.append(("box", slot["label"], path + (j,)))
                elif isinstance(slot, dict):
                    out.append(("box", slot["mod"].NAME, path + (j,)))
                else:
                    out.append(("box", slot, path + (j,)))
                continue
            seen.add(j)
            if isinstance(slot, dict) and "adv" in slot:
                out.append(("box", slot["label"], path + (j,)))
            elif isinstance(slot, dict):
                out.extend(flatten(slot, path + (j,)))
            else:
                out.append(("box", slot, path + (j,)))
        elif kind == "dec":                   # a box the picture draws that is not an input (the second box of A (+) B): shown, never typed into
            out.append(("dec", text, None))
        elif kind == "out":                   # the answer box of the formula, e.g. the A of A = pi r^2: filled in by =, never typed into
            shown = node.get("out", "")
            out.append(("out", shown[o] if isinstance(shown, list) else shown, None))
            o += 1
        else:
            out.append(("op", text, None))
    return out


def get_slot(node, path):
    for j in path:
        node = node["slots"][j]
    return node


def owner(node, path):
    """(operator node, input number) that the box at `path` belongs to."""
    for j in path[:-1]:
        node = node["slots"][j]
    return node, path[-1]


def advanced_slot(kind, text, value, label):
    """A box filled from the Advanced Input window."""
    return {"adv": True, "kind": kind, "text": text, "value": value, "label": label}


def set_slot(node, path, value):
    for j in path[:-1]:
        node = node["slots"][j]
    node["slots"][path[-1]] = value


def fmt(x):
    """Show a result: 2 not 2.0, i for imaginary, tuples/lists as (a, b)."""
    if isinstance(x, bool):
        return "yes" if x else "no"
    if isinstance(x, complex):
        if abs(x.imag) < 1e-12:
            return fmt(x.real)
        re = "" if abs(x.real) < 1e-12 else fmt(x.real)
        im = fmt(abs(x.imag)) + "i"
        sign = "-" if x.imag < 0 else ("+" if re else "")
        return re + sign + im
    if isinstance(x, (int, float)):
        x = float(x)
        if math.isnan(x) or math.isinf(x):
            return str(x)
        return str(int(x)) if x.is_integer() and abs(x) < 1e15 else "%.10g" % x
    if isinstance(x, (tuple, list)):
        return "(" + ", ".join(fmt(v) for v in x) + ")"
    if isinstance(x, (set, frozenset)):
        return "{" + ", ".join(fmt(v) for v in sorted(x, key=str)) + "}"
    if isinstance(x, dict):
        return "{" + ", ".join("%s: %s" % (fmt(k), fmt(v)) for k, v in x.items()) + "}"
    return str(x)


def evaluate(node):
    """Calculate the tree and remember the answer in the node's answer box (if the formula has one).  Raises ValueError(message) when it can't."""
    result = _evaluate(node)
    outs = sum(1 for kind, _ in node["mod"].LEFT if kind == "out")
    if outs > 1 and isinstance(result, (tuple, list)) and len(result) == outs:
        node["out"] = [fmt(v) for v in result]        # (x1, x2) = ...: each answer box shows its own answer
    elif outs:
        node["out"] = fmt(result)
    return result


def _evaluate(node):
    mod = node["mod"]
    if mod.CALC == "reference":
        raise ValueError("%s is reference only: it shows the formula but can't calculate yet." % mod.NAME)
    vals = []
    for slot in node["slots"]:
        if isinstance(slot, dict) and "adv" in slot:
            vals.append(slot["value"])
        elif isinstance(slot, dict):
            v = evaluate(slot)
            if mod.CALC == "advanced" or node["key"] == "_number":      # the plain number around a row passes any result through (several answers come back as a list)
                vals.append(v)
                continue
            if isinstance(v, bool) or not isinstance(v, (int, float, complex)):
                raise ValueError("%s gives %s, which can't be used as a single number inside %s."
                                 % (slot["mod"].NAME, fmt(v), mod.NAME))
            vals.append(v)
        else:
            try:
                vals.append(int(slot))          # whole numbers stay whole (factorial, n choose k ...)
            except ValueError:
                try:
                    vals.append(float(slot))
                except ValueError:
                    raise ValueError("Fill every square box first (number pad, or Advanced Input for lists, "
                                     "matrices and functions).")
    if node["key"] == "_number":
        return vals[0]
    try:
        if node["key"].startswith(WORD_PREFIX):
            # the boxes are the numbers of the equation that are also in the problem text; the other text numbers stay as written
            problem = word_library.get(node["key"][len(WORD_PREFIX):])
            full = list(problem.NUMBERS)
            for place, value in zip(mod.BOX_INDEX, vals):
                full[place] = value
            return problem.compute(*full)
        return library.get(node["key"]).compute(*vals)
    except ZeroDivisionError:
        raise ValueError("Division by zero.")
    except NotImplementedError as e:
        raise ValueError("%s is reference only: %s" % (mod.NAME, e))
    except (ValueError, OverflowError, TypeError, KeyError, IndexError, AttributeError) as e:
        raise ValueError("%s can't calculate that: %s" % (mod.NAME, e))

"""Path   [path]

Category : Math > Graph theory and combinatorics
Formula  : A sequence of distinct vertices where consecutive vertices are joined by edges

Status   : ready to use - call compute(graph, start, end)
"""

NAME = 'Path'
SYMBOL = 'path'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A sequence of distinct vertices where consecutive vertices are joined by edges'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph, start, end):
    """A shortest path of distinct vertices from start to end, as a list"""
    adj = H.undirected(graph)
    prev, queue = {start: None}, [start]
    for u in queue:
        for v in sorted(adj.get(u, ()), key=str):
            if v not in prev:
                prev[v] = u
                queue.append(v)
    if end not in prev:
        raise ValueError("no path from start to end")
    out, u = [], end
    while u is not None:
        out.append(u)
        u = prev[u]
    return out[::-1]

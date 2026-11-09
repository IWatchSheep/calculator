"""Max flow min cut   [max-flow = min-cut]

Category : Math > Graph theory and combinatorics
Formula  : The maximum flow from source to sink equals the capacity of the minimum cut

Status   : ready to use - call compute(graph, source, sink)
"""

NAME = 'Max flow min cut'
SYMBOL = 'max-flow = min-cut'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'The maximum flow from source to sink equals the capacity of the minimum cut'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph, source, sink):
    """Maximum flow from source to sink (Edmonds–Karp); the weights are capacities.  Equals the minimum cut"""
    cap = {}
    for u, nbrs in graph.items():
        for v, w in nbrs:
            cap.setdefault(u, {})[v] = cap.get(u, {}).get(v, 0) + w
            cap.setdefault(v, {}).setdefault(u, 0)
    flow = 0
    while True:
        prev, queue = {source: None}, [source]
        for u in queue:
            for v, c in cap.get(u, {}).items():
                if c > 1e-12 and v not in prev:
                    prev[v] = u
                    queue.append(v)
        if sink not in prev:
            return flow
        path, v = [], sink
        while prev[v] is not None:
            path.append((prev[v], v))
            v = prev[v]
        push = min(cap[u][v] for u, v in path)
        for u, v in path:
            cap[u][v] -= push
            cap[v][u] += push
        flow += push

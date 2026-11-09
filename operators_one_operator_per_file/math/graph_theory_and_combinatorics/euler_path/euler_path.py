"""Euler path   [Euler path]

Category : Math > Graph theory and combinatorics
Formula  : A path using every edge exactly once; exists iff the graph is connected with 0 or 2 odd-degree vertices

Status   : ready to use - call compute(graph)
"""

NAME = 'Euler path'
SYMBOL = 'Euler path'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A path using every edge exactly once; exists iff the graph is connected with 0 or 2 odd-degree vertices'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """True if a path can use every edge exactly once (connected, and 0 or 2 vertices of odd degree)"""
    adj = H.undirected(graph)
    nonempty = {v for v in adj if adj[v]}
    comps = [c for c in H.components(adj) if c & nonempty]
    odd = sum(1 for v in adj if len(adj[v]) % 2)
    return len(comps) <= 1 and odd in (0, 2)

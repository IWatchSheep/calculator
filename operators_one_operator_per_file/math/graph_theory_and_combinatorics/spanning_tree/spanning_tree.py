"""Spanning tree   [T ⊆ G]

Category : Math > Graph theory and combinatorics
Formula  : A tree that contains every vertex of G

Status   : ready to use - call compute(graph)
"""

NAME = 'Spanning tree'
SYMBOL = 'T ⊆ G'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A tree that contains every vertex of G'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """A minimum-weight spanning tree (Kruskal) → (edges, total weight)"""
    edges = sorted((w, u, v) for u, nbrs in graph.items() for v, w in nbrs)
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    out, total = [], 0
    for w, u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            out.append((u, v, w))
            total += w
    return out, total

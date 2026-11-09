"""Chromatic number   [χ(G)]

Category : Math > Graph theory and combinatorics
Formula  : The smallest number of colors needed to color vertices so adjacent vertices differ

Status   : ready to use - call compute(graph)
"""

NAME = 'Chromatic number'
SYMBOL = 'χ(G)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'The smallest number of colors needed to color vertices so adjacent vertices differ'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """The fewest colours needed so that joined vertices differ (exact search, up to 14 vertices)"""
    adj = H.undirected(graph)
    verts = sorted(adj, key=lambda v: -len(adj[v]))
    if len(verts) > 14:
        raise ValueError("too many vertices for the exact search (limit 14)")
    def ok(k):
        colour = {}
        def go(i):
            if i == len(verts):
                return True
            v = verts[i]
            for c in range(k):
                if all(colour.get(u) != c for u in adj[v]):
                    colour[v] = c
                    if go(i + 1):
                        return True
                    del colour[v]
            return False
        return go(0)
    k = 1
    while not ok(k):
        k += 1
    return k

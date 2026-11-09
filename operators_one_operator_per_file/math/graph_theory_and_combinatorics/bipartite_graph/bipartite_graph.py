"""Bipartite graph   [bipartite]

Category : Math > Graph theory and combinatorics
Formula  : Vertices split into two sets with edges only between the sets (no odd cycles)

Status   : ready to use - call compute(graph)
"""

NAME = 'Bipartite graph'
SYMBOL = 'bipartite'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'Vertices split into two sets with edges only between the sets (no odd cycles)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """True if the vertices can be split into two sets with edges only between them (2-colourable)"""
    adj = H.undirected(graph)
    colour = {}
    for s in adj:
        if s in colour:
            continue
        colour[s] = 0
        stack = [s]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in colour:
                    colour[v] = 1 - colour[u]
                    stack.append(v)
                elif colour[v] == colour[u]:
                    return False
    return True

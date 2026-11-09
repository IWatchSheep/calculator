"""Hamiltonian path   [Hamilton path]

Category : Math > Graph theory and combinatorics
Formula  : A path visiting every vertex exactly once

Status   : ready to use - call compute(graph)
"""

NAME = 'Hamiltonian path'
SYMBOL = 'Hamilton path'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A path visiting every vertex exactly once'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """A path visiting every vertex exactly once, as a list (or False if none); up to 10 vertices"""
    adj = H.undirected(graph)
    if len(adj) > 10:
        raise ValueError("too many vertices for the exact search (limit 10)")
    def go(path):
        if len(path) == len(adj):
            return path
        for v in adj[path[-1]]:
            if v not in path:
                found = go(path + [v])
                if found:
                    return found
        return None
    for s in adj:
        found = go([s])
        if found:
            return found
    return False

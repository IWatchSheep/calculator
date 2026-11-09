"""Cycle   [cycle]

Category : Math > Graph theory and combinatorics
Formula  : A path that returns to its starting vertex

Status   : ready to use - call compute(graph)
"""

NAME = 'Cycle'
SYMBOL = 'cycle'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A path that returns to its starting vertex'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """True if the graph contains a cycle (a path that returns to its start)"""
    adj = H.undirected(graph)
    return H.edge_count(adj) > len(adj) - len(H.components(adj))

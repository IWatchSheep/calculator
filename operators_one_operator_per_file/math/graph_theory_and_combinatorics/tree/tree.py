"""Tree   [tree]

Category : Math > Graph theory and combinatorics
Formula  : A connected graph with no cycles; a tree on n vertices has n − 1 edges

Status   : ready to use - call compute(graph)
"""

NAME = 'Tree'
SYMBOL = 'tree'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A connected graph with no cycles; a tree on n vertices has n − 1 edges'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """True if the graph is connected with no cycles (a tree on n vertices has n − 1 edges)"""
    adj = H.undirected(graph)
    return len(H.components(adj)) == 1 and H.edge_count(adj) == len(adj) - 1

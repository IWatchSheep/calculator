"""Graph   [G = (V, E)]

Category : Math > Graph theory and combinatorics
Formula  : A set of vertices V and a set of edges E joining pairs of vertices

Status   : ready to use - call compute(graph)
"""

NAME = 'Graph'
SYMBOL = 'G = (V, E)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A set of vertices V and a set of edges E joining pairs of vertices'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """(number of vertices, number of edges) of a graph given as vertex: neighbours"""
    adj = H.undirected(graph)
    return len(adj), H.edge_count(adj)

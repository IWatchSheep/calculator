"""Planar graph   [planar]

Category : Math > Graph theory and combinatorics
Formula  : Can be drawn in the plane without crossing edges; then E ≤ 3V − 6 (V ≥ 3)

Status   : ready to use - call compute(graph)
"""

NAME = 'Planar graph'
SYMBOL = 'planar'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'Can be drawn in the plane without crossing edges; then E ≤ 3V − 6 (V ≥ 3)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(graph):
    """Edge-count test for planarity: E ≤ 3V − 6 (V ≥ 3).  False means NOT planar; True means it passes this test"""
    adj = H.undirected(graph)
    V, E = len(adj), H.edge_count(adj)
    return V < 3 or E <= 3 * V - 6

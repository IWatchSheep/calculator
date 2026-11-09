"""Adjacency matrix   [A]

Category : Math > Graph theory and combinatorics
Formula  : Aᵢⱼ = 1 if vertices i and j are joined (undirected), else 0

Status   : ready to use - call compute(n, edges)
"""

NAME = 'Adjacency matrix'
SYMBOL = 'A'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'Aᵢⱼ = 1 if vertices i and j are joined (undirected), else 0'


def compute(n, edges):
    """Aᵢⱼ = 1 if vertices i and j are joined (undirected), else 0"""
    return [[1 if (i, j) in edges or (j, i) in edges else 0 for j in range(n)] for i in range(n)]

"""Vertex degree   [deg(v)]

Category : Math > Graph theory and combinatorics
Formula  : deg(v) = number of edges at v   (graph = {vertex: [neighbors]})

Status   : ready to use - call compute(graph, v)
"""

NAME = 'Vertex degree'
SYMBOL = 'deg(v)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'deg(v) = number of edges at v   (graph = {vertex: [neighbors]})'


def compute(graph, v):
    """deg(v) = number of edges at v   (graph = {vertex: [neighbors]})"""
    return len(graph[v])

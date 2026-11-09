"""Shortest path (Dijkstra)   [d(u, v)]

Category : Math > Graph theory and combinatorics
Formula  : Dijkstra's algorithm; graph = {node: [(neighbor, weight), …]}, returns {node: distance}

Status   : ready to use - call compute(graph, start)
"""
import math, heapq

NAME = 'Shortest path (Dijkstra)'
SYMBOL = 'd(u, v)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = "Dijkstra's algorithm; graph = {node: [(neighbor, weight), …]}, returns {node: distance}"


def compute(graph, start):
    """Dijkstra's algorithm; graph = {node: [(neighbor, weight), …]}, returns {node: distance}"""
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, math.inf):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

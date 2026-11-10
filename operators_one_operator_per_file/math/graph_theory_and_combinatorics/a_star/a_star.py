"""Shortest path (A*)   [A*]

Category : Math > Graph theory and combinatorics
Formula  : A* on the Dijkstra graph with node positions; straight-line distance to the goal; returns the path of nodes

Status   : ready to use - call compute(graph, positions, start, goal)
"""

NAME = 'Shortest path (A*)'
SYMBOL = 'A*'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'A* on the Dijkstra graph with node positions; straight-line distance to the goal; returns the path of nodes'
import math, heapq


def compute(graph, positions, start, goal):
    """A*: the path of nodes from start to goal (graph = {node: [(neighbor, weight), …]}, positions = {node: [x, y]})"""
    for edges in graph.values():
        for _node, w in edges:
            if w < 0:
                raise ValueError("a weight cannot be negative")

    def where(node):
        p = positions.get(node)
        if p is None or len(p) != 2:
            raise ValueError("each node needs a position")
        return p

    gx, gy = where(goal)

    def heuristic(node):
        x, y = where(node)
        return math.sqrt((gx - x) * (gx - x) + (gy - y) * (gy - y))

    cost = {start: 0}
    came = {}
    count = 0
    heap = [(heuristic(start), count, start)]
    while heap:
        f, _count, u = heapq.heappop(heap)
        if f > cost[u] + heuristic(u):
            continue
        if u == goal:
            path = [u]
            while path[-1] in came:
                path.append(came[path[-1]])
            return path[::-1]
        for v, w in graph.get(u, []):
            g = cost[u] + w
            if g < cost.get(v, math.inf):
                cost[v] = g
                came[v] = u
                count += 1
                heapq.heappush(heap, (g + heuristic(v), count, v))
    raise ValueError("no path")

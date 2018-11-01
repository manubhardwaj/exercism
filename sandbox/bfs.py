#!/usr/bin/env python3

def bfs(graph, start):
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited


if __name__ == '__main__':
    graph = {
            'A': set(['B','C']),
            'B': set(['D','E']),
            'C': set(['F','G']),
            'D': set(['H','I']),
            'E': set(['B']),
            'F': set(['C']),
            'G': set(['C']),
            'H': set(['D']),
            'I': set(['D'])
    }
    print(bfs(graph,'A'))

from sys import stdin
from collections import deque
input = stdin.readline
# for n in [int(num) for num in stdin.read().split()]:
"""
-------------------------------------------------------
INPUT
N: 정점(node)의 개수
M: 간선(edge)의 개수 (간선은 양방향)
V: 탐색을 시작할 정점의 번호

OUTPUT
DFS 의 결과
BFS 의 결과
-------------------------------------------------------
"""


class Graph:
    def __init__(self):
        self.edges = dict()

    def add_edge(self, from_node, to_node):
        self._add_edge(from_node, to_node)
        self._add_edge(to_node, from_node)

    def _add_edge(self, from_node, to_node):
        self.edges.setdefault(from_node, set())
        self.edges[from_node].add(to_node)


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        cur = stack.pop()

        if cur not in visited:
            visited.append(cur)
            stack += sorted(list(graph.edges[cur] - set(visited)), reverse=True)

    return visited


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        cur = queue.popleft()

        if cur not in visited:
            visited.append(cur)
            queue += sorted(list(graph.edges[cur] - set(visited)))

    return visited


N, M, V = map(int, input().split())
my_graph = Graph()
for _ in range(M):
    fr, to = map(int, input().split())
    my_graph.add_edge(fr, to)

print(*dfs(my_graph, V))
print(*bfs(my_graph, V))
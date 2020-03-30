from sys import stdin
from collections import deque
input = stdin.readline


def bfs(start):
    visited = [start]
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for search in range(len(adj_matrix[current])):
            if adj_matrix[current][search] and search not in visited:
                visited.append(search)
                queue.append(search)

    return len(visited) - 1


node = int(input())
edge = int(input())
adj_matrix = [[False]*(node+1) for _ in range(node+1)]

for _ in range(edge):
    comp_1, comp_2 = [int(c) for c in input().split()]
    adj_matrix[comp_1][comp_2] = True
    adj_matrix[comp_2][comp_1] = True

print(bfs(1))
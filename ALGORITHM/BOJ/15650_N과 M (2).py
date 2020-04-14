# 패키지를 활용한 풀이
"""
from itertools import permutations

N, M = map(int, input().split())
visited = []

for p in permutations(range(1, N+1), M):
    if tuple(sorted(p)) not in visited:
        visited.append(p)

for v in visited:
    print(*v)
"""

# DFS 방식 구현

N, M = map(int, input().split())
visited = [False] * (N+1)
permutation = []


def DFS(depth):

    if depth == M:
        print(*permutation)
        return

    for idx in range(1, N + 1):
        if visited[idx]:
            continue

        visited[idx] = True
        permutation.append(idx)

        DFS(depth + 1)

        permutation.pop()

        for i in range(idx + 1, N + 1):
            visited[i] = False


DFS(0)
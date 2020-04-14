# itertools 패키지를 통해 쉽게 답을 구할 수 있다

"""
from itertools import permutations

N, M = map(int, input().split())

for p in permutations(range(1, N+1), M):
    print(*p)
"""

# DFS 방식으로 구현

N, M = map(int, input().split())
visited = [False] * (N+1)
permutation = []


def DFS(depth):
    if depth == M:
        print(*permutation)
        return

    for idx in range(1, N+1):
        if not visited[idx]:
            permutation.append(idx)
            visited[idx] = True

            DFS(depth + 1)

            permutation.pop()
            visited[idx] = False


DFS(0)
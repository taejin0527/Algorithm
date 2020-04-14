N, M = map(int, input().split())
visited = [False] * (N + 1)
permutation = []


def DFS(depth, pre):
    if depth == M:
        print(*permutation)
        return

    for idx in range(1, N+1):
        if idx >= pre:
            permutation.append(idx)
            DFS(depth + 1, idx)
            permutation.pop()


DFS(0, 1)
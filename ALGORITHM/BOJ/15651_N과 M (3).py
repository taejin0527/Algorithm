N, M = map(int, input().split())
permutation = []


def DFS(depth):
    if depth == M:
        print(*permutation)
        return

    for idx in range(1, N+1):
        permutation.append(idx)
        DFS(depth + 1)
        permutation.pop()


DFS(0)
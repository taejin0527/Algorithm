N, M = map(int, input().split())
P = [int(n) for n in input().split()]
P.sort()
visited = [False] * (N + 1)
permutation = []


def DFS(depth):
    if depth == M:
        print(*permutation)
        return

    for idx in range(N):
        permutation.append(P[idx])
        DFS(depth + 1)
        permutation.pop()


DFS(0)
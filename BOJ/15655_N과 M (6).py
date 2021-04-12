N, M = map(int, input().split())
P = [int(n) for n in input().split()]
P.sort()
visited = [False] * (N + 1)
permutation = []


def DFS(depth, pre):
    if depth == M:
        print(*permutation)
        return

    for idx in range(N):
        if not visited[idx] and pre <= P[idx]:
            visited[idx] = True
            permutation.append(P[idx])

            DFS(depth + 1, P[idx])

            visited[idx] = False
            permutation.pop()


DFS(0, P[0])
from sys import stdin

N, M = map(int, stdin.readline().split())
P = sorted([int(n) for n in stdin.readline().split()])
perm, v = [], [False] * N
check = set()


def dfs(depth):
    if depth == M:
        t = tuple(perm)

        if t not in check:
            check.add(t)
            print(*perm)
        return

    for i in range(N):
        if not v[i]:
            v[i] = True
            perm.append(P[i])
            dfs(depth+1)
            perm.pop()
            v[i] = False


dfs(0)

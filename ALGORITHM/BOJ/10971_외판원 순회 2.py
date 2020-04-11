from collections import defaultdict


def travel(now, depth):
    global charge, ans

    if depth == N:
        if path[now][0] > 0:
            ans = min(ans, charge + path[now][0])
            return

    visit[now] = 1

    for l in link[now]:
        if not visit[l]:
            charge += path[now][l]
            travel(l, depth+1)
            charge -= path[now][l]

    visit[now] = 0


N = int(input())
path = [[int(n) for n in input().split()] for _ in range(N)]
visit = [0] * N
link = defaultdict(list)
charge, ans = 0, float('inf')

for i in range(N):
    for j in range(N):
        if path[i][j]:
            link[i].append(j)

travel(0, 1)
print(ans)
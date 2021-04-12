from collections import deque
from sys import stdin

input = stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = []
v = [False] * (N+1)

q = deque()
q.append((X, 0))

while q:
    cur, step = q.popleft()
    if step == K:
        ans.append(cur)
    elif step < K:
        for nxt in graph[cur]:
            if not v[nxt]:
                v[nxt] = True
                q.append((nxt, step+1))

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    print(*ans, sep='\n')


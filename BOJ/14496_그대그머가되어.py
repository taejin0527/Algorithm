from collections import deque
from sys import stdin
input = stdin.readline
"""
@params
a, b            바꾸려하는 문자 a, b
N, M            전체 문자의 수, 치환 가능한 문자쌍의 수
[list]          치환 가능한 문자쌍

@return
answer          최소 치환 횟수(불가능하면 -1)
"""

a, b = map(int, input().split())
N, M = map(int, input().split())
pair = [[] for _ in range(N+1)]
for _ in range(M):
    n, m = map(int, input().split())
    pair[n].append(m)
    pair[m].append(n)

dist = [-1] * (N+1)
dist[a] = 0
q = deque([a])

while q:
    cur = q.popleft()

    for nxt in pair[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

print(dist[b])
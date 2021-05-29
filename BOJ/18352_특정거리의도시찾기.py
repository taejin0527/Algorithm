from collections import deque
from sys import stdin
input = stdin.readline

"""
@parmas
N           도시의 개수
M           도로의 개수
K           거리 정보
X           출발 도시의 번호
[A, B]      A 도시에서 B 도시로 이동하는 도로 존재

@return
answer      X로부터 출발하여 도달할 수 있는 도시 중, 최단 거리가 K인 도시의 번호(오름차순), 없으면 -1
"""

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    
dist = [-1] * (N+1)
dist[X] = 0
q = deque([X])

while q:
    cur = q.popleft()
    
    for nxt in graph[cur]:
        if dist[nxt] >= 0:
            continue
        dist[nxt] = dist[cur] + 1
        q.append(nxt)

answer = []
for idx, d in enumerate(dist):
    if d == K:
        answer.append(idx)

if len(answer):
    print(*answer, sep="\n")
else:
    print(-1)
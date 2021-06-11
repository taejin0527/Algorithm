"""
@params
n, m                집하장의 개수, 집하장간 경로의 개수
[u, v, w]           두 집하장의 번호와 그 사이를 오가는데 필요한 시간

@return
[answer]             경로표
"""

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append(([u, w]))

answer = [['-'] * n for _ in range(n)]
dist = [int(1e9)] * n
dist[0] = 0

for i in range(n):


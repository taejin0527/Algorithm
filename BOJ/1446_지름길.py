"""
@params
N, D            지름길의 개수, 고속도로의 길이
[list]          지름길의 시작위치, 도착위치, 길이

@return
answer          운전해야하는 거리의 최솟값
"""

N, D = map(int, input().split())
graph = {i: [(i+1, 1)] for i in range(D)}
graph[D] = []   # 도착위치

for _ in range(N):
    u, v, w = map(int, input().split())
    if v <= D:
        graph[u].append((v, w))

INF = int(1e9)
dp = [i for i in range(D+1)]

for cur in range(D+1):
    for nxt, w in graph[cur]:
        dp[nxt] = min(dp[nxt], dp[cur]+w)
        
print(dp[-1])
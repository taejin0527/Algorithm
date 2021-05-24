import heapq
import sys
input = sys.stdin.readline

"""
@params
T                      테스트 게이스의 개수
n, d, c                컴퓨터 개수, 의존성 개수, 해킹단한 컴퓨터의 번호
[list]                 의존성 (a가 b를 의존하며, b가 감염되면 s초 후 a도 감염)

@return
cnt, infection_time    총 감염되는 컴퓨터 수, 걸리는 시간
"""
INF = int(1e9)
    
def dijkstra(graph, start):
    q = []
    time = [INF] * len(graph)
    time[start] = 0
    heapq.heappush(q, (start, 0))
    
    while q:
        cur, ct = heapq.heappop(q)

        for nxt, nt in graph[cur]:
            if time[nxt] > ct + nt:
                time[nxt] = ct + nt
                heapq.heappush(q, (nxt, ct + nt))

    return time
    
    

for T in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
        
    time = dijkstra(graph, c)
    time = list(filter(lambda x: x != INF, time))
    
    cnt, infection_time = 0, 0
    
    for t in time:
        if time == INF:
            continue
        if infection_time < t:
            infection_time = t
        cnt += 1
    
    print(cnt, infection_time)
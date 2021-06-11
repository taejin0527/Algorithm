"""
 * @FileName : basic_dijkstra.py
 * @Book
 * @Date : 2021-05-30
 * @author : AoN
 * @Description : O(V^2)
 * 
"""

from sys import stdin
input = stdin.readline

INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드 정보
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)       # 방문 체크
distance = [INF] * (n+1)        # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않는 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for b, c in distance[start]:
        distance[b] = c
        

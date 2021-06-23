"""
@params
N               트리 노드의 개수
[node * N]      부모 노드의 번호
R               지울 노드의 번호

@return
answer          남은 리프 노드의 개수
"""
import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
R = int(input())

def dfs(num, arr):
    graph[num] = -2

    for i in range(N):
        if num == graph[i]:
            dfs(i, graph)

dfs(R, graph)

answer = 0
for i in range(N):
    if graph[i] != -2 and i not in graph:
        answer += 1
print(answer)
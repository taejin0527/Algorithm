"""
@params
N                       섬의 개수
[t, a, p] * (N-1)       t: 양/늑대, a: 마리 수, p: 다리 유무

@return
answer                  구출할 수 있는 양의 수
"""
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N = int(input())
graph = [[0, []] for _ in range(N + 1)]

for i in range(2, N + 1):
    t, a, p = map(lambda x: int(x) if x.isdigit() else x, input().split())

    if t == "W":
        a = -a

    graph[i][0] = a
    graph[p][1].append(i)


def dfs(depth):
    # 늑대 or 양 마리 수 저장 및 갱신
    answer = graph[depth][0]
    for g in graph[depth][1]:
        answer += dfs(g)

    # 섬을 이동할 때 섬에 늑대만 있거나 양보다 늑대가 많아서 양을 다 잡아 먹을 때
    if answer < 0:
        return 0
    else:
        return answer


print(dfs(1))

from collections import defaultdict


def dfs(start, depth):
    global state
    visited[start] = True

    if depth == 4:
        state = True
        return

    for next_node in my_graph[start]:
        if not visited[next_node]:
            dfs(next_node, depth + 1)
            visited[next_node] = False

    return visited


N, M = [int(n) for n in input().split()]
my_graph = defaultdict(list)
for _ in range(M):
    a, b = [int(n) for n in input().split()]
    my_graph[a].append(b)
    my_graph[b].append(a)

visited = [False] * N
state = False
for s in my_graph.keys():
    dfs(s, 0)
    visited[s] = False
    if state:
        break

print(1 if state else 0)

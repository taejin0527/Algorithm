import sys
sys.setrecursionlimit(10000)


def dfs(node):
    visited[node] = True

    for next_node in my_graph[node]:
        if not visited[next_node]:
            dfs(next_node)


nodes, edges = [int(n) for n in sys.stdin.readline().split()]
my_graph = [[] for _ in range(nodes+1)]
for _ in range(edges):
    u, v = [int(n) for n in sys.stdin.readline().split()]
    my_graph[u].add(v)
    my_graph[v].add(u)

visited = [False] * (nodes+1)
components = 0
for start in range(1, nodes+1):
    if not visited[start]:
        dfs(start)
        components += 1

print(components)

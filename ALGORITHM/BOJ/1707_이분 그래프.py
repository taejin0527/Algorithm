
        for next_node in my_graph[current]:
            if colored[next_node] == 0:
                colored[next_node] = -1 * colored[current]
                queue.append(next_node)
            elif colored[next_node] == colored[current]:
                return 1
    return 0


K = int(input())

for _ in range(K):
    V, E = [int(n) for n in input().split()]
    my_graph = [[] for _ in range(V)]
    for _ in range(E):
        vertex, edge = [int(n) for n in input().split()]
        my_graph[vertex - 1].append(edge - 1)
        my_graph[edge - 1].append(vertex - 1)

    colored = [0] * V       # 0:not visited 1: Red -1: Black
    ans = 0
    for i in range(V):
        if colored[i] == 0:
            ans = bfs(i)
            if ans:
                break
    print("NO" if ans else "YES")
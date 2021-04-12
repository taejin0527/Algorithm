from sys import stdin
input = stdin.readline
"""
-------------------------------------------------------
INPUT
N: 정점(node)의 개수
M: 간선(edge)의 개수 (간선은 양방향)
V: 탐색을 시작할 정점의 번호

OUTPUT
DFS 의 결과
BFS 의 결과
-------------------------------------------------------
"""
def dfs(matrix, current_node, visited):
    visited += [current_node]

    for next_node in range(len(matrix[current_node])):
        if matrix[current_node][next_node] and next_node not in visited:
            visited = dfs(matrix, next_node, visited)

    return visited


def bfs(matrix, start_node):
    visited = [start_node]
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        for next_node in range(len(matrix[current_node])):
            if matrix[current_node][next_node] and next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)

    return visited

N, M, V = [int(n) for n in input().split()]
adj_matrix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    from_node, to_node = [int(num) for num in input().split()]
    adj_matrix[from_node][to_node] = 1
    adj_matrix[to_node][from_node] = 1

print(*dfs(adj_matrix, V, []))
print(*bfs(adj_matrix, V))

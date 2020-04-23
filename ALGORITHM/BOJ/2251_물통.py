from collections import deque

A, B, C = map(int, input().split())


def bfs():
    queue = deque()
    queue.append((0, 0, C))
    visited = []

    while queue:
        a, b, c = queue.popleft()

        if c not in visited:
            visited.append(c)
            if A < C:
                queue.append((A, 0, c - A))
            else:
                queue.append((c, 0, 0))

            if B < C:
                queue.append((0, B, c - B))
            else:
                queue.append((0, c, 0))
        print(queue)


bfs()
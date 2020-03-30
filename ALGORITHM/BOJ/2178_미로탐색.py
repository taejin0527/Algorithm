from collections import deque


def bfs():
    _dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == (N-1, M-1):
            return visited[x][y]

        for i in range(4):
            next_x = x + _dir[i][0]
            next_y = y + _dir[i][1]

            if 0 <= next_x < N and 0 <= next_y < M:
                if visited[next_x][next_y] == 0 and maze[next_x][next_y] == 1:
                    visited[next_x][next_y] = visited[x][y] + 1
                    queue.append((next_x, next_y))


N, M = [int(n) for n in input().split()]
maze = [[] for _ in range(N)]

for i in range(N):
    maze[i].extend([int(num) for num in input()])

print(bfs() + 1)

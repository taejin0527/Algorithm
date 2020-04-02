from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def bfs():
    queue = deque()
    queue.append((0, 0))
    AOJ[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M:
                if not maze[next_x][next_y] and AOJ[next_x][next_y] == -1:
                    queue.appendleft((next_x, next_y))
                    AOJ[next_x][next_y] = AOJ[x][y]
                elif maze[next_x][next_y] and AOJ[next_x][next_y] == -1:
                    queue.append((next_x, next_y))
                    AOJ[next_x][next_y] = AOJ[x][y] + 1

    return AOJ[N-1][M-1]


M, N = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
AOJ = [[-1] * M for _ in range(N)]

print(bfs())
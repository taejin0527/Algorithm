"""
조건 : 벽을 한 개 까지 부수고 이동하여도 된다
"""
from collections import deque


def bfs():
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    queue = deque()

    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        x, y, c = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[c][x][y]

        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and not visited[c][next_x][next_y]:
                if not board[next_x][next_y]:
                    visited[c][next_x][next_y] = visited[c][x][y] + 1
                    queue.append((next_x, next_y, c))
                elif board[next_x][next_y] and not c:
                    visited[1][next_x][next_y] = visited[c][x][y] + 1
                    queue.append((next_x, next_y, 1))
    return -1


MAX = 1000
N, M = map(int, input().split())
board = [[int(n) for n in input()] for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

print(bfs())
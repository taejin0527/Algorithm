from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j))

    days = -1
    while queue:
        days += 1
        length = len(queue)

        for _ in range(length):
            x, y = queue.popleft()

            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if 0 <= next_x < N and 0 <= next_y < M and box[next_x][next_y] == 0:
                    box[next_x][next_y] = 1
                    queue.append((next_x, next_y))

    for b in box:
        if 0 in b:
            return -1

    return days


M, N = [int(n) for n in input().split()]
box = [[int(n) for n in input().split()] for _ in range(N)]

print(bfs())
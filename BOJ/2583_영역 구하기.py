M, N, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
areas = []

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())

    for y in range(ly, ry):
        for x in range(lx, rx):
            board[y][x] = 1

# bfs
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            area, board[i][j] = 1, 1
            queue = [[i, j]]

            while queue:
                x, y = queue.pop()
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                        board[nx][ny] = 1
                        area += 1
                        queue.append([nx, ny])

            areas.append(area)

areas.sort()
print(len(areas))
print(*areas, sep=' ')
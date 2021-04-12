N = int(input())
areas = [list(input()) for _ in range(N)]

ans1, ans2 = 0, 0


def bfs(a, b, color):
    queue = [(a, b)]

    while queue:
        x, y = queue.pop()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny] and areas[nx][ny] in color:
                v[nx][ny] = True
                queue.append((nx, ny))


# BFS
v = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            v[i][j] = True
            ans1 += 1
            bfs(i, j, areas[i][j])


v = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            v[i][j] = True
            ans2 += 1
            if areas[i][j] == 'R' or areas[i][j] == 'G':
                bfs(i, j, ['R', 'G'])
            else:
                bfs(i, j, ['B'])

print(ans1, ans2)

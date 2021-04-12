from sys import stdin


def dp(x: int, y: int):
    if v[x][y] > 0:
        return

    v[x][y] = 0
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and my_map[nx][ny] > my_map[x][y]:
            if v[nx][ny] < 0:
                dp(nx, ny)
            v[x][y] += v[nx][ny]


N, M = map(int, stdin.readline().split())
my_map = [list(map(int, stdin.readline().split())) for _ in range(N)]
v = [[-1] * M for _ in range(N)]

v[0][0] = 1
for i in range(N):
    for j in range(M):
        dp(i, j)

print(v[-1][-1])

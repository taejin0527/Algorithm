from collections import deque


N, M = map(int, input().split())
lab = [[int(n) for n in input().split()] for _ in range(N)]
virus = deque()
safe, infected = 0, N*M


def find_virus():
    global safe, virus

    for i in range(N):
        for j in range(M):
            if lab[i][j] != 1:
                safe += 1
            if lab[i][j] == 2:
                virus.append((i, j))


def scenario(wall, x, y):
    global infected

    if wall == 3:
        cnt = 0
        visited_lab = [[False]*M for _ in range(N)]

        for i, j in virus:
            cnt += dfs(i, j, visited_lab)

        infected = min(infected, cnt + 3)
        return

    for nx in range(x, N):
        k = y if nx == x else 0

        for ny in range(k, M):
            if lab[nx][ny] == 0:
                lab[nx][ny] = 1
                scenario(wall+1, nx, ny+1)
                lab[nx][ny] = 0


def dfs(x, y, visited):
    res = 1
    visited[x][y] = True
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M and\
                not (visited[nx][ny] or lab[nx][ny]):
            res += dfs(nx, ny, visited)

    return res


find_virus()
scenario(0, 0, 0)
print(safe - infected)
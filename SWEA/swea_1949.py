from sys import stdin

input = stdin.readline


def dfs(x, y, flag):
    global ans

    if ans < v[x][y]:
        ans = v[x][y]

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if v[nx][ny] > 0: continue

        if my_map[nx][ny] < my_map[x][y]:
            v[nx][ny] = v[x][y] + 1
            dfs(nx, ny, flag)
            v[nx][ny] = 0
        elif my_map[nx][ny] >= my_map[x][y] and not flag:
            for d in range(1, K+1):
                my_map[nx][ny] -= d
                if my_map[nx][ny] < my_map[x][y]:
                    v[nx][ny] = v[x][y] + 1
                    dfs(nx, ny, True)
                    v[nx][ny] = 0
                my_map[nx][ny] += d


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    peek = max(map(max, my_map))

    ans = 0
    for i in range(N):
        for j in range(N):
            if my_map[i][j] == peek:
                v = [[0]*N for _ in range(N)]
                v[i][j] = 1
                dfs(i, j, False)

    print('#{} {}'.format(tc, ans))
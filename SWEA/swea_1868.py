from collections import deque

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    v[x][y] = True

    while dq:
        cx, cy = dq.popleft()

        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
                v[nx][ny] = True
                if my_map[nx][ny] == 0:
                    dq.append((nx, ny))


def find_mine(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if my_map[nx][ny] == '*':
            return 1

    return 0


for tc in range(1, int(input())+1):
    N = int(input())
    my_map = [list(input()) for _ in range(N)]
    zero_list = []

    for i in range(N):
        for j in range(N):
            if my_map[i][j] == '.':
                my_map[i][j] = find_mine(i, j)
            if my_map[i][j] == 0:
                zero_list.append((i, j))

    click = 0
    v = [[False] * N for _ in range(N)]

    for r, c in zero_list:
        if v[r][c]:
            continue
        bfs(r, c)
        click += 1

    for i in range(N):
        for j in range(N):
            if not v[i][j] and my_map[i][j] != '*':
                click += 1

    print('#{} {}'.format(tc, click))

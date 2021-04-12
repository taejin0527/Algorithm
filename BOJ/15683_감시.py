N, M = map(int, input().split())
office = [[int(n) for n in input().split()] for _ in range(N)]


def init():
    global empty, cctv
    U, R, D, L = 0, 1, 2, 3

    for i in range(N):
        for j in range(M):
            cur = office[i][j]
            if cur == 0:
                empty += 1
            elif cur == 1:
                cctv.append([watch(i, j, [U]), watch(i, j, [R]), watch(i, j, [D]), watch(i, j, [L])])
            elif cur == 2:
                cctv.append([watch(i, j, [U, D]), watch(i, j, [R, L])])
            elif cur == 3:
                cctv.append([watch(i, j, [U, R]), watch(i, j, [R, D]), watch(i, j, [D, L]), watch(i, j, [L, U])])
            elif cur == 4:
                cctv.append([watch(i, j, [U, R, D]), watch(i, j, [R, D, L]), watch(i, j, [D, L, U]), watch(i, j, [L, U, R])])
            elif cur == 5:
                cctv.append([watch(i, j, [U, R, D, L])])


def watch(_x, _y, _dir):            # (x, y) : cctv 위치, dir : 감시 방향
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    my_set = set()

    for d in _dir:
        nx, ny = _x, _y
        while True:
            nx, ny = nx + dx[d], ny + dy[d]

            if not (0 <= nx < N and 0 <= ny < M):
                break
            if office[nx][ny] == 6:
                break
            if office[nx][ny] == 0:
                my_set.add((nx, ny))

    return my_set


def dfs(n, union_set):
    global max_cctv

    if n == len(cctv):
        max_cctv = max(max_cctv, len(union_set))
        return

    for i in cctv[n]:
        dfs(n+1, union_set|i)


max_cctv, cctv = 0, []
empty = 0

init()
dfs(0, set())
print(empty - max_cctv)
from collections import deque


def explode(x, y, cur_grid):
    q = deque([[x, y, cur_grid[x][y]]])
    cur_grid[x][y] = 0
    res = 1

    while q:
        cx, cy, cp = q.popleft()

        for p in range(1, cp):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + p * dx, cy + p * dy

                if not (0 <= nx < H and 0 <= ny < W):
                    continue
                if cur_grid[nx][ny] != 0:
                    if cur_grid[nx][ny] != 1:
                        q.append([nx, ny, cur_grid[nx][ny]])
                    res += 1
                    cur_grid[nx][ny] = 0

    return res


def fallDown(cur_grid):
    for y in range(W):
        prev = H - 1
        for x in range(H-1, -1, -1):
            if cur_grid[x][y]:
                if prev != x:
                    cur_grid[prev][y], cur_grid[x][y] = cur_grid[x][y], cur_grid[prev][y]
                prev -= 1


def dfs(depth, cnt, cur_grid):
    global max_cnt
    if depth == N:
        max_cnt = max(max_cnt, cnt)
        return

    for w in range(W):
        copy_grid = [row[:] for row in cur_grid]
        ch = 0

        while ch < H and not cur_grid[ch][w]:
            ch += 1

        bombed = 0
        if ch < H:
            bombed = explode(ch, w, copy_grid)
            fallDown(copy_grid)

        dfs(depth+1, cnt + bombed, copy_grid)


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    total_bricks = 0
    for x in range(H):
        for y in range(W):
            if grid[x][y]:
                total_bricks += 1

    max_cnt = 0
    dfs(0, 0, grid)

    print('#{} {}'.format(tc+1, total_bricks - max_cnt))

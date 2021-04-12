N, M = [int(n) for n in input().split()]
r, c, d = [int(n) for n in input().split()]
MAP = [[int(n) for n in input().split()] for _ in range(N)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)   # (N, E, S, W) = (0, 1, 2, 3)
MAP[r][c] = 2                           # 빈칸: 0, 벽: 1, 로봇 청소: 2


def cleaning(x, y, d):
    cleaned = 1

    while True:
        moved = False

        for _ in range(4):              # 4방향 탐색
            left = (d + 3) % 4
            nxt_x, nxt_y, d = x + dx[left], y + dy[left], left

            if not MAP[nxt_x][nxt_y]:   # 벽(1)이나 청소(2)된 곳이 아니면,
                moved = True
                MAP[nxt_x][nxt_y] = 2   # 청소(2)
                cleaned += 1
                x, y = nxt_x, nxt_y
                break

        if not moved:                   # 4방향으로 이동이 불가능하고,
            pre_x, pre_y = x - dx[d], y - dy[d]

            if MAP[pre_x][pre_y] == 1:  # 후진시 벽이라면
                return cleaned          # 작동 종료
            else:                       # 아니면
                x, y = pre_x, pre_y     # 후진


print(cleaning(r, c, d))
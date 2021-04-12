N, M, x, y, K = [int(n) for n in input().split()]
MAP = [[int(n) for n in input().split()] for _ in range(N)]
commands = [int(n) for n in input().split()]

dice, pre_dice = [0] * 6, [0] * 6
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)   # (E, W, N, S) = (1, 2, 3, 4)
direction = [
    (2, 0, 5, 3, 4, 1),  # E
    (1, 5, 0, 3, 4, 2),  # W
    (4, 1, 2, 0, 5, 3),  # N
    (3, 1, 2, 5, 0, 4),  # S
]

for cmd in commands:
    x, y = x + dx[cmd - 1], y + dy[cmd - 1]
    if 0 <= x < N and 0 <= y < M:
        for i in range(6):
            pre_dice[i] = dice[i]

        for i in range(6):       # 방향 회전에 따른 주사위값 저장
            dice[i] = pre_dice[direction[cmd-1][i]]

        if MAP[x][y]:            # 지도의 칸에 값이 있다면,
            dice[5] = MAP[x][y]  # 바닥면에 칸의 값을 넣고
            MAP[x][y] = 0        # 칸은 0으로 업데이트
        else:
            MAP[x][y] = dice[5]  # 칸 이 0이라면, 주사위의 값을 복사
        print(dice[0])           # 주사위의 바닥면을 출력
    else:
        x, y = x - dx[cmd - 1], y - dy[cmd - 1]

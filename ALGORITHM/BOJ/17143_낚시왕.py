R, C, M = map(int, input().split())                     # (R, C): 격자판 크기, M: 상어의 수
ocean = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())           # (r, c): 상어의 위치, s: 속력, d: 이동방향, z: 크기
    ocean[r-1][c-1] = [s, d, z]
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)                   # 위, 아래, 오른쪽, 왼쪽 순서


def catch_shark():
    global total_shark_size

    for row in range(R):                                  # 행을 따라 내려가며
        if ocean[row][fish_king]:                         # 상어가 있으면
            _s, _d, _size = ocean[row][fish_king]
            total_shark_size += _size                     # 상어의 크기를 기록
            ocean[row][fish_king] = []                    # 잡은 상어는 바다에서 제거
            break


def shark_move():
    global ocean
    nxt_ocean = [[[] for _ in range(C)] for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if ocean[row][col]:                             # 이동할 상어가 있으면
                _speed, _dir, _size = ocean[row][col]
                cx, cy = row, col

                if _dir == 1 or _dir == 2:
                    for _ in range(_speed % (R * 2 - 2)):   # 불필요한 왕복 제거한 범위
                        if cx == 0:             # 가장 위에 도착하면
                            _dir = 2            # 아래로 턴
                        if cx == R-1:           # 가장 아래 도착하면
                            _dir = 1            # 위로 턴
                        cx = cx + dx[_dir - 1]  # 상어 이동 중...

                elif _dir == 3 or _dir == 4:
                    for _ in range(_speed % (C * 2 - 2)):   # 불필요한 왕복 제거한 범위
                        if cy == 0:             # 가장 왼쪽이면
                            _dir = 3            # 오른쪽으로 턴
                        if cy == C-1:           # 가장 오른쪽이면
                            _dir = 4            # 왼쪽으로 턴
                        cy = cy + dy[_dir - 1]  # 상어 이동 중...

                if nxt_ocean[cx][cy]:
                    pre_size = nxt_ocean[cx][cy][2]
                    if _size > pre_size:
                        nxt_ocean[cx][cy] = [_speed, _dir, _size]
                else:
                    nxt_ocean[cx][cy] = [_speed, _dir, _size]

    ocean = nxt_ocean[:]


fish_king = -1                               # 1번 열의 한 칸 왼쪽에 있다(init)
total_shark_size = 0                         # 잡은 상어 크기의 합

while fish_king < C - 1:                     # (가장 오른쪽 열의 오른쪽 칸에 이동하면 멈춤)
    fish_king += 1                           # 낚시왕이 한 칸 이동한다
    catch_shark()                            # 상어를 잡는다(크기 기록)
    shark_move()                             # 상어가 이동한다

print(total_shark_size)
from collections import deque

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())        # 사과의 위치
    board[r-1][c-1] = 1                     # 보드에 1로 표시
L = int(input())
cmd = deque()
for _ in range(L):
    X, C = input().split()                  # 뱀의 방향 변환 정보
    cmd.append([int(X), C])                 # X초가 끝난 뒤에 C방향 으로 회전


def snake_game():
    time, d = 0, 0                           # 게임 시간, 현재 방향(오른쪽을 보고 있음)
    cmd_time, cmd_d = cmd.popleft()              # 최초 방향 변환 시간, 방향 정보
    hx, hy = 0, 0                            # 게임이 시작할때 뱀은 맨위 맨좌측에 위치
    board[hx][hy] = 2                        # 뱀은 보드에 2로 표시
    snake = deque([(hx, hy)])                # 뱀 몸통

    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)    # 방향(우, 좌, 하, 상)
    L, D = (3, 2, 0, 1), (2, 3, 1, 0)        # 왼쪽(상좌하우), 오른쪽(하좌상우)

    while True:
        time += 1                            # 1초가 지나면서
        hx, hy = hx + dx[d], hy + dy[d]      # 뱀이 이동하고

        if hx < 0 or hx >= N or hy < 0 or hy >= N or board[hx][hy] == 2:
            return time

        if not board[hx][hy]:                 # 만약 이동한 칸에 아무것도 없으면
            tx, ty = snake.popleft()          # 몸길이를 줄여서
            board[tx][ty] = 0                 # 꼬리가 위치한 칸을 비워준다

        snake.append((hx, hy))                # 뱀은 몸길이를 늘려
        board[hx][hy] = 2                     # 머리를 다음칸에 위치시킨다

        if time == cmd_time:                 # 만약 방향을 바꾸는 시간이라면
            if cmd_d == 'L':
                d = L[d]
            else:
                d = D[d]
            if cmd:                          # 명령어가 남아 있다면
                cmd_time, cmd_d = cmd.popleft()


ans = snake_game()
print(ans)
from collections import deque

N = int(input())
dragon_curves = deque(list(map(int, input().split())) for _ in range(N))

gen = [0]                                  # 0세대 시작 방향은 0이다(->)
for i in range(1, 11):                     # 10세대까지 미리 구해보자
    k = 1 << (i-1)                         # k-1 세대의 선분 개수
    for j in range(k):
        gen.append((gen[k-1-j] + 1) % 4)   # k-1 세대 드래곤 커브를 90도 회전한 값을 더한다

dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
board = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = dragon_curves.popleft()

    board[x][y] = 1                         # 시작점 표시
    for i in range(1 << g):                 # 0세대 부터 g세대까지
        nd = (d + gen[i]) % 4               # 시작방향(d)을 반영한 다음 방향으로
        x, y = x + dx[nd], y + dy[nd]       # 점을 옮겨가며
        board[x][y] = 1                     # 각 점을 표시

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            cnt += 1

print(cnt)
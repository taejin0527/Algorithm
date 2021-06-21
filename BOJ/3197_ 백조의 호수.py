"""
@params
R, C                호수(행렬)의 크기
[lake * C] * R      호수의 상태

@return
answer              두 백조가 만나는 날
"""
from collections import deque
import sys, copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
encounter = False
swan = []
waterq = deque()
swanq = deque()
next_swanq = deque()
next_waterq = deque()
day = 0


def swan_bfs():
    global encounter

    while swanq and not encounter:
        x, y = swanq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == False:
                if board[nx][ny] == "L":
                    encounter = True
                    v[nx][ny] = True
                    return
                elif board[nx][ny] == ".":
                    swanq.append((nx, ny))
                    v[nx][ny] = True
                elif board[nx][ny] == "X":
                    v[nx][ny] = True
                    next_swanq.append((nx, ny))


def water_bfs():
    global swanq, waterq, next_swanq, next_waterq

    while waterq:
        x, y = waterq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == "X":
                    board[nx][ny] = "."
                    next_waterq.append((nx, ny))

    swanq = next_swanq
    waterq = next_waterq
    next_swanq = deque()
    next_waterq = deque()


n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
v = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            swan = (i, j)
        if board[i][j] != "X":
            waterq.append((i, j))


swanq.append((swan[0], swan[1]))
v[swan[0]][swan[1]] = True

swan_bfs()
while not encounter:
    water_bfs()
    swan_bfs()
    day += 1

print(day)

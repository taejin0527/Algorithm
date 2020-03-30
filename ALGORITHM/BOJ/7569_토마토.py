"""
INPUT
M, N, H
(N lines) BOX
    M: 상자의 가로 칸의 수 (2 ≤ M ≤ 100)
    N: 상자의 세로 칸의 수 (2 ≤ N ≤ 100)
    H: 상자의 수 (1 ≤ H ≤ 100)
    BOX: 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보

    (정수)1: 익은 토마토
         0: 익지 않은 토마토
        -1: 토마토가 들어있지 않은 칸

OUTPUT
토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산
     n: 걸린 시간(날짜)
     0: 모두 이미 익어있는 상태
    -1: 모두 익지 못하는 상태
"""
from collections import deque
from sys import stdin
input = stdin.readline

def check_box(V, Q):
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    V.append((z, y, x))
                    Q.append((z, y, x))

    return V, Q


def bfs():
    v, q = [], deque()
    _dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    days = 0

    visited, queue = check_box(v, q)

    while queue:
        size = len(queue)
        days += 1

        for i in range(size):
            z, y, x = queue.popleft()

            for nz, ny, nx in _dir:
                next_z, next_y, next_x = nz + z, ny + y, nx + x
                next_dir = (next_z, next_y, next_x)

                if 0 <= next_z < H and 0 <= next_y < N and 0 <= next_x < M:
                    if next_dir not in visited and box[next_z][next_y][next_x] != -1:
                        visited.append(next_dir)
                        queue.append(next_dir)
                        box[next_z][next_y][next_x] = 1

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if box[k][i][j] == 0:
                    return -1

    return days - 1


M, N, H = [int(n) for n in input().split()]
box = [[[]for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        box[h][n] = list(map(int, input().split()))

print(bfs())


# 위에 내가 작성한 코드는 시간초과가 뜬다ㅠㅠ
"""
from collections import deque
import sys
input = sys.stdin.readline


M, N, H = map(int, input().split())
boxes = []
check = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue = deque([])
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    boxes.append(box)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                queue.append((i, j, k, 0))
day = 0
while queue:
    i, j, k, c = queue.popleft()
    for x, y, z in (-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0):
        xx, yy, zz = x+i, y+j, z+k
        if xx < 0 or yy < 0 or zz < 0 or xx >= H or yy >= N or zz >= M:
            continue
        if not check[xx][yy][zz] and boxes[xx][yy][zz] == 0:
            check[xx][yy][zz] = 1
            boxes[xx][yy][zz] = 1
            queue.append((xx, yy, zz, c+1))
    day = max(day, c)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 0:
                print(-1)
                sys.exit()
print(day)
"""
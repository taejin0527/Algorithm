from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
lab = [[int(n) for n in input().split()] for _ in range(N)]
queue = deque()


def select_walls(_x, _y, cnt):
    if cnt == 3:
        new_lab = deepcopy(lab)

    else:
        for i in range(_x, N):
            for j in range(_y, M):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    select_walls(i, j, cnt + 1)
                    lab[i][j] = 0


def find_virus():
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append((i, j))


def bfs():
    while queue:
        S = queue.popleft()

        print(S)


find_virus()
bfs()

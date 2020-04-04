"""
지도 크기:
    - R * C
지도 표시:
    - '.': 비어있는 곳
    - '*': 물이 차있는 지역
    - 'X': 돌
    - 'D': 비버의 굴
    - 'S': 고슴도치의 위치
조건:
    - 물은 매 분마다 인접해있는 비어있는 칸으로 확장 (돌, 비버의 굴 통과 못함)
    - 고슴도치는 매 분마다 (위, 아래, 오른쪽, 왼쪽)으로 이동 가능 (돌, 물 통과 못함)
    * 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다
"""
from collections import deque


def find_location():
    w, s, d = [], (), ()
    for x in range(R):
        for y in range(C):
            if TW_map[x][y] == '*':
                w.append((x, y))
            if TW_map[x][y] == 'S':
                s = (x, y)
            if TW_map[x][y] == 'D':
                d = (x, y)
    return w, s, d


def bfs():
    queue = deque()
    water, hedgehog, beaver = find_location()
    queue.extend(water)
    queue.append(hedgehog)

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < R and 0 <= next_y < C:
                if TW_map[x][y] == '*' and TW_map[next_x][next_y] == '.':
                    TW_map[next_x][next_y] = '*'
                    queue.append((next_x, next_y))
                elif TW_map[x][y] == 'S' and (TW_map[next_x][next_y] == '.' or TW_map[next_x][next_y] == 'D'):
                    TW_map[next_x][next_y] = 'S'
                    visited[next_x][next_y] = visited[x][y] + 1
                    queue.append((next_x, next_y))

    return beaver


R, C = map(int, input().split())
TW_map = [[x for x in input()] for _ in range(R)]
visited = [[-1 for _ in range(C)] for _ in range(R)]

bx, by = bfs()
if visited[bx][by] == -1:
    print('KAKTUS')
else:
    print(visited[bx][by] + 1)
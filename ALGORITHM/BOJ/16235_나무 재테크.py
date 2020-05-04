"""
봄   : 자신의 나이만큼 양분을 먹고, 나이가 1 증가
여름 : 봄에 죽은 나무가 양분으로 변함(죽은 나무 나이를 2로 나눈 값)
가을 : 나이가 5의 배수인 나무가 번식
겨울 : S2D2가 양분을 추가, 양분의 양은 A 배열에 주어짐
"""
from collections import deque

N, M, K = map(int, input().split())
A = [[int(n) for n in input().split()] for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]      # 같은 칸에 여러 개의 나무가 심어져 있을 수도 있다
tree_cnt = 0
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
    tree_cnt += 1
nutrient = [[5 for _ in range(N)] for _ in range(N)]


def spring_summer():
    global tree_cnt

    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if nutrient[i][j] >= tree[i][j][k]:         # 양분이 충분하면
                    nutrient[i][j] -= tree[i][j][k]         # 나무가 양분을 흡수하고
                    tree[i][j][k] += 1                      # 나이를 한살 더 먹는다
                else:
                    while k < len(tree[i][j]):              # 양분이 충분하지 않으면
                        nutrient[i][j] += (tree[i][j].pop() // 2)   # 죽은 나무 나이의 1/2이 양분으로 더해지며
                        tree_cnt -= 1                       # 나무는 죽음
                    break


def fall_winter():
    global tree_cnt
    dx, dy = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)

    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if not tree[i][j][k] % 5:                   # 나이가 5의 배수인 나무
                    for t in range(8):                      # 주변에
                        nx, ny = i+dx[t], j+dy[t]
                        if 0 <= nx < N and 0 <= ny < N:     # (범위를 벗어나지 않으면)
                            tree[nx][ny].appendleft(1)      # 나이 1인 나무를 번식
                            tree_cnt += 1

            nutrient[i][j] += A[i][j]                       # S2D2가 양분 추가


for _ in range(K):  # K년이 흐르고...
    spring_summer() # 봄, 여름
    fall_winter()   # 가을, 겨울

print(tree_cnt)     # 살아있는 나무의 개수

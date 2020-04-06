# 탐색 좌표의 순서를 문제에 첨부되어 있는 이미지에 나타난 색깔 순
# 파랑(2), 노랑(1), 주황(8), 초록(4), 분홍(4) = 총 (19)

blue = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)]
]
yellow = [
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]
orange = [
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (0, -1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (0, -1), (0, -2), (1, 0)],
    [(0, 0), (-1, 0), (0, -1), (0, -2)],
    [(0, 0), (-1, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (0, 1), (0, 2)]
]
green = [
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]
pink = [
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (-1, 1), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)]
]


def tetromino(x, y):
    sub_total = 0

    for shape in shapes:
        each_total = 0
        for nx, ny in shape:
            try:
                next_x, next_y = x + nx, y + ny
                each_total += board[next_x][next_y]
            except IndexError:
                continue

        sub_total = max(sub_total, each_total)

    return sub_total


N, M = map(int, input().split())
board = [[int(n) for n in input().split()] for _ in range(N)]
shapes = blue + yellow + orange + green + pink

max_total = 0
for i in range(N):
    for j in range(M):
        max_total = max(max_total, tetromino(i, j))

print(max_total)

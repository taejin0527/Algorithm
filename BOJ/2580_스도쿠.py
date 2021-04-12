import sys

board = [list(map(int, input().split())) for _ in range(9)]
zeroes = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def sdoku(cnt):
    if cnt == len(zeroes):
        for row in board:
            print(*row)
        sys.exit(0)
    else:
        x, y = zeroes[cnt]
        dx, dy = (x//3)*3, (y//3)*3

    num_list = [True] + [False for _ in range(9)]
    # row, col
    for j in range(9):
        if board[x][j] > 0:
            num_list[board[x][j]] = True
        if board[j][y] > 0:
            num_list[board[j][y]] = True

    # 3x3 box
    for i in range(dx, dx+3):
        for j in range(dy, dy+3):
            if board[i][j] > 0:
                num_list[board[i][j]] = True

    for num, chk in enumerate(num_list):
        if chk: continue
        board[x][y] = num
        sdoku(cnt+1)
        board[x][y] = 0


sdoku(0)

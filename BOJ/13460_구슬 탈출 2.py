from collections import deque

N, M = map(int, input().split())
board = [[b for b in input()] for _ in range(N)]
queue = deque()
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]


def find_xy():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red = i, j
            if board[i][j] == 'B':
                blue = i, j

    visited[red[0]][red[1]][blue[0]][blue[1]] = True
    queue.append((*red, *blue, 1))


def move(_x, _y, dx, dy, cnt):
    while board[_x + dx][_y + dy] != '#' and board[_x][_y] != 'O':
        _x += dx
        _y += dy
        cnt += 1
    return _x, _y, cnt


def bfs():
    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        if depth > 10:
            break

        for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rnx, rny, cnt_r = move(rx, ry, nx, ny, 0)
            bnx, bny, cnt_b = move(bx, by, nx, ny, 0)

            if board[bnx][bny] == 'O':
                continue
            if board[rnx][rny] == 'O':
                print(depth)
                return
            if (rnx, rny) == (bnx, bny):
                if cnt_r > cnt_b:
                    rnx, rny = rnx - nx, rny - ny
                else:
                    bnx, bny = bnx - nx, bny - ny

            if not visited[rnx][rny][bnx][bny]:
                visited[rnx][rny][bnx][bny] = True
                queue.append((rnx, rny, bnx, bny, depth + 1))

    print(-1)


find_xy()
bfs()

from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(s, e):
    steps = 0
    queue = deque()
    queue.append([s[0], s[1], steps])
    board[s[0]][s[1]] = True

    while queue:
        x, y, step = queue.popleft()

        if [x, y] == e:
            return step
        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < chess_len and 0 <= ny < chess_len and not board[nx][ny]:
                    board[nx][ny] = True
                    queue.append([nx, ny, step + 1])


for _ in range(int(input())):
    chess_len = int(input())
    start = [int(n) for n in input().split()]
    end = [int(n) for n in input().split()]

    board = [[False] * chess_len for _ in range(chess_len)]
    print(bfs(start, end))



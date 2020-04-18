from collections import deque, defaultdict


def find_start():
    start = 0
    fx, fy = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 9
            start = start * 10 + board[i][j]
    return start


def puzzle(start):
    q = deque()
    dist = defaultdict()

    q.append(start)
    dist[start] = 0

    while q:
        now_num = q.popleft()
        now = str(now_num)
        z = now.find('9')
        x = z // 3
        y = z % 3

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                temp = list(now)
                temp[x * 3 + y], temp[nx * 3 + ny] = temp[nx * 3 + ny], temp[x * 3 + y]
                num = int(''.join(temp))

                if num not in dist:
                    dist[num] = dist[now_num] + 1
                    q.append(num)

    if 123456789 in dist:
        print(dist[123456789])
    else:
        print(-1)


board = [[int(n) for n in input().split()] for _ in range(3)]

puzzle(find_start())
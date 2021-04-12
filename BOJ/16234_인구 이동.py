from collections import deque

N, L, R = map(int, input().split())
A = [[int(n) for n in input().split()] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt, migration = -1, True


def borderline():
    global cnt, visited, migration

    while migration:
        migration = False
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    bfs(i, j)
        cnt += 1


def bfs(x, y):
    global migration
    visited[x][y] = True
    union = [(x, y)]
    queue = deque([(x, y)])
    total_population = A[x][y]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(A[nx][ny] - A[cx][cy]) <= R:
                    migration = True
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    queue.append((nx, ny))
                    total_population += A[nx][ny]

    union_num = len(union)
    if union_num == 1:          # 연합이 없음(국경이 안 열림)
        return

    average = total_population // union_num
    for i, j in union:
        A[i][j] = average


borderline()
print(cnt)

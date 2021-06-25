from collections import deque

N, M = map(int, input().split())
지도 = [list(map(int, input())) for _ in range(N)]

방문 = [[-1] * M for _ in range(N)]
이세카이 = [[-1] * M for _ in range(N)]

q = deque([[0, 0, False]])
방문[0][0] = 1

while q:
    x, y, 벽부숨 = q.popleft()

    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if not 벽부숨:
            if 방문[nx][ny] > 0:
                continue
            if 지도[nx][ny] == 1:
                이세카이[nx][ny] = 방문[x][y] + 1
                q.append([nx, ny, True])
                continue
            방문[nx][ny] = 방문[x][y] + 1
            q.append([nx, ny, False])

        else:
            if 이세카이[nx][ny] > 0:
                continue
            if 지도[nx][ny] == 1:
                continue
            이세카이[nx][ny] = 이세카이[x][y] + 1
            q.append([nx, ny, True])

print(*방문, sep="\n")
print()
print(*이세카이, sep="\n")


ans1 = 방문[N - 1][M - 1]
ans2 = 이세카이[N - 1][M - 1]

if ans1 > 0 and ans2 == -1:
    print(ans1)
elif ans1 == -1 and ans2 > 0:
    print(ans2)
else:
    print(min(ans1, ans2))

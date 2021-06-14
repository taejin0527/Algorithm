"""
@params
N, M                    행의 크기, 열의 크기
[farm * M] * N          농장 상태

@return
answer                  산봉우리의 개수
"""

from sys import stdin
input = stdin.readline


N, M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def dfs(cx, cy):
    global is_peak

    for nx, ny in ((cx, cy+1), (cx, cy-1), (cx+1, cy), (cx-1, cy),
                   (cx+1, cy+1), (cx+1, cy-1), (cx-1, cy-1), (cx-1, cy+1)):
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if farm[nx][ny] > farm[cx][cy]:
            is_peak = False
        if visited[nx][ny] or farm[nx][ny] != farm[cx][cy]:
            continue

        visited[nx][ny] = True
        dfs(nx, ny)

    return


answer = 0
is_peak = True
for x in range(N):
    for y in range(M):
        if not visited[x][y] and farm[x][y]:
            visited[x][y] = True
            is_peak = True
            dfs(x, y)
            if is_peak:
                answer += 1

print(answer)
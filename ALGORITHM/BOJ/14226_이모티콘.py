from collections import deque


def bfs(screen, clip):
    queue = deque()
    visited[screen][clip] = 0
    queue.append((screen, clip))

    while queue:
        ts, tc = queue.popleft()

        # 1 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if ts < MAX and visited[ts][ts] == -1:
            visited[ts][ts] = visited[ts][tc] + 1
            queue.append((ts, ts))

        # 2 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        paste = ts + tc
        if paste < MAX and visited[paste][tc] == -1:
            visited[paste][tc] = visited[ts][tc] + 1
            queue.append((paste, tc))

        # 3 화면에 있는 이모티콘 중 하나를 삭제한다.
        if 0 <= ts - 1 and visited[ts-1][tc] == -1:
            visited[ts-1][tc] = visited[ts][tc] + 1
            queue.append((ts-1, tc))


MAX = 1001
S = int(input())
visited = [[-1] * MAX for _ in range(MAX)]

bfs(1, 0)
ans = MAX
for m in visited[S]:
    if m != -1 and m < ans:
        ans = m
print(ans)
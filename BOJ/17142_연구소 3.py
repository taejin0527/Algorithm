from collections import deque
from itertools import combinations

N, M = map(int, input().split())
lab = [[int(n) for n in input().split()] for _ in range(N)]
virus, safe = deque(), 0


def scenario():
    find_virus()                                    # 바이러스 위치 파악

    for each_scenario in combinations(virus, M):    # M개를 활성화하는 모든 경우를
        bfs(each_scenario)                          # bfs 탐색으로 계산


def find_virus():
    global virus, safe

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:                      # 빈 칸이면
                safe += 1                           # 카운트(모두 퍼졌는지 확인하기 위해)
            if lab[i][j] == 2:                      # 바이러스면
                virus.append((i, j))                # 큐에 저장


def bfs(virus_pos):
    global ans
    time = [[-1 for _ in range(N)] for _ in range(N)]            # 각 칸에 바이러스가 퍼지는 시간
    max_time, infected = 0, 0                                    # 최종 시간, 감염된 칸의 수
    active_virus = deque()

    for pos in virus_pos:
        active_virus.append(pos)                                 # 활성화되는 바이러스 큐에 저장
        time[pos[0]][pos[1]] = 0                                 # 해당 위치 0초

    while active_virus:                                          # 활성화된 바이러스가 있는 동안
        cx, cy = active_virus.popleft()                          # 현재 바이러스 위치 기준으로

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):          # 네 방향으로 퍼지는데
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N:                      # 범위를 벗어나지 않으면서
                if lab[nx][ny] != 1 and time[nx][ny] == -1:      # 벽이 아니고 방문한 곳이 아니면
                    time[nx][ny] = time[cx][cy] + 1              # 바이러스 시간 갱신
                    active_virus.append((nx, ny))                # 큐에 추가

                    if lab[nx][ny] == 0:
                        infected += 1
                        max_time = time[nx][ny]
    if safe == infected:
        ans = min(ans, max_time)


ans = 10**9
scenario()

print(ans if ans != 10**9 else -1)

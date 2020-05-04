R, C, T = map(int, input().split())
A = [[int(n) for n in input().split()] for _ in range(R)]
air_cleaner = 0 # 위쪽 공기청정기 위치좌표(아래쪽은 +1 하면 됨)
for i in range(R):
    if A[i][0] == -1:
        air_cleaner = i
        break


def diffuse():
    temp_A = [[0 for _ in range(C)] for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if A[x][y] >= 5:                                            # 먼지가 5 이하는 확산될 때 사라진다
                dust = A[x][y] // 5                                     # 확산되는 미세먼지 양
                for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):         # 4 방향을 돌아가며
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C:                     # 범위 안에 들어가며
                        if A[nx][ny] != -1:                             # 공기청정기가 아니라면
                            temp_A[nx][ny] += dust                      # 확산되는 먼지를 임시로 저장하고
                            A[x][y] -= dust                             # 해당 칸의 미세먼지는 줄여준다

    for x in range(R):
        for y in range(C):
            A[x][y] += temp_A[x][y]                                     # 임시로 저장했던 먼지를 더한다


def wind_cycle():
    up, down = air_cleaner, air_cleaner+1

    # 위쪽 공기청정기(반시계방향 순환)
    for x in range(up-1, 0, -1):      # 1번열 아래로 이동
        A[x][0] = A[x-1][0]
    for y in range(C-1):               # 1번행 왼쪽으로 이동
        A[0][y] = A[0][y+1]
    for x in range(up):                # C열 위로 이동
        A[x][C-1] = A[x+1][C-1]
    for y in range(C-1, 0, -1):       # 공기청정기가 있는 행 오른쪽으로 이동
        A[up][y] = A[up][y-1]

    A[up][1] = 0                          # 공기청정기에서 정화되어 나감

    # 아래쪽 공기청정기(시계방향 순환)
    for x in range(down+1, R-1):       # 1번열 위로 이동
        A[x][0] = A[x+1][0]
    for y in range(C-1):               # R행 왼쪽으로 이동
        A[R-1][y] = A[R-1][y+1]
    for x in range(R-1, down, -1):   # C열 아래로 이동
        A[x][C-1] = A[x-1][C-1]
    for y in range(C-1, 0, -1):       # 공기청정기가 있는 행 오른쪽으로 이동
        A[down][y] = A[down][y-1]

    A[down][1] = 0                       # 공기청정기에서 정화되어 나감


for _ in range(T):  # T초 동안
    diffuse()       # 미세먼지가 확산
    wind_cycle()    # 공기청정기가 작동

ans = 0
for s in A:
    ans += sum(s)

print(ans + 2)      # 구사과 방에 남아있는 미세먼지의 양(공기청정기 때문에 +2)

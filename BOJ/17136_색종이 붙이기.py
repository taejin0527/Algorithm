"""
@params
[[n * 10] * 10]            총 10개의 줄에 종이의 각 칸에 적힌 수

@return
answer                      모든 1을 덮는데 필요한 색종이의 최소 개수 (불가능하면 -1)
"""
from collections import Counter

grid = [list(map(int, input().split())) for _ in range(10)]
total = Counter([i for row in grid for i in row])[1]        # 0과 1의 개수를 구해서 그 중 1인 칸의 개수
paper = [0 for _ in range(5)]
minPaperCnt = int(1e9)


def dfs(x, y, paperCnt):
    global minPaperCnt

    if y >= 10:         # 탐색 완료
        minPaperCnt = min(minPaperCnt, paperCnt)
        return

    if x >= 10:         # 행의 끝에 닿으면 다음 행으로 이동
        dfs(0, y+1, paperCnt)
        return

    if grid[x][y] == 1:    # 놓을 수 있는 위치면
        for k in range(5):  # 각 종이를 매칭시키는데
            if paper[k] == 5:   # 만약 5장 다 썼으면 스킵
                continue
            if x + k >= 10 or y + k >= 10:  # 범위를 벗어나도 스킵
                continue

            flag = False
            for i in range(x, x + k + 1):   # 종이 크기만큼 1이 있는지 확인
                for j in range(y, y + k + 1):
                    if grid[i][j] == 0:
                        flag = True
                        break
                if flag:
                    break

            if not flag:                    # 만약 놓을 수 있다면
                for i in range(x, x + k + 1):   # 1을 0으로 바꿔주고
                    for j in range(y, y + k + 1):
                        grid[i][j] = 0

                paper[k] += 1
                dfs(x + k + 1, y, paperCnt + 1)
                paper[k] -= 1

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        grid[i][j] = 1
    else:
        dfs(x + 1, y, paperCnt)

dfs(0, 0, 0)

answer = -1 if minPaperCnt == int(1e9) else minPaperCnt
print(answer)
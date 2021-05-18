from collections import defaultdict

"""
@params
N               교실 크기 (학생수 = N^2)
[list]          학생의 번호, 그 학생이 좋아하는 학생 4명의 번호

@return
answer          학생의 만족도 총 합
"""
N = int(input())
classroom = [[0] * N for _ in range(N)]
friendly = defaultdict(list)

for _ in range(N**2):
    std, *args = map(int, input().split())
    friendly[std] = args
    
    mx, my, maxLike, maxEmpty = 0, 0, -1, -1
    
    for x in range(N):
        for y in range(N):
            if classroom[x][y] == 0:
                curLike, curEmpty = 0, 0
                
                for nx, ny in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
                    if not (0 <= nx < N and 0 <= ny < N):
                        continue
                    if classroom[nx][ny] in args:
                        curLike += 1
                    elif classroom[nx][ny] == 0:
                        curEmpty += 1
                        
                if curLike > maxLike: # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
                    mx, my = x, y
                    maxLike, maxEmpty = curLike, curEmpty
                elif curLike == maxLike and curEmpty > maxEmpty: # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
                    mx, my = x, y
                    maxLike, maxEmpty = curLike, curEmpty
                # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    
    classroom[mx][my] = std

scores = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
answer = 0

for x in range(N):
    for y in range(N):
        score = 0
        for nx, ny in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if classroom[nx][ny] in friendly[classroom[x][y]]:
                score += 1
                
        answer += scores[score]


print(answer)
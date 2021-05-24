from collections import deque

"""
@params
N, M            격자 한 변의 크기, 색상의 개수
[list]          격자의 칸에 들어있는 블록의 정보

@return
answer          획득한 점수의 합
"""

# 검은색 -1, 무지개 0, 일반 (M가지 색상)

def find_block(x, y, visited):
    blockColor = grid[x][y]
    cur_blocks = [(x, y)]
    rainbow_blocks = []
    min_x, min_y = x, y
    
    q = deque([(x, y)])
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()

        for nx, ny in ((cx, cy+1), (cx, cy-1), (cx+1, cy), (cx-1, cy)):
            if not (0 <= nx < N and 0 <= ny < N):   # 범위를 벗어나거나
                continue
            if visited[nx][ny]:                     # 방문했거나
                continue
            if grid[nx][ny] not in (0, blockColor): # 무지개 블록, 검색하는 블록이 아니면 정지
                continue
            
            if grid[nx][ny] == 0:
                rainbow_blocks.append((nx, ny))
            
            if min_x > nx or (min_x == nx and min_y > ny):
                min_x, min_y = nx, ny

            visited[nx][ny] = True
            cur_blocks.append((nx, ny))
            q.append((nx, ny))
         
    for x, y in rainbow_blocks:
        visited[x][y] = False
        
    return cur_blocks, rainbow_blocks, min_x, min_y


def gravity(grid):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if grid[i][j] >= 0 and grid[i+1][j] == -2:
                flag = 0
                for k in range(i+1, N):
                    nx = k
                    if grid[k][j] > -2:
                        flag = 1
                        break
                if flag:
                    grid[nx-1][j] = grid[i][j]
                else:
                    grid[nx][j] = grid[i][j]
                grid[i][j] = -2


N, M = map(int, input().split())
grid = [list(map(int, list(input().split()))) for _ in range(N)]


answer = 0

while True:
    # 크기가 가장 큰 블록 그룹 찾기
    max_blocks = []
    max_rainbow = 0
    max_x, max_y = -1, -1
    visited = [[False] * N for _ in range(N)]
    
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and grid[x][y] > 0:
                cur_blocks, rainbow_blocks, cx, cy = find_block(x, y, visited)
            
                if len(cur_blocks) > len(max_blocks):
                    max_blocks = cur_blocks
                    max_x, max_y = cx, cy
                elif len(cur_blocks) == len(max_blocks):
                    if len(rainbow_blocks) > max_rainbow:
                        max_blocks = cur_blocks
                        max_x, max_y = cx, cy
                    elif len(rainbow_blocks) == max_rainbow:
                        if cx > max_x or (cx == max_x and cy > max_y):
                            max_x, max_y = cx, cy
                            max_blocks = cur_blocks
                
    if len(max_blocks) < 2:
        break
    
            
    # 블록 제거, 점수 획득
    for x, y in max_blocks:
        grid[x][y] = -2
        
    answer += len(max_blocks) ** 2

    # 중력 작용
    gravity(grid)
    
    # 90도 반시계 회전
    grid = list(zip(*grid))[::-1]
    grid = [list(g) for g in grid]

    # 중력 작용
    gravity(grid)

print(answer)
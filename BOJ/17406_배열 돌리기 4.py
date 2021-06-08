"""
@params
N, M, K               배열 크기, 회전 연산의 개수
[[n] * M] * N         배열에 들어가는 수
[r, c, s] * K         회전 연산 정보

@return
answer          각 행에 있는 모든 수의 합 중 최솟값
"""
from itertools import permutations

def rotate(array, cases):
    global answer
    for r, c, s in cases:
        r -= 1
        c -= 1

        for d in range(s, 0, -1):
            save = array[r-d][c-d]              # save left-top
            for x in range(r-d, r+d):           # push left col
                array[x][c-d] = array[x+1][c-d]
            for y in range(c-d, c+d):           # push bottom row
                array[r+d][y] = array[r+d][y+1]
            for x in range(r+d, r-d, -1):       # push right col
                array[x][c+d] = array[x-1][c+d]
            for y in range(c+d, c-d+1, -1):     # push top row
                array[r-d][y] = array[r-d][y-1]
            array[r-d][c-d+1] = save            # put saved left-top

    for row in array:
        answer = min(answer, sum(row))


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cmds = [list(map(int, input().split())) for _ in range(K)]
answer = int(1e9)
# 순열을 구하고
perm = permutations(cmds, K)

# 각 순열마다 회전을 수행
for p in perm:
    temp = [row[:] for row in grid]
    rotate(temp, p)

print(answer)
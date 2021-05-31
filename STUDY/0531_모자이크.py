"""
@params
R, C        행, 열의 크기 (1000000 이하)
paperCnt    색종이 장수
N           잘못 칠해진 칸의 수
[x, y]      잘못 칠해진 칸의 위치(N개)

@return
answer          가장 작은 색종이의 크기
"""

def paper_cnt(width):
    start = -1
    cnt = 0

    for i in range(len(pos)):
        if i == 0:
            start = pos[i]
            cnt += 1
        else:
            if pos[i] >= start + width:
                start = pos[i]
                cnt += 1

    return cnt



R, C = map(int, input().split())
paperCnt = int(input())
N = int(input())
maxHeight = 0
pos = []
for _ in range(N):
    x, y = map(int, input().split())
    maxHeight = max(maxHeight, x)
    pos.append(y)

# 혹시 모르니 정렬
pos.sort()

left = maxHeight
right = int(1e6)
while left < right:
    mid = (left + right) // 2

    if paper_cnt(mid) <= paperCnt:
        right = mid
    else:
        left = mid + 1

print(left)
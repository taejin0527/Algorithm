# https://www.acmicpc.net/problem/2631

"""
@params
N           아이들의 수
[list]      아이 번호

@return
answer      번호대로 줄을 세우는데 옮겨지는 아이들의 최소 수
"""
N = int(input())
children = []
for _ in range(N):
    children.append(int(input()) - 1)

dp = [[0] * N for _ in range(N)]

dp[0][children[0]] = 1
for idx, child in enumerate(children):
    if idx == 0:
        continue
    dp[idx] = dp[idx-1]
    dp[idx][child] = max(dp[idx][:child+1]) + 1


print(N - max(dp[N-1]))
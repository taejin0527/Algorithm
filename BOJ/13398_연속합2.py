n = int(input())
sequence = list(map(int, input().split()))

# 수를 제거한 경우 0, 제거하지 않은 경우 1
dp = [[0]*n for _ in range(2)]

dp[0][0] = sequence[0]
dp[1][0] = 0

ans = -1e9
if n == 1:
    print(sequence[0])
else:
    for i in range(n-1):
        # (제거 안 하는 경우)
        dp[0][i+1] = max(dp[0][i] + sequence[i+1], sequence[i+1])
        # (제거한 경우)
        # 이전에 제거한 경우, 이번에 제거하는 경우 비교
        dp[1][i+1] = max(dp[1][i] + sequence[i+1], dp[0][i])

        ans = max(ans, dp[0][i+1], dp[1][i+1])

    print(ans)

def max_profit():
    dp = [0] * N
    day, money = zip(*schedule)

    # 마지막 날 상담 가능한지 확인
    if day[N-1] == 1:
        dp[N-1] = money[N-1]

    # 마지막 전 날부터 DP 계산
    for cur in range(N-2, -1, -1):
        if cur + day[cur] > N:
            dp[cur] = dp[cur + 1]
        else:
            if cur + day[cur] == N:
                dp[cur] = max(money[cur], dp[cur + 1])
            else:
                dp[cur] = max(dp[cur + day[cur]] + money[cur], dp[cur + 1])

    print(dp[0])


N = int(input())
schedule = [[int(n) for n in input().split()] for _ in range(N)]

max_profit()
for tc in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    total = int(input())

    dp = [1] + [0 for _ in range(total)]
    for i in range(N):
        for j in range(1, total+1):
            if j - coins[i] >= 0:
                dp[j] += dp[j - coins[i]]

    print(dp[total])
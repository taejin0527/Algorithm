"""
LIS 응용
"""

from sys import stdin

input = stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x: x[0])

dp = [0] * N
dp[0] = 1

for i in range(1, N):
    max_value = 0
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            max_value = max(dp[j], max_value)
    dp[i] = max_value + 1

print(N - max(dp))
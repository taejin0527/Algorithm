n = int(input())
sequence = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    
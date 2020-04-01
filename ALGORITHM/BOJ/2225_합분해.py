# N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)

mod = 1000000000
N, K = [int(n) for n in input().split()]
d = [[0 for _ in range(N+1)] for _ in range(K+1)]
d[0][0] = 1

for k in range(1, K+1):
    for n in range(N+1):
        d[k][n] = (d[k-1][n] + d[k][n-1]) % mod

print(d[K][N])
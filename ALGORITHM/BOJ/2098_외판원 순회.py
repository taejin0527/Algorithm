def find_path(last, visited):
    inf = float('inf')

    if visited == (1 << N) - 1:
        return W[last][0] if W[last][0] > 0 else inf

    if DP[last][visited]:
        return DP[last][visited]

    tmp = inf
    for city in range(N):
        if visited & (1 << city) == 0 and W[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])
    DP[last][visited] = tmp

    return tmp


N = int(input())
W = [[int(n) for n in input().split()] for _ in range(N)]

DP = [[None] * (1 << N) for _ in range(N)]

print(find_path(0, 1 << 0))

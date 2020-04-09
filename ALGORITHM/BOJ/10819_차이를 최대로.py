from itertools import permutations

N = int(input())
A = [int(n) for n in input().split()]

MAX_total = 0
for p in permutations(A):
    total = 0
    for idx in range(N-1):
        total += abs(p[idx] - p[idx+1])

    MAX_total = max(MAX_total, total)

print(MAX_total)
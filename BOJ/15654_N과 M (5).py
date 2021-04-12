from itertools import permutations

N, M = map(int, input().split())
P = [int(n) for n in input().split()]

for p in permutations(sorted(P), M):
    print(*p)
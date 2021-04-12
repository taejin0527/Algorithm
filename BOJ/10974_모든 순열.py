from itertools import permutations

N = int(input())
A = range(1, N+1)

for a in permutations(A):
    print(*a)
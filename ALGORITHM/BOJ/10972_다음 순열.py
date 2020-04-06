from itertools import permutations

N = input()
P = [int(n) for n in input().split()]

print(*permutations(P))
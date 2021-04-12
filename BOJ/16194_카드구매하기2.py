N = int(input())
P = [int(n) for n in input().split()]
minP = [0] * (N + 1)

for i in range(1, N+1):
    if i == 1:
        minP[i] = P[i-1]
        continue
    if i == 2:
        minP[i] = min(P[i-1], P[i-2] * 2)
        continue

    minP[i] = P[i-1]
    for j in range(1, i//2+1):
        minP[i] = min(minP[i], minP[i-j] + minP[j])

print(minP[-1])
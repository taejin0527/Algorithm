N = int(input())
P = [int(n) for n in input().split()]
mP = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        mP[i] = P[i-1]    # 첫번째 카드팩
        continue
    if i == 2:
        mP[i] = max(P[i-1], P[i-2] * 2)   # 두번째 카드팩
        continue
    mP[i] = P[i-1]    # 한 팩으로 N개 사는 경우
    for j in range(1, i//2+1):
        mP[i] = max(mP[i], mP[i-j] + mP[j])


print(mP[-1])
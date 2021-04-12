exp = input().split('-')

partial_sum = []
for e in exp:
    temp = list(map(int, e.split('+')))
    partial_sum.append(sum(temp))

ans = partial_sum[0]
for p in partial_sum[1:]:
    ans -= p

print(ans)
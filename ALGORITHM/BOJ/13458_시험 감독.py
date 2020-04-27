N = int(input())
A = [int(n) for n in input().split()]
B, C = [int(n) for n in input().split()]

ans = 0
for num_a in A:
    ans += 1
    if num_a >= B:
        num_a -= B
        ans += (num_a // C + 1) if num_a % C else (num_a // C)

print(ans)

from itertools import combinations

N, S = map(int, input().split())
A = [int(n) for n in input().split()]

count = 0
for i in range(N):
    subsequence = combinations(A, i + 1)

    for sub in subsequence:
        if sum(sub) == S:
            count += 1

print(count)


"""
# 재귀함수 풀이
def sum_subsequence(idx, total):
    global count

    if idx == N:
        if total == S:
            count += 1
        return

    sum_subsequence(idx + 1, total + A[idx])
    sum_subsequence(idx + 1, total)


N, S = map(int, input().split())
A = [int(n) for n in input().split()]

count = 0
sum_subsequence(0, 0)
print(count if S else count - 1)
"""
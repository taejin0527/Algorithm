from collections import Counter

size_A = int(input())
A = [int(n) for n in input().split()]

count_A = Counter(A)
stack = []
result = [-1 for _ in range(size_A)]
for idx in range(size_A):
    while stack and count_A[A[stack[-1]]] < count_A[A[idx]]:
        result[stack.pop()] = A[idx]

    stack.append(idx)

print(*result)

"""
# 시간 초과 뜬다!

size_A = int(input())
A = [int(n) for n in input().split()]

current = A.pop(0)
stack = A
result = []
while stack:
    for num in stack:
        if current < num:
            result.append(num)
            break
    else:
        result.append(-1)

    current = A.pop(0)

result.append(-1)
print(*result)
"""

# O(n)으로 실행되게 만들어야 한다

size_A = int(input())
A = [int(n) for n in input().split()]

stack = []
result = [-1 for _ in range(size_A)]
for idx in range(size_A):
    while stack and A[stack[-1]] < A[idx]:
        result[stack.pop()] = A[idx]

    stack.append(idx)

print(*result)
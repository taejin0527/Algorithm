"""
@params
s                   a, b로만 이루어진 문자열

@return
answer              a를 모두 연속으로 만들기 위해서 필요한 교환의 최소 회수
"""
from collections import deque

s = input()
size = 0

for i in range(len(s)):
    if s[i] == 'b':
        size += 1

s += s
answer = size

q = deque()
for i in range(len(s)):
    print(q)
    if q:
        front = q.popleft()
        if i - front < size:
            q.appendleft(front)

    if s[i] == 'b':
        q.append(i)
    print(size, len(q))
    answer = min(answer, size - len(q))

print(answer)
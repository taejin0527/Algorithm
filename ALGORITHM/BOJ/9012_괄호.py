import sys


def solve(string):
    stack = []

    for ch in string:
        if len(stack) == 0 and ch == ')':
            return 'NO'

        if ch == '(':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    return 'NO'


t = int(input())
ans = []
for _ in range(t):
    PS = sys.stdin.readline().strip()
    ans.append(solve(PS))

for i in ans:
    print(i)
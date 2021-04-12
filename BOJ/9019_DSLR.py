from collections import deque


def DSLR(start):
    dslr = [
        ('D', lambda x: 2*x % 10000),
        ('S', lambda x: x - 1 if x else 9999),
        ('L', lambda x: (x%1000)*10 + (x//1000)),
        ('R', lambda x: (x//10) + (x%10)*1000),
    ]
    queue = deque([(start, '')])
    visited = [False] * 10000
    visited[start] = True

    while queue:
        now, commands = queue.popleft()

        if now == result:
            return commands

        for i, cmd in enumerate(dslr):
            temp = cmd[1](now)
            if not visited[temp]:
                queue.append((temp, commands + cmd[0]))
                visited[temp] = True


for test_case in range(int(input())):
    n, result = map(int, input().split())

    print(DSLR(n))
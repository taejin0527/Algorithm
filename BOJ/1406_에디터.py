from collections import deque
from sys import stdin

cursor_left, cursor_right = deque(stdin.readline()[:-1]), deque()
num_of_commands = int(stdin.readline())

for _ in range(num_of_commands):
    cmd, *args = stdin.readline().split()
    if cmd == 'L':
        if cursor_left:
            cursor_right.appendleft(cursor_left.pop())
    elif cmd == 'D':
        if cursor_right:
            cursor_left.append(cursor_right.popleft())
    elif cmd == 'B':
        if cursor_left:
            cursor_left.pop()
    elif cmd == 'P':
        cursor_left.append(*args)

print(*(cursor_left + cursor_right), sep='')

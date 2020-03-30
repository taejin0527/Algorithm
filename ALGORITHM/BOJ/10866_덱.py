from collections import deque
from sys import stdin

my_Q = deque()

N = int(stdin.readline())
for _ in range(N):
    cmd, *args = stdin.readline().split()

    if cmd == 'push_front':
        my_Q.appendleft(*args)
    elif cmd == 'push_back':
        my_Q.append(*args)
    elif cmd == 'pop_front':
        print(my_Q.popleft() if my_Q else -1)
    elif cmd == 'pop_back':
        print(my_Q.pop() if my_Q else -1)
    elif cmd == 'size':
        print(len(my_Q))
    elif cmd == 'empty':
        print(0 if my_Q else 1)
    elif cmd == 'front':
        print(my_Q[0] if my_Q else -1)
    elif cmd == 'back':
        print(my_Q[-1] if my_Q else -1)
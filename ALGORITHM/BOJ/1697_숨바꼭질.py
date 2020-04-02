from collections import deque


def bfs(start, end):
    queue = deque([start])
    location[start] = 0

    while queue:
        X = queue.popleft()

        if X == end:
            return location[X]

        if X+1 < MAX and location[X] + 1 < location[X+1]:
            location[X+1] = location[X] + 1
            queue.append(X + 1)
        if 0 < X and location[X] + 1 < location[X-1]:
            location[X-1] = location[X] + 1
            queue.append(X - 1)
        if X*2 < MAX and location[X] + 1 < location[2*X]:
            location[2*X] = location[X] + 1
            queue.append(2 * X)


MAX = 1000001
N, K = map(int, input().split())
location = [MAX] * MAX

print(bfs(N, K))
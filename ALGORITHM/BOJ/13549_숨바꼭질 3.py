from collections import deque


def bfs(start, end):
    queue = deque([start])
    locations[start] = 0

    while queue:
        X = queue.popleft()

        if X == end:
            print(locations[X])

        for next_x in [X-1, X+1, X*2]:
            if 0 <= next_x < MAX and locations[next_x] > locations[X] + 1:
                if next_x == X*2:
                    locations[next_x] = locations[X]
                else:
                    locations[next_x] = locations[X] + 1
                queue.append(next_x)


MAX = 100001
N, K = map(int, input().split())
locations = [MAX] * MAX

bfs(N, K)
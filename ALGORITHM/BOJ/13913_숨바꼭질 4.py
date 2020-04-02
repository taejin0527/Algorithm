from collections import deque


def bfs(start, end):
    queue = deque([start])
    locations[start][0] = 0

    while queue:
        X = queue.popleft()

        if X == end:
            break

        for next_x in [X-1, X+1, X*2]:
            if 0 <= next_x < MAX and locations[X][0] + 1 < locations[next_x][0]:
                locations[next_x][0] = locations[X][0] + 1
                locations[next_x][1] = X
                queue.append(next_x)


MAX = 100001
N, K = map(int, input().split())
locations = [[MAX, MAX] for _ in range(MAX)]

bfs(N, K)

ans = [K]
T = K
while locations[T][1] != MAX:
    ans.append(locations[T][1])
    T = locations[T][1]

print(locations[K][0])
print(*reversed(ans))
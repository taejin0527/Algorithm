from collections import deque


def bfs(start, end):
    queue = deque([start])
    locations[start] = [0, 1]

    while queue:
        X = queue.popleft()

        for next_x in [X-1, X+1, X*2]:
            if 0 <= next_x < MAX:
                if locations[next_x][0] == MAX:
                    locations[next_x][0] = locations[X][0] + 1
                    locations[next_x][1] = locations[X][1]
                    queue.append(next_x)
                elif locations[X][0] + 1 == locations[next_x][0]:
                    locations[next_x][1] += locations[X][1]

    return locations[end]


MAX = 100001
N, K = map(int, input().split())
locations = [[MAX, 0] for _ in range(MAX)]

ans = bfs(N, K)
print(*ans, sep='\n')

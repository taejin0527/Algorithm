from collections import deque
from itertools import permutations
from copy import deepcopy

A, B, C = map(int, input().split())


def bfs():
    queue, visited, ans = deque(), [], []
    limit = [A, B, C]
    P = list(permutations([0, 1, 2], 2))

    queue.append([0, 0, C])
    visited.append([0, 0, C])
    while queue:
        buckets = queue.popleft()

        if buckets[0] == 0:
            ans.append(buckets[2])

        for i in range(len(P)):
            pour_from, pour_to = P[i][0], P[i][1]
            temp = deepcopy(buckets)

            if buckets[pour_from] + buckets[pour_to] > limit[pour_to]:
                temp[pour_from] = buckets[pour_from] + buckets[pour_to] - limit[pour_to]
                temp[pour_to] = limit[pour_to]
            else:
                temp[pour_from] = 0
                temp[pour_to] = buckets[pour_from] + buckets[pour_to]

            if temp not in visited:
                visited.append(temp)
                queue.append(temp)

    return ans


result = bfs()

print(*sorted(result))
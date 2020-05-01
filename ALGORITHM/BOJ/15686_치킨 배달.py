from itertools import combinations


N, M = map(int, input().split())
city = [[int(n) for n in input().split()] for _ in range(N)]
home, store = [], []


def find_store():
    for x in range(N):
        for y in range(N):
            if city[x][y] == 1:
                home.append((x, y))
            if city[x][y] == 2:
                store.append((x, y))


def close_store():
    min_cd = 1e9

    for survived in combinations(store, M):
        chicken_distance = 0

        for hx, hy in home:
            distance = 1e9

            for cx, cy in survived:
                distance = min(distance, abs(hx-cx) + abs(hy-cy))

            chicken_distance += distance

        min_cd = min(min_cd, chicken_distance)

    return min_cd


find_store()
ans = close_store()
print(ans)
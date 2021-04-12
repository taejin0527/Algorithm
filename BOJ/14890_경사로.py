N, L = map(int, input().split())
MAP = [[int(n) for n in input().split()] for _ in range(N)]


def count_slope(my_map):
    slope_cnt = 0

    for i in range(N):
        j = 0
        checked = [False] * N
        slope_ok = True

        while j < N - 1:
            cur, nxt = my_map[i][j], my_map[i][j + 1]       # 현재 블록과 다음 블록

            if cur == nxt:          # 높이가 같으면
                j = j + 1                                   # 다음 칸으로 이동
                continue
            elif cur == nxt + 1:    # 높은 곳 -> 낮은 곳
                slope = my_map[i][j + 1:j + 1 + L]          # 다음 블록부터 L개의 블록을 경사로 설정

                if slope.count(nxt) == L:                   # nxt와 높이가 같은 블록이 L개면
                    checked[j + 1:j + 1 + L] = [True] * L   # 경사를 설치하고
                    j = j + L                               # L 만큼 스킵
                    continue
                else:
                    slope_ok = False
                    break
            elif cur + 1 == nxt:    # 낮은 곳 -> 높은 곳
                slope = my_map[i][j + 1 - L:j + 1]

                if True not in checked[j + 1 - L:j + 1]\
                        and slope.count(cur) == L:          # 이전 L개의 블록에 경사가 없고 모두 높이가 cur와 같으면
                    # checked[j + 1 - L:j + 1] = [True] * L # 경사를 설치(크게 의미 없음)
                    j = j + 1                               # 다음 칸으로 이동
                    continue
                else:
                    slope_ok = False
                    break
            else:                   # 그 외(높이 차이가 1 이상일 때)
                slope_ok = False
                break

        if slope_ok:
            slope_cnt += 1

    return slope_cnt


ans = count_slope(MAP) + count_slope(list(zip(*MAP)))
print(ans)
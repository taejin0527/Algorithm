N, M, H = map(int, input().split())
L = [[False] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    L[a-1][b-1] = True


def min_ladder(cnt, x, y):                          # 현재 사다리 수, 탐색중인 위치(x, y)
    global ans, found_min

    if check_ladder():                              # 모든 조건을 만족하면
        ans = min(ans, cnt)                         # 최소값을 갱신
        return

    if cnt == 3:
        return

    if cnt >= ans:                                  # 최소값(ans)보다 커지면
        found_min = True                            # 불필요한 반복을 빠져나온다
        return

    for h in range(x, H):
        t = y if h == x else 0
        for n in range(t, N - 1):
            if found_min:                           # 이미 답을 찾았다면 빠져나온다
                break
            if L[h][n]:                             # 2개의 가로선이 연속되는 것을 방지
                n += 1
            else:
                L[h][n] = True
                min_ladder(cnt + 1, h, n+2)
                L[h][n] = False


def check_ladder():
    for n in range(N):                              # 1~N 세로선 마다
        player = n
        for h in range(H):                          # 세로(h)로 내려오면서
            if L[h][player]:                        # 오른쪽에 사다리가 있으면
                player += 1                         # 오른쪽으로 이동
            elif player != 0 and L[h][player-1]:    # 왼쪽에 사다리가 있으면(1번 세로선은 왼쪽이 없음)
                player -= 1                         # 왼쪽으로 이동
        if player != n:                             # 결과가 시작점과 같지 않으면 답이 아님
            return False
    return True                                     # 아무 이상이 없으면 통과


ans = 4
found_min = False
min_ladder(0, 0, 0)
print(ans if ans != 4 else -1)
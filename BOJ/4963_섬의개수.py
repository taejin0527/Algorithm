from collections import deque


def bfs(v):
    # 데크를 생성하고 기준으로 들어온 좌표를 넣어둔다.
    q = deque()
    q.append(v)

    # 8방향 탐색. 데크에 값이 없을 때 까지 탐색을 진행한다.
    while q:
        v = q.popleft()  # 맨 왼쪽 값을 제거한다.

        for a in range(8):  # 8방향 탐색을 위해 반복문 사용
            i = v[0] + di[a]  # 좌표 계산. di는 8방향의 행 값이 들어가 있다.
            j = v[1] + dj[a]  # 좌표 계산. dj는 8방향의 열 값이 들어가 있다.
            if 0 <= i <= h - 1 and 0 <= j <= w - 1 and ocean[i][j]:  # 1-8방향에 속하는 좌표가 유효한 좌표인지, 2-해당 좌표가 육지인지 확인
                ocean[i][j] = 0  # 육지를 0으로 바꿔 다음 탐색 때 걸리지 않게 함
                q.append([i, j])  # 해당 육지 좌표를 데크에 넣어 탐색의 대상이 되게 설정


# 8방향 좌표 설정
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())  # 지역의 너비와 높이를 받아옴
    if w == 0 and h == 0:  # 들어오는 모든 값이 0 0 이면 코드 종료
        break
    ocean = [list(map(int, input().split())) for _ in range(h)]  # 높이의 수에 맞게끔 데이터를 받아온다.
    cnt = 0  # 섬의 갯수 변수

    # 좌표 하나하나를 탐색하면서 육지가 있는지 확인
    for i in range(h):
        for j in range(w):
            if ocean[i][j]:  # 육지(1)가 있으면 일단 검색한다.
                cnt += 1  # 바로 갯수 추가. BFS 함수에서 연결된 육지는 모두 제거 되기에 중복 증가 X
                bfs([i, j])  # 해당 좌표를 넣고 주변 탐색

    print(cnt)
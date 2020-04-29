from collections import deque


"""
입력 -> 
    sprocket :  톱니바퀴는 12시방향부터 시계방향 순서로 입력
                (N극은 0, S극은 1)
    K        :  회전 횟수
    rotate   :  회전시킨 톱니바퀴의 번호(n), 회전 방향(d)
                                        (시계 방향: 1, 반시계 방향: -1)
    
출력 ->
    ans : 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력
        (톱니바퀴 12시방향이 S극 이면 각각 1, 2, 4, 8점 획득
                          N극 이면 모두 0점) 
"""
sprocket = [deque(map(int, input())) for _ in range(4)]
K = int(input())
rotate = deque([int(n) for n in input().split()] for _ in range(K))


def rotate_wheel():
    score = 0
    while rotate:                                       # 명령어가 남아 있다면
        n, d = rotate.popleft()                         # (번호, 방향)을 꺼내서
        n -= 1
        right, left = sprocket[n][2], sprocket[n][6]    # 비교를 위해 (n) 바퀴의 오른쪽, 왼쪽 값을 저장
        sprocket[n].rotate(d)                           # (n) 바퀴를 (d)방향으로 회전

        # 기준 바퀴의 왼쪽
        nxt_d = d
        for i in range(n-1, -1, -1):
            if sprocket[i][2] != left:
                nxt_d += -1
                left = sprocket[i][6]
                sprocket[i].rotate(nxt_d)
            else:
                break

        # 기준 바퀴의 오른쪽
        nxt_d = d
        for i in range(n + 1, 4):
            if sprocket[i][6] != right:
                nxt_d += -1
                right = sprocket[i][2]
                sprocket[i].rotate(nxt_d)
            else:
                break

    for i in range(4):
        if sprocket[i][0] == 1:
            score += 2**i

    return score

ans = rotate_wheel()

print(ans)
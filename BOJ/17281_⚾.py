"""
@params
N               이닝 수
[scores] * N    이닝에서 얻는 결과

@return
answer          아인타팀이 얻을 수 있는 최대 점수
"""

from sys import stdin
input = stdin.readline

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
battingOrder = [-1] * 9             # 타순
check = [False] * 9                 # 타순에 선수가 있는지 확인
answer = 0

battingOrder[3] = 0                 # 4번 타자는 1번 선수로 고정
check[3] = True

def dfs(player):
    global answer

    if player == 9:
        cur, score = 0, 0           # 현재 타순, 점수

        for inning in innings:
            # 매 이닝마다 베이스, 아웃 카운트는 초기화, 
            b1, b2, b3 = 0, 0, 0        # 1~3루
            outCnt = 0                  # 아웃 카운

            # 3 아웃되면 이닝 종료
            while outCnt < 3:
                batter = battingOrder[cur]              # 타자 번호

                if inning[batter] == 0:                 # 아웃: 모든 주자는 진루하지 못하고, 
                    outCnt += 1                         #      공격 팀에 아웃이 하나 증가한다.
                elif inning[batter] == 1:               # 안타: 
                    score += b3                         #      3루 주자는 점수 득점
                    b1, b2, b3 = 1, b1, b2              #      타자와 모든 주자가 한 루씩 진루한다.
                elif inning[batter] == 2:               # 2루타: 타자와 모든 주자가 두 루씩 진루한다.
                    score += b2 + b3                    #       2,3루 주자 득점
                    b1, b2, b3 = 0, 1, b1               #       타자는 2루로, 1루->3루
                elif inning[batter] == 3:               # 3루타: 타자와 모든 주자가 세 루씩 진루한다.
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                elif inning[batter] == 4:               # 홈런: 타자와 모든 주자가 홈까지 진루한다.
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

                cur = (cur+1)%9                         # 다음 타순

        # 모든 이닝이 종료되면 최대값 계산
        answer = max(answer, score)

        return

    for i in range(9):
        if check[i]:
            continue
        check[i] = True
        battingOrder[i] = player
        dfs(player + 1)
        check[i] = False
        battingOrder[i] = -1

dfs(1)
print(answer)
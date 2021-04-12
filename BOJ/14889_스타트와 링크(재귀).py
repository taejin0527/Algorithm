n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]

myteam = [False] * n  # 팀을 구분한다. True-> 스타트팀, False->링크팀
answer = 1e9


def solve(count, index):
    global answer

    if index == n:  # 전체 N명에 대해서 확인이 끝났다면 종료
        return
    if count == n // 2:
        s_team, link_team = 0, 0  # 스타트팀, 링크팀
        for i in range(n):
            for j in range(n):
                if myteam[i] and myteam[j]:  # 스타트팀
                    s_team += team[i][j]  # 능력치를 구한다.
                if not myteam[i] and not myteam[j]:  # 링크팀
                    link_team += team[i][j]
        answer = min(answer, abs(s_team - link_team))  # 두 팀의 능력치 차이가 최소가 되는 값
        return

    myteam[index] = True  # 스타트팀
    solve(count + 1, index + 1)
    myteam[index] = False  # 링크팀
    solve(count, index + 1)


solve(0, 0)
print(answer)
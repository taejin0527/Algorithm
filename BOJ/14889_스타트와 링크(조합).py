from itertools import combinations


N = int(input())
S = [[int(n) for n in input().split()] for _ in range(N)]


def solve():
    players = [n for n in range(N)]
    div_team = list(combinations(players, N//2))
    min_ability = 100 * N//2

    for comb in div_team:
        start_team = list(combinations(comb, 2))
        link_team = list(combinations((set(players) - set(comb)), 2))

        start_ability, link_ability = 0, 0
        for i, j in start_team:
            start_ability += (S[i][j] + S[j][i])
        for i, j in link_team:
            link_ability += (S[i][j] + S[j][i])

        min_ability = min(min_ability, abs(start_ability - link_ability))

    return min_ability


print(solve())

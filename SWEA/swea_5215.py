
food = ["상추", "고기", "토마토", "치즈", "피클"]

for tc in range(1, int(input())+1):
    N, L = map(int, input().split()) # 재료, 제한칼로리

    score, calorie = [], []

    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)

    for i in range(1 << N):
        sum_score, sum_calorie = 0, 0
        for j in range(N):
            if i & (1<<j):
                sum_score += score[j]
                sum_calorie += calorie[j]

        if sum_calorie <= L:
            ans = max(ans, sum_score)

    print('#{} {}'.format(tc, ans))

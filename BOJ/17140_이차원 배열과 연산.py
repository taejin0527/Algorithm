from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

time = 0
while time <= 100:
    if r <= len(A) and c <= len(A[0]) and A[r - 1][c - 1] == k:
        print(time)
        break

    time += 1

    C_flag = False      # C연산인 경우 : transpose
    if len(A) < len(A[0]):
        C_flag = True
        A = list(zip(*A))

    max_len = 0
    tmp_a = []
    for now_row in A:
        ct = Counter(now_row)
        if ct.get(0):  # 0은 카운팅하지 않음
            del ct[0]
        num_cnt = list(map(list, ct.items()))
        num_cnt.sort(key=lambda x: (x[1], x[0]))         # 주어진 순서대로 정렬
        tmp_a.append(list(sum(num_cnt, []))[:100])       # 100개를 초과하는 경우 100개 까지만
        max_len = max(max_len, len(tmp_a[-1]))

    for i in range(len(tmp_a)):
        if len(tmp_a[i]) < max_len:
            tmp_a[i] += [0] * (max_len - len(tmp_a[i]))  # 길이 맞춰주기

    A = tmp_a
    if C_flag:  # 다시 transpose
        A = list(zip(*A))


if time > 100:
    print(-1)
"""
이진수 : binary number
이친수 : pinary number
    - 이친수는 0으로 시작하지 않는다.
    - 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
"""

pinary_number = [[0] * 2 for _ in range(91)]
for i in range(91):
    for j in range(2):
        if i == 1 and j == 1:
            pinary_number[i][j] = 1
        elif i == 2 and j == 0:
            pinary_number[i][j] = 1
        else:
            if j == 1:
                pinary_number[i][j] = pinary_number[i-1][0]
            elif j == 0:
                pinary_number[i][j] = pinary_number[i-1][1] + pinary_number[i-1][0]

N = int(input())
print(sum(pinary_number[N]))

"""
# 피보나치 수열로도 풀 수 있다

N = int(input())

if N == 1 or N == 2:
    print(1)
else:
    f_start = 1
    f_next = 1
    for _ in range(N - 2):
        f_start, f_next = f_next, f_start + f_next
    print(f_next)
"""
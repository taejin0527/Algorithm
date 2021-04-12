N = int(input())
A = [[int(n) for n in input().split()] for _ in range(N)]

result = []
for y in range(N):
    for x in range(N):
        for d1 in range(1, min(x, N - y - 1) + 1):
            for d2 in range(1, min(N - x - 1, N - y - 1) + 1):
                if y + d1 + d2 <= N - 1:
                    value1, value2, value3, value4, value5 = 0, 0, 0, 0, 0

                    for a in range(N):
                        for b in range(N):
                            if x + y <= a + b <= x + y + 2 * d2 and y - x <= a - b <= y - x + 2 * d1:
                                value5 += A[a][b]
                            elif 0 <= a < y + d1 and 0 <= b <= x and a + b < y + x:
                                value1 += A[a][b]
                            elif 0 <= a <= y + d2 and x < b <= N - 1 and a - b < y - x:
                                value2 += A[a][b]
                            elif y + d1 <= a <= N - 1 and 0 <= b < x - d1 + d2 and a - b > y - x + 2 * d1:
                                value3 += A[a][b]
                            elif y + d2 < a <= N - 1 and x - d1 + d2 <= b <= N - 1 and a + b > y + x + 2 * d2:
                                value4 += A[a][b]
                    result.append(max(value1, value2, value3, value4, value5) - min(value1, value2, value3, value4, value5))


print(min(result))

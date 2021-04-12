# 1 <= N <= 100,000
N = int(input())
d = [0] * 100001
square_num = [n**2 for n in range(1, 317)]

for i in range(1, N+1):
    temp = []
    for j in square_num:
        if j > i:
            break
        temp.append(d[i-j])
    d[i] = min(temp) + 1

print(d[N])
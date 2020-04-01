mod = 1000000000
stair_number = [[0] * 10 for _ in range(101)]

for i in range(1, 101):
    for j in range(10):
        if i == 1 and j != 0:
            stair_number[i][j] = 1
        else:
            if j == 0:
                stair_number[i][j] = stair_number[i-1][j+1]
            elif j == 9:
                stair_number[i][j] = stair_number[i-1][j-1]
            else:
                stair_number[i][j] = stair_number[i-1][j-1] + stair_number[i-1][j+1]

N = int(input())
print(sum(stair_number[N]) % mod)
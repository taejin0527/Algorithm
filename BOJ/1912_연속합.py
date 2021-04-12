N = int(input())
num_list = [int(n) for n in input().split()]
temp = [0] * N
result = -1000

for i in range(N):
    temp[i] = max(temp[i - 1] + num_list[i], num_list[i])
    result = max(result, temp[i])

print(result)
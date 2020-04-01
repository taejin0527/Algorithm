N = int(input())
numbers = [int(n) for n in input().split()]
seq_len = [1] * N
seq_num = [[num] for num in numbers]
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j] and seq_len[i] < seq_len[j] + 1:
            seq_num[i] = seq_num[j] + [numbers[i]]
            seq_len[i] = seq_len[j] + 1

max_len, p = 0, 0
for i in range(N):
    if max_len < seq_len[i]:
        max_len = seq_len[i]
        p = i
print(max_len)
print(*seq_num[p])

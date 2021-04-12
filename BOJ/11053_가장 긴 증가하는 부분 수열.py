N_size = 1000
N = int(input())
numbers = [int(n) for n in input().split()]
seq_num = [0] * N
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j] and seq_num[i] < seq_num[j]:
            seq_num[i] = seq_num[j]
    seq_num[i] += 1

print(max(seq_num))
T = int(input())
calc_nums = [[10],
             [1],
             [6, 2, 4, 8],
             [1, 3, 9, 7],
             [6, 4],
             [5],
             [6],
             [1, 7, 9, 3],
             [6, 8, 4, 2],
             [1, 9]]
for _ in range(T):
    a, b = [int(n) for n in input().split()]
    i_a = a % 10
    i_b = b % len(calc_nums[i_a])
    print(calc_nums[i_a][i_b])

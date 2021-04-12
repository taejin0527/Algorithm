from itertools import combinations

L, C = map(int, input().split())
A = input().split()

vowels = 'aeiou'
for password in combinations(sorted(A), L):
    v_cnt, c_cnt = 0, 0

    for p in password:
        if p in vowels:
            v_cnt += 1
        else:
            c_cnt += 1

    if v_cnt >= 1 and c_cnt >= 2:
        print(*password, sep='')

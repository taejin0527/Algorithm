def calc_operator(add, sub, mul, div, result, num_idx):
    global MAX, MIN
    if num_idx == N:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return

    if add:
        calc_operator(add - 1, sub, mul, div, result + A[num_idx], num_idx + 1)
    if sub:
        calc_operator(add, sub - 1, mul, div, result - A[num_idx], num_idx + 1)
    if mul:
        calc_operator(add, sub, mul - 1, div, result * A[num_idx], num_idx + 1)
    if div:
        # 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
        if result > 0:
            calc_operator(add, sub, mul, div - 1, result // A[num_idx] , num_idx + 1)
        else:
            calc_operator(add, sub, mul, div - 1, -(abs(result) // A[num_idx]), num_idx + 1)


N = int(input())
A = [int(n) for n in input().split()]
a, s, m, d = [int(n) for n in input().split()]

MAX, MIN = -1e9, 1e9

calc_operator(a, s, m, d, A[0], 1)
print(MAX)
print(MIN)
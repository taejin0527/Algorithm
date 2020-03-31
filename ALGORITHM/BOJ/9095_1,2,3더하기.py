def dynamic_plus(n):
    if n in (1, 2):
        return n
    if n == 3:
        return 4
    return dynamic_plus(n-1) + dynamic_plus(n-2) + dynamic_plus(n-3)


for _ in range(int(input())):
    n = int(input())
    print(dynamic_plus(n))
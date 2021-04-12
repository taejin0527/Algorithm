from itertools import combinations


def gcd(a, b):
    return a if not b else gcd(b, a % b)


for test_case in range(int(input())):
    n, *numbers = map(int, input().split())

    result = 0
    for comb in combinations(numbers, 2):
        result += gcd(comb[0], comb[1])
    print(result)
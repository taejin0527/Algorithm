def gcd(a, b):
    return gcd(b, a%b) if b else a


def lcm(a, b):
    return a * b // gcd(a, b)


T = int(input())
for _ in range(T):
    A, B = [int(n) for n in input().split()]
    print(lcm(A, B))
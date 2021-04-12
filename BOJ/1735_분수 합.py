def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)


n_a, d_a = map(int, input().split())
n_b, d_b = map(int, input().split())
numerator = n_a*d_b + n_b*d_a
denominator = d_a*d_b
GCD = gcd(numerator, denominator)

print(numerator//GCD, denominator//GCD)
a = int(input())
b = int(input())
f = a * b

while b // 10 > 0:
    print(a * (b % 10))
    b //= 10
print(a * (b % 10))
print(f)

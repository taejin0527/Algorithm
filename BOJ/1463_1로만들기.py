num = int(input())

fx = [0 for _ in range(num + 1)]
for i in range(1, num + 1):
    if i == 1:
        fx[i] = 0
        continue

    fx[i] = fx[i-1] + 1
    if i % 3 == 0 and fx[i//3] + 1 < fx[i]:
        fx[i] = fx[i//3] + 1
    if i % 2 == 0 and fx[i//2] +1 < fx[i]:
        fx[i] = fx[i//2] + 1

print(fx[-1])
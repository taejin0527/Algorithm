n = int(input())
rectangle = [1, 1]
for i in range(2, n+1):
    rectangle.append(2* rectangle[i-2] + rectangle[i-1])

print(rectangle[n] % 10007)